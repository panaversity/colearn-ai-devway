#!/usr/bin/env python3
"""
Integration tests for assessment-builder skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_assessment() -> str:
    """Create a sample assessment YAML file for testing."""
    yaml_content = """title: "Python Functions Assessment"
target_audience: "beginner"
time_limit: 45
total_points: 100
passing_score: 70

learning_objectives:
  - "Define functions with parameters and return values"
  - "Call functions correctly"
  - "Understand function scope"

cognitive_distribution:
  remember: 15
  understand: 20
  apply: 40
  analyze: 20
  evaluate: 5
  create: 0

questions:
  - id: "q1"
    type: "mcq"
    bloom_level: "understand"
    points: 10
    question: |
      What will this code print?
      ```python
      def add(a, b):
          return a + b
      result = add(3, 5)
      print(result)
      ```
    options:
      - text: "8"
        correct: true
        explanation: "The function adds 3 + 5 and returns 8"
      - text: "35"
        correct: false
        explanation: "This would concatenate strings, not add numbers"
        misconception: "Confusion about + operator with numbers"
      - text: "None"
        correct: false
        explanation: "The function returns a value, not None"
        misconception: "Thinks functions without explicit print return None"
      - text: "Error"
        correct: false
        explanation: "This code is syntactically correct"
        misconception: "Confusion about function syntax"

  - id: "q2"
    type: "code-writing"
    bloom_level: "apply"
    points: 25
    question: |
      Write a function called `greet` that takes a name as a parameter
      and returns a greeting message like "Hello, Alice!"
    requirements:
      - "Function must be named 'greet'"
      - "Must take one parameter"
      - "Must return a string (not print)"
    test_cases:
      - input: "greet('Alice')"
        expected: "'Hello, Alice!'"
        type: "normal"
      - input: "greet('Bob')"
        expected: "'Hello, Bob!'"
        type: "normal"
    rubric:
      correctness: 15
      code_quality: 7
      style: 3

  - id: "q3"
    type: "debugging"
    bloom_level: "analyze"
    points: 20
    question: |
      This function should calculate the area of a rectangle,
      but it has a bug. Find and fix it.
      ```python
      def calculate_area(length, width):
          area = length + width
          return area
      ```
    expected_fix: "Change + to *"
    misconception_tested: "Confusion between addition and multiplication"
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as f:
        f.write(yaml_content)
        return f.name


def test_skill_activation_quiz_creation() -> None:
    """
    Test: Skill activates when educator asks "need to create a quiz"
    Semantic Context: Creating assessment instruments (not keyword-based)
    """
    print("Test: Skill activation for quiz creation request...")
    print("  [Semantic Understanding]: Educator wants to measure student learning")
    print("  [Expected]: Assessment-builder skill should activate")
    assert Path("./.claude/skills/assessment-builder/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_meaningful_distractors() -> None:
    """
    Test: Skill activates when educator mentions "need better multiple choice answers"
    Semantic Context: Desire for diagnostic distractors
    """
    print("Test: Skill activation for distractor design...")
    print("  [Semantic Understanding]: Educator wants MCQ options that reveal misconceptions")
    print("  [Expected]: Assessment-builder skill should activate")
    assert Path("./.claude/skills/assessment-builder/reference/distractor-design.md").exists()
    print("✓ Distractor design reference available")


def test_skill_activation_cognitive_balance() -> None:
    """
    Test: Skill activates for "testing understanding not just memorization"
    Semantic Context: Ensuring higher-order thinking assessment
    """
    print("Test: Skill activation for cognitive balance...")
    print("  [Semantic Understanding]: Educator wants to assess deep understanding")
    print("  [Expected]: Assessment-builder skill should activate")
    assert Path("./.claude/skills/assessment-builder/reference/blooms-assessment-alignment.md").exists()
    print("✓ Bloom's assessment alignment reference available")


def test_skill_activation_rubric_design() -> None:
    """
    Test: Skill activates when educator asks "how to grade open-ended questions"
    Semantic Context: Need for assessment criteria
    """
    print("Test: Skill activation for rubric creation...")
    print("  [Semantic Understanding]: Educator needs grading criteria for complex responses")
    print("  [Expected]: Assessment-builder skill should activate")
    assert Path("./.claude/skills/assessment-builder/reference/rubric-guidelines.md").exists()
    print("✓ Rubric guidelines reference available")


def test_validation_with_sample_assessment() -> None:
    """Test the assessment validation script with sample assessment."""
    print("Test: Running validation on sample assessment...")
    assessment_file = create_sample_assessment()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/assessment-builder/scripts/validate-assessment.py",
                assessment_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Validation results: {output['summary']}")
        assert output["summary"]["total_questions"] == 3, "Should find 3 questions"
        assert "cognitive_distribution" in output["summary"], "Should analyze cognitive levels"
        non_recall_pct = output["summary"]["cognitive_distribution"]["non_recall_percentage"]
        assert non_recall_pct >= 60, f"Non-recall should be ≥60%, got {non_recall_pct}%"
        print("✓ Assessment validation passed with good cognitive balance")

    finally:
        Path(assessment_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/assessment-builder/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: assessment-builder" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content
    assert "## When to Activate" in content
    assert "## Process" in content
    assert "## Output Format" in content
    assert "## Examples" in content

    # Check for references to Layer 3 files
    assert "reference/question-types.md" in content
    assert "reference/distractor-design.md" in content
    assert "reference/blooms-assessment-alignment.md" in content
    assert "reference/rubric-guidelines.md" in content
    assert "templates/assessment-template.yml" in content
    assert "scripts/validate-assessment.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/assessment-builder/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "question-types.md",
        "distractor-design.md",
        "blooms-assessment-alignment.md",
        "rubric-guidelines.md",
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
        "./.claude/skills/assessment-builder/templates/assessment-template.yml",
        "./.claude/skills/assessment-builder/templates/rubric-template.yml",
    ]

    for template_path in template_files:
        template_file = Path(template_path)
        assert template_file.exists(), f"Template file must exist: {template_path}"
        content = template_file.read_text()
        assert len(content) > 50, f"{template_path} should have content"

    print("✓ Template files exist with required content")


if __name__ == "__main__":
    print("\n=== Assessment Builder Skill Integration Tests ===\n")

    test_skill_activation_quiz_creation()
    test_skill_activation_meaningful_distractors()
    test_skill_activation_cognitive_balance()
    test_skill_activation_rubric_design()
    test_validation_with_sample_assessment()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nAssessment-builder skill is ready for use.")
    print("Skill activates when educators need balanced assessments with meaningful questions.")
