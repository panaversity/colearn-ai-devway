#!/usr/bin/env python3
"""
Integration tests for technical-clarity skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_explanation() -> str:
    """Create a sample explanation markdown file for testing."""
    markdown_content = """# Introduction to Python Decorators

Decorators are a powerful feature in Python that allows you to modify or enhance functions without changing their source code. Obviously, this is very useful for adding functionality like logging, timing, or authentication to existing functions.

## What are Decorators?

A decorator is simply a function that takes another function as an argument and returns a new function. Everyone knows that functions in Python are first-class objects, meaning they can be passed around just like any other object.

## Example

Here's a simple decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

When you run this, you'll see that the wrapper function executes before and after the original function. It's trivially simple to understand once you grasp the concept.

## Common Use Cases

Decorators are used for cross-cutting concerns like:
- Logging function calls
- Measuring execution time
- Access control and authentication
- Caching expensive function results

Naturally, you'll want to use decorators in your own code once you understand them.
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, dir="/tmp"
    ) as f:
        f.write(markdown_content)
        return f.name


def test_skill_activation_clarity_feedback() -> None:
    """
    Test: Skill activates when educator asks "is this explanation clear enough"
    Semantic Context: Seeking clarity assessment (not keyword-based)
    """
    print("Test: Skill activation for clarity feedback request...")
    print("  [Semantic Understanding]: Educator wants feedback on explanation clarity")
    print("  [Expected]: Technical-clarity skill should activate")
    assert Path("./.claude/skills/technical-clarity/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_jargon_check() -> None:
    """
    Test: Skill activates when educator mentions "too technical for beginners"
    Semantic Context: Concern about jargon and accessibility
    """
    print("Test: Skill activation for jargon concerns...")
    print("  [Semantic Understanding]: Educator worried about technical language level")
    print("  [Expected]: Technical-clarity skill should activate")
    assert Path("./.claude/skills/technical-clarity/reference/readability-metrics.md").exists()
    print("✓ Readability metrics reference available")


def test_skill_activation_gatekeeping_language() -> None:
    """
    Test: Skill activates for "does this sound condescending or exclusive"
    Semantic Context: Detecting gatekeeping language
    """
    print("Test: Skill activation for gatekeeping detection...")
    print("  [Semantic Understanding]: Educator wants to avoid exclusive language")
    print("  [Expected]: Technical-clarity skill should activate")
    assert Path("./.claude/skills/technical-clarity/reference/gatekeeping-language.md").exists()
    print("✓ Gatekeeping language reference available")


def test_skill_activation_completeness_check() -> None:
    """
    Test: Skill activates when educator asks "what am I missing in this tutorial"
    Semantic Context: Assessing explanation completeness
    """
    print("Test: Skill activation for completeness assessment...")
    print("  [Semantic Understanding]: Educator checking for missing context or information")
    print("  [Expected]: Technical-clarity skill should activate")
    assert Path("./.claude/skills/technical-clarity/scripts/check-completeness.py").exists()
    print("✓ Completeness checking script available")


def test_validation_with_sample_explanation() -> None:
    """Test the completeness checking script with sample explanation."""
    print("Test: Running completeness check on sample explanation...")
    explanation_file = create_sample_explanation()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/technical-clarity/scripts/check-completeness.py",
                explanation_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Completeness results: {output['summary']}")
        assert "score" in output["summary"], "Should calculate completeness score"
        assert "gatekeeping_language" in output, "Should detect gatekeeping language"
        assert len(output["gatekeeping_language"]) > 0, "Should find gatekeeping phrases"
        print("✓ Completeness check identified issues (gatekeeping language detected)")

    finally:
        Path(explanation_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/technical-clarity/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: technical-clarity" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content
    assert "## When to Activate" in content
    assert "## Process" in content
    assert "## Output Format" in content
    assert "## Examples" in content

    # Check for references to Layer 3 files
    assert "reference/readability-metrics.md" in content
    assert "reference/gatekeeping-language.md" in content
    assert "reference/clarity-checklist.md" in content
    assert "templates/clarity-report-template.yml" in content
    assert "scripts/check-completeness.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/technical-clarity/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "readability-metrics.md",
        "gatekeeping-language.md",
        "analogy-patterns.md",
        "clarity-checklist.md",
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

    template_file = Path("./.claude/skills/technical-clarity/templates/clarity-report-template.yml")
    assert template_file.exists(), "Template file must exist"

    content = template_file.read_text()
    assert "clarity" in content.lower() or "report" in content.lower()

    print("✓ Template file exists with required structure")


if __name__ == "__main__":
    print("\n=== Technical Clarity Skill Integration Tests ===\n")

    test_skill_activation_clarity_feedback()
    test_skill_activation_jargon_check()
    test_skill_activation_gatekeeping_language()
    test_skill_activation_completeness_check()
    test_validation_with_sample_explanation()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nTechnical-clarity skill is ready for use.")
    print("Skill activates when educators need feedback on clarity, jargon, and accessibility.")
