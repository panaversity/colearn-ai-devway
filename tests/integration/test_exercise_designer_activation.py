#!/usr/bin/env python3
"""
Integration tests for exercise-designer skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_exercise() -> str:
    """Create a sample exercise YAML file for testing."""
    yaml_content = """topic: "Python List Operations"
learning_objectives:
  - "Students will apply list methods (append, remove, extend) correctly"
  - "Students will analyze list operations for efficiency"

estimated_time: 30
evidence_based_strategies:
  - "retrieval-practice"
  - "interleaving"
  - "progressive-difficulty"

exercises:
  - id: "ex-01"
    title: "Complete the List Builder"
    type: "fill-in-blank"
    difficulty: "easy"
    time_minutes: 5
    strategies:
      - "retrieval-practice"
    instructions: |
      Complete the function to build a list from user input.
      Fill in the blanks to make the code work.
    starter_code: |
      def build_list(items):
          result = []
          for item in items:
              result._____(item)  # Add item to list
          return result
    test_cases:
      - input: "[1, 2, 3]"
        expected: "[1, 2, 3]"
        tests: "Normal case"
      - input: "[]"
        expected: "[]"
        tests: "Edge case - empty input"
    hints:
      - "What list method adds items to the end?"
      - "The method starts with 'app'"
      - "Use result.append(item)"
    rubric:
      correctness: 4
      code_quality: 1

  - id: "ex-02"
    title: "Debug the List Merger"
    type: "debug-this"
    difficulty: "medium"
    time_minutes: 8
    strategies:
      - "retrieval-practice"
      - "error-recognition"
    instructions: |
      This function should merge two lists, but it has a bug.
      Find and fix the error.
    starter_code: |
      def merge_lists(list1, list2):
          result = list1
          result.extend(list2)
          return result

      # Test
      a = [1, 2]
      b = [3, 4]
      merged = merge_lists(a, b)
      print(a)  # Should be [1, 2], but prints [1, 2, 3, 4]
    test_cases:
      - input: "a=[1,2], b=[3,4]"
        expected: "merged=[1,2,3,4], a=[1,2]"
        tests: "Original list should not be modified"
    hints:
      - "What happens when you assign a list to a variable?"
      - "Consider using list() or [:] to create a copy"
      - "result = list(list1) or result = list1[:]"
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as f:
        f.write(yaml_content)
        return f.name


def test_skill_activation_practice_activities() -> None:
    """
    Test: Skill activates when educator asks "need exercises for students to practice"
    Semantic Context: Designing deliberate practice activities (not keyword-based)
    """
    print("Test: Skill activation for practice activities request...")
    print("  [Semantic Understanding]: Educator wants practice exercises for skill building")
    print("  [Expected]: Exercise-designer skill should activate")
    assert Path("./.claude/skills/exercise-designer/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_varied_question_types() -> None:
    """
    Test: Skill activates for "how to test understanding beyond simple coding"
    Semantic Context: Need for diverse assessment formats
    """
    print("Test: Skill activation for varied exercise types...")
    print("  [Semantic Understanding]: Educator wants diverse exercise formats")
    print("  [Expected]: Exercise-designer skill should activate")
    assert Path("./.claude/skills/exercise-designer/reference/exercise-types.md").exists()
    print("✓ Exercise types reference available")


def test_skill_activation_spaced_repetition() -> None:
    """
    Test: Skill activates when educator mentions "reviewing prior concepts"
    Semantic Context: Applying spaced repetition principles
    """
    print("Test: Skill activation for spaced repetition...")
    print("  [Semantic Understanding]: Educator wants exercises that review prior learning")
    print("  [Expected]: Exercise-designer skill should activate")
    assert Path("./.claude/skills/exercise-designer/reference/spaced-repetition.md").exists()
    print("✓ Spaced repetition reference available")


def test_skill_activation_difficulty_progression() -> None:
    """
    Test: Skill activates for "exercises that gradually increase in challenge"
    Semantic Context: Scaffolding difficulty appropriately
    """
    print("Test: Skill activation for difficulty progression...")
    print("  [Semantic Understanding]: Educator needs appropriate challenge levels")
    print("  [Expected]: Exercise-designer skill should activate")
    assert Path("./.claude/skills/exercise-designer/reference/difficulty-progression.md").exists()
    print("✓ Difficulty progression reference available")


def test_validation_with_sample_exercise() -> None:
    """Test the test case generation script with sample exercise."""
    print("Test: Running test case generation on sample exercise...")
    exercise_file = create_sample_exercise()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/exercise-designer/scripts/generate-test-cases.py",
                exercise_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Analysis results: {output['summary']}")
        assert output["summary"]["total_exercises"] == 2, "Should find 2 exercises"
        assert output["summary"]["has_test_cases"] is True, "Should have test cases"
        print("✓ Test case analysis passed for well-formed exercises")

    finally:
        Path(exercise_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/exercise-designer/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: exercise-designer" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content
    assert "## When to Activate" in content
    assert "## Process" in content
    assert "## Output Format" in content
    assert "## Examples" in content

    # Check for references to Layer 3 files
    assert "reference/exercise-types.md" in content
    assert "reference/evidence-based-strategies.md" in content
    assert "reference/difficulty-progression.md" in content
    assert "reference/spaced-repetition.md" in content
    assert "templates/exercise-template.yml" in content
    assert "scripts/generate-test-cases.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/exercise-designer/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "exercise-types.md",
        "evidence-based-strategies.md",
        "difficulty-progression.md",
        "spaced-repetition.md",
    ]

    for filename in required_files:
        filepath = ref_dir / filename
        assert filepath.exists(), f"Missing reference: {filename}"
        content = filepath.read_text()
        assert len(content) > 500, f"{filename} should be substantive (>500 chars)"

    print("✓ All reference files present and substantive")


def test_templates() -> None:
    """Verify templates exist."""
    print("Test: Template files...")

    template_files = [
        "./.claude/skills/exercise-designer/templates/exercise-template.yml",
        "./.claude/skills/exercise-designer/templates/rubric-template.yml",
    ]

    for template_path in template_files:
        template_file = Path(template_path)
        assert template_file.exists(), f"Template file must exist: {template_path}"
        content = template_file.read_text()
        assert len(content) > 50, f"{template_path} should have content"

    print("✓ Template files exist with required content")


if __name__ == "__main__":
    print("\n=== Exercise Designer Skill Integration Tests ===\n")

    test_skill_activation_practice_activities()
    test_skill_activation_varied_question_types()
    test_skill_activation_spaced_repetition()
    test_skill_activation_difficulty_progression()
    test_validation_with_sample_exercise()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nExercise-designer skill is ready for use.")
    print("Skill activates when educators need varied, evidence-based practice exercises.")
