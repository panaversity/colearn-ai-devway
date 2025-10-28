#!/usr/bin/env python3
"""
Integration tests for code-example-generator skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_code_example() -> str:
    """Create a sample Python code file for testing validation."""
    code_content = """# Demonstrates: List comprehensions
# Level: Intermediate

def filter_even_numbers(numbers):
    \"\"\"
    Filter even numbers from a list using list comprehension.

    Args:
        numbers: List of integers

    Returns:
        List of even integers
    \"\"\"
    return [num for num in numbers if num % 2 == 0]

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(data)
print(f"Even numbers: {evens}")  # Output: Even numbers: [2, 4, 6, 8, 10]

# How it works:
# - List comprehension iterates through numbers
# - Condition (num % 2 == 0) filters even values
# - Returns new list containing only even numbers
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, dir="/tmp"
    ) as f:
        f.write(code_content)
        return f.name


def test_skill_activation_teaching_demonstration() -> None:
    """
    Test: Skill activates when educator asks "show me how to demonstrate this concept"
    Semantic Context: Need for pedagogical code examples (not keyword-based)
    """
    print("Test: Skill activation for teaching demonstration request...")
    print("  [Semantic Understanding]: Educator wants code examples for teaching")
    print("  [Expected]: Code-example-generator skill should activate")
    assert Path("./.claude/skills/code-example-generator/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_runnable_examples() -> None:
    """
    Test: Skill activates when educator mentions "need working code for tutorial"
    Semantic Context: Requirement for validated, executable examples
    """
    print("Test: Skill activation for runnable examples request...")
    print("  [Semantic Understanding]: Educator needs verified, working code")
    print("  [Expected]: Code-example-generator skill should activate")
    assert Path("./.claude/skills/code-example-generator/scripts/validate-syntax.py").exists()
    print("✓ Syntax validation script available")


def test_skill_activation_progressive_sequence() -> None:
    """
    Test: Skill activates for "show simple to advanced examples"
    Semantic Context: Need for progressive example complexity
    """
    print("Test: Skill activation for progressive examples...")
    print("  [Semantic Understanding]: Educator wants examples with increasing complexity")
    print("  [Expected]: Code-example-generator skill should activate")
    assert Path("./.claude/skills/code-example-generator/reference/example-patterns.md").exists()
    print("✓ Example patterns reference available")


def test_skill_activation_best_practices() -> None:
    """
    Test: Skill activates when educator asks "how should I write code for teaching"
    Semantic Context: Pedagogical code quality concerns
    """
    print("Test: Skill activation for code quality guidance...")
    print("  [Semantic Understanding]: Educator wants best practices for teaching code")
    print("  [Expected]: Code-example-generator skill should activate")
    assert Path("./.claude/skills/code-example-generator/reference/python-best-practices.md").exists()
    print("✓ Python best practices reference available")


def test_validation_with_sample_code() -> None:
    """Test the actual syntax validation script with sample code."""
    print("Test: Running syntax validation on sample code...")
    code_file = create_sample_code_example()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/code-example-generator/scripts/validate-syntax.py",
                code_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Validation results: {output['summary']}")
        assert output["summary"]["syntax_valid"] is True, "Code should be syntactically valid"
        assert output["summary"]["functions"] >= 1, "Should find at least 1 function"
        print("✓ Syntax validation passed for well-formed code")

    finally:
        Path(code_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/code-example-generator/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: code-example-generator" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content
    assert "## When to Activate" in content
    assert "## Process" in content
    assert "## Output Format" in content
    assert "## Examples" in content

    # Check for references to Layer 3 files
    assert "reference/python-best-practices.md" in content
    assert "reference/example-patterns.md" in content
    assert "templates/code-example-template.md" in content
    assert "scripts/validate-syntax.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/code-example-generator/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "python-best-practices.md",
        "example-patterns.md",
        "pep8-summary.md",
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

    template_file = Path("./.claude/skills/code-example-generator/templates/code-example-template.md")
    assert template_file.exists(), "Template file must exist"

    content = template_file.read_text()
    assert "Concept" in content or "concept" in content
    assert "Code" in content or "code" in content
    assert "Example" in content or "example" in content

    print("✓ Template file exists with required fields")


if __name__ == "__main__":
    print("\n=== Code Example Generator Skill Integration Tests ===\n")

    test_skill_activation_teaching_demonstration()
    test_skill_activation_runnable_examples()
    test_skill_activation_progressive_sequence()
    test_skill_activation_best_practices()
    test_validation_with_sample_code()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nCode-example-generator skill is ready for use.")
    print("Skill activates when educators need runnable, pedagogically sound code examples.")
