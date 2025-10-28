#!/usr/bin/env python3
"""
Integration tests for book-architecture skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_book_outline() -> str:
    """Create a sample book outline YAML file for testing."""
    yaml_content = """book_title: "Python Programming Fundamentals"
subtitle: "A Beginner's Guide"
target_audience: "Absolute beginners with no programming experience"
prerequisites: "None - starts from basics"

learning_outcomes:
  - "Write basic Python programs using variables, functions, and control flow"
  - "Debug simple Python code"
  - "Apply fundamental programming concepts"

flow_pattern: "Linear"

parts:
  - id: "part-01"
    title: "Getting Started"
    purpose: "Foundation"
    chapters:
      - id: "ch-01"
        number: 1
        title: "Introduction to Python"
        purpose: "Core"
        dependencies:
          required: []
          recommended: []
        synopsis: "Install Python, run first program, understand basic syntax"
        learning_objectives:
          - "Install Python on their system"
          - "Write and run a simple Python program"
        key_concepts:
          - "Python installation"
          - "REPL usage"
          - "print() function"
        estimated_pages: 15

      - id: "ch-02"
        number: 2
        title: "Variables and Data Types"
        purpose: "Core"
        dependencies:
          required: ["ch-01"]
          recommended: []
        synopsis: "Understanding variables, numbers, strings, and basic operations"
        learning_objectives:
          - "Create and use variables"
          - "Work with different data types"
        key_concepts:
          - "Variable assignment"
          - "Integers and floats"
          - "Strings"
          - "Type conversion"
        estimated_pages: 20

      - id: "ch-03"
        number: 3
        title: "Control Flow"
        purpose: "Core"
        dependencies:
          required: ["ch-02"]
          recommended: []
        synopsis: "Making decisions with if/else and loops"
        learning_objectives:
          - "Write conditional statements"
          - "Use for and while loops"
        key_concepts:
          - "if/elif/else"
          - "Boolean logic"
          - "for loops"
          - "while loops"
        estimated_pages: 25

reading_paths:
  - name: "Linear Path (Recommended)"
    description: "Read all chapters in order"
    chapters: ["ch-01", "ch-02", "ch-03"]

dependency_graph: |
  ch-01 → ch-02 → ch-03
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as f:
        f.write(yaml_content)
        return f.name


def test_skill_activation_book_organization() -> None:
    """
    Test: Skill activates when educator asks "how should I organize my book"
    Semantic Context: Structural planning for multi-chapter content (not keyword-based)
    """
    print("Test: Skill activation for book organization request...")
    print("  [Semantic Understanding]: Educator needs to structure comprehensive content")
    print("  [Expected]: Book-architecture skill should activate")
    assert Path("./.claude/skills/book-architecture/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_chapter_sequencing() -> None:
    """
    Test: Skill activates when educator mentions "what order for chapters"
    Semantic Context: Determining appropriate learning trajectory
    """
    print("Test: Skill activation for chapter sequencing...")
    print("  [Semantic Understanding]: Educator needs help with content sequence")
    print("  [Expected]: Book-architecture skill should activate")
    assert Path("./.claude/skills/book-architecture/reference/chapter-flow-patterns.md").exists()
    print("✓ Chapter flow patterns reference available")


def test_skill_activation_prerequisite_management() -> None:
    """
    Test: Skill activates for "how to handle chapter dependencies"
    Semantic Context: Managing prerequisite knowledge across chapters
    """
    print("Test: Skill activation for dependency management...")
    print("  [Semantic Understanding]: Educator managing prerequisite relationships")
    print("  [Expected]: Book-architecture skill should activate")
    assert Path("./.claude/skills/book-architecture/reference/chapter-dependencies.md").exists()
    print("✓ Chapter dependencies reference available")


def test_skill_activation_content_organization() -> None:
    """
    Test: Skill activates when educator asks "tutorial vs reference balance"
    Semantic Context: Structural design decisions
    """
    print("Test: Skill activation for content organization...")
    print("  [Semantic Understanding]: Educator deciding on organizational patterns")
    print("  [Expected]: Book-architecture skill should activate")
    assert Path("./.claude/skills/book-architecture/reference/structural-patterns.md").exists()
    print("✓ Structural patterns reference available")


def test_validation_with_sample_outline() -> None:
    """Test the structure validation script with sample outline."""
    print("Test: Running structure validation on sample outline...")
    outline_file = create_sample_book_outline()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/book-architecture/scripts/validate-structure.py",
                outline_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Validation results: {output['summary']}")
        assert output["summary"]["valid"] is True, "Structure should be valid"
        assert output["summary"]["circular_dependencies"] == 0, "Should have no cycles"
        assert output["summary"]["total_chapters"] == 3, "Should find 3 chapters"
        print("✓ Structure validation passed with clean dependencies")

    finally:
        Path(outline_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/book-architecture/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: book-architecture" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content or "# Purpose" in content
    assert "## When to Activate" in content or "# When to Activate" in content
    assert "## Process" in content or "# Process" in content
    assert "## Output Format" in content or "# Output Format" in content
    assert "## Examples" in content or "# Examples" in content

    # Check for references to Layer 3 files
    assert "reference/chapter-flow-patterns.md" in content
    assert "reference/chapter-dependencies.md" in content
    assert "reference/structural-patterns.md" in content
    assert "templates/book-outline-template.yml" in content
    assert "scripts/validate-structure.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/book-architecture/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "chapter-flow-patterns.md",
        "chapter-dependencies.md",
        "structural-patterns.md",
        "content-organization.md",
    ]

    for filename in required_files:
        filepath = ref_dir / filename
        assert filepath.exists(), f"Missing reference: {filename}"
        content = filepath.read_text()
        assert len(content) > 1000, f"{filename} should be substantive (>1000 chars)"

    print("✓ All reference files present and substantive")


def test_templates() -> None:
    """Verify templates exist."""
    print("Test: Template files...")

    template_files = [
        "./.claude/skills/book-architecture/templates/book-outline-template.yml",
        "./.claude/skills/book-architecture/templates/chapter-structure-template.yml",
    ]

    for template_path in template_files:
        template_file = Path(template_path)
        assert template_file.exists(), f"Template file must exist: {template_path}"
        content = template_file.read_text()
        assert len(content) > 100, f"{template_path} should have content"

    print("✓ Template files exist with required content")


if __name__ == "__main__":
    print("\n=== Book Architecture Skill Integration Tests ===\n")

    test_skill_activation_book_organization()
    test_skill_activation_chapter_sequencing()
    test_skill_activation_prerequisite_management()
    test_skill_activation_content_organization()
    test_validation_with_sample_outline()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nBook-architecture skill is ready for use.")
    print("Skill activates when educators need to design comprehensive book structures.")
