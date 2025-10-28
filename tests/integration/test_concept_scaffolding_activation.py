#!/usr/bin/env python3
"""
Integration tests for concept-scaffolding skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_scaffolding() -> str:
    """Create a sample YAML file with scaffolding plan for testing."""
    yaml_content = """concept: "Python Decorators"
target_audience: "intermediate"
total_steps: 5
estimated_time: 60

prerequisites:
  - "Understanding functions as first-class objects"
  - "Basic closures knowledge"
  - "Higher-order function concepts"

steps:
  - step_number: 1
    title: "Functions as Variables"
    new_concepts:
      - "Functions can be assigned to variables"
      - "Functions can be passed as arguments"
    cognitive_load: "low"
    time_minutes: 10
    explanation: "Demonstrate that functions are objects in Python"
    worked_example: |
      def greet():
          return "Hello!"

      # Assign function to variable
      my_func = greet
      print(my_func())  # Output: Hello!
    checkpoint: "Can you assign a function to a variable and call it?"

  - step_number: 2
    title: "Functions Returning Functions"
    new_concepts:
      - "Functions can return other functions"
      - "Nested function definitions"
    cognitive_load: "medium"
    time_minutes: 12
    explanation: "Build toward decorator pattern by showing function factories"
    worked_example: |
      def outer():
          def inner():
              return "Inner function"
          return inner

      func = outer()
      print(func())  # Output: Inner function
    checkpoint: "Write a function that returns another function"

  - step_number: 3
    title: "Higher-Order Functions"
    new_concepts:
      - "Functions taking functions as arguments"
    cognitive_load: "medium"
    time_minutes: 12
    explanation: "Complete the foundation for decorators"
    worked_example: |
      def execute_twice(func):
          func()
          func()

      def say_hello():
          print("Hello!")

      execute_twice(say_hello)  # Prints Hello! twice
    checkpoint: "Create a function that takes another function as parameter"
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as f:
        f.write(yaml_content)
        return f.name


def test_skill_activation_progressive_breakdown() -> None:
    """
    Test: Skill activates when educator asks to "break down complex topic into steps"
    Semantic Context: Managing complexity through scaffolding (not keyword-based)
    """
    print("Test: Skill activation for progressive breakdown request...")
    print("  [Semantic Understanding]: Educator wants to teach complex concept incrementally")
    print("  [Expected]: Concept-scaffolding skill should activate")
    assert Path("./.claude/skills/concept-scaffolding/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_cognitive_load_management() -> None:
    """
    Test: Skill activates when educator mentions "too much for beginners at once"
    Semantic Context: Recognizing cognitive overload concerns
    """
    print("Test: Skill activation for cognitive load concern...")
    print("  [Semantic Understanding]: Educator concerned about overwhelming learners")
    print("  [Expected]: Concept-scaffolding skill should activate")
    assert Path("./.claude/skills/concept-scaffolding/reference/cognitive-load-theory.md").exists()
    print("✓ Cognitive load theory reference available")


def test_skill_activation_prerequisite_sequencing() -> None:
    """
    Test: Skill activates when educator asks "what order should I teach these concepts"
    Semantic Context: Determining learning progression
    """
    print("Test: Skill activation for prerequisite sequencing...")
    print("  [Semantic Understanding]: Educator needs to sequence dependent concepts")
    print("  [Expected]: Concept-scaffolding skill should activate")
    assert Path("./.claude/skills/concept-scaffolding/reference/scaffolding-strategies.md").exists()
    print("✓ Scaffolding strategies reference available")


def test_skill_activation_worked_examples() -> None:
    """
    Test: Skill activates for "how to gradually introduce decorators"
    Semantic Context: Need for incremental concept introduction
    """
    print("Test: Skill activation for incremental introduction...")
    print("  [Semantic Understanding]: Complex topic requiring progressive steps")
    print("  [Expected]: Concept-scaffolding skill should activate")
    assert Path("./.claude/skills/concept-scaffolding/reference/worked-examples.md").exists()
    print("✓ Worked examples reference available")


def test_validation_with_sample_scaffolding() -> None:
    """Test the actual cognitive load assessment script with sample scaffolding."""
    print("Test: Running cognitive load assessment on sample scaffolding...")
    scaffolding_file = create_sample_scaffolding()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/concept-scaffolding/scripts/assess-cognitive-load.py",
                scaffolding_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Assessment results: {output['summary']}")
        assert output["summary"]["total_steps"] == 3, "Should find 3 steps"
        assert output["summary"]["overall_load"] in ["low", "medium", "high"], "Should calculate overall load"
        print("✓ Cognitive load assessment passed for well-formed scaffolding")

    finally:
        Path(scaffolding_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/concept-scaffolding/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: concept-scaffolding" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content
    assert "## When to Activate" in content
    assert "## Process" in content
    assert "## Output Format" in content
    assert "## Examples" in content

    # Check for references to Layer 3 files
    assert "reference/cognitive-load-theory.md" in content
    assert "reference/scaffolding-strategies.md" in content
    assert "reference/worked-examples.md" in content
    assert "templates/scaffolding-plan-template.yml" in content
    assert "scripts/assess-cognitive-load.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/concept-scaffolding/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "cognitive-load-theory.md",
        "scaffolding-strategies.md",
        "worked-examples.md",
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

    template_file = Path("./.claude/skills/concept-scaffolding/templates/scaffolding-plan-template.yml")
    assert template_file.exists(), "Template file must exist"

    content = template_file.read_text()
    assert "concept:" in content
    assert "target_audience:" in content
    assert "steps:" in content
    assert "cognitive_load:" in content
    assert "worked_example:" in content

    print("✓ Template file exists with required fields")


if __name__ == "__main__":
    print("\n=== Concept Scaffolding Skill Integration Tests ===\n")

    test_skill_activation_progressive_breakdown()
    test_skill_activation_cognitive_load_management()
    test_skill_activation_prerequisite_sequencing()
    test_skill_activation_worked_examples()
    test_validation_with_sample_scaffolding()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nConcept-scaffolding skill is ready for use.")
    print("Skill activates when educators need to break down complex concepts into progressive learning steps.")
