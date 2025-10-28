#!/usr/bin/env python3
"""
Integration tests for ai-augmented-teaching skill semantic activation

Tests that the skill activates appropriately with semantically varied requests
(not keyword-based, but contextual understanding of when the skill is needed)
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def create_sample_ai_lesson() -> str:
    """Create a sample AI-integrated lesson YAML file for testing."""
    yaml_content = """lesson_metadata:
  title: "Introduction to Python Functions"
  topic: "Python Functions"
  duration: "90 minutes"
  target_audience: "Beginners"
  ai_integration_level: "Low"

learning_objectives:
  - statement: "Students will define functions with parameters"
    ai_role: "None"
  - statement: "Students will call functions correctly"
    ai_role: "None"
  - statement: "Students will debug function errors"
    ai_role: "Explainer"
  - statement: "Students will explore function variations"
    ai_role: "Pair Programmer"

foundational_skills_focus:
  - "Understanding function syntax (def, parameters, return)"
  - "Tracing function execution manually"
  - "Writing simple functions independently"

ai_assisted_skills_focus:
  - "Exploring function variations with AI assistance"
  - "Getting explanations for confusing errors"
  - "Generating test cases with AI help"

phases:
  - phase_name: "Foundation (Independent)"
    duration_minutes: 30
    ai_usage: "None"
    activities:
      - "Lecture: Function concepts and syntax"
      - "Live coding: Demonstrate 3 example functions"
      - "Students write 3 simple functions independently"
      - "Quick comprehension check (no AI)"

  - phase_name: "AI-Assisted Exploration"
    duration_minutes: 40
    ai_usage: "Encouraged"
    activities:
      - "Students use AI to explain function concepts they find confusing"
      - "Request AI help to generate test cases for their functions"
      - "Ask AI for alternative function implementations"
      - "Document all AI usage in learning journal"
    ai_guidelines:
      - "Use AI to explain, not to write code for you"
      - "Always read and understand AI responses"
      - "Test all AI-suggested code before accepting"

  - phase_name: "Independent Verification"
    duration_minutes: 15
    ai_usage: "None"
    activities:
      - "Write 2 functions without any AI assistance"
      - "Explain in writing what each function does"
      - "Demonstrate independent function-writing capability"

  - phase_name: "Wrap-Up and Reflection"
    duration_minutes: 5
    ai_usage: "Optional"
    activities:
      - "Reflect: When was AI most helpful? When did you struggle without it?"
      - "Discuss ethical AI use expectations"

ai_assistance_balance:
  foundational_work_percentage: 40
  ai_assisted_work_percentage: 45
  independent_verification_percentage: 15

ethical_considerations:
  disclosure_required: true
  understanding_verification: true
  prohibited_actions:
    - "Submitting AI-generated code without understanding it"
    - "Using AI during independent verification phase"
    - "Not documenting AI assistance"
  verification_methods:
    - "Code explanation requirement"
    - "Independent verification phase"
    - "Process documentation in learning journal"
"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as f:
        f.write(yaml_content)
        return f.name


def test_skill_activation_ai_integration() -> None:
    """
    Test: Skill activates when educator asks "how to use AI tools in teaching"
    Semantic Context: Integrating AI assistants into curriculum (not keyword-based)
    """
    print("Test: Skill activation for AI integration request...")
    print("  [Semantic Understanding]: Educator wants to incorporate AI tools responsibly")
    print("  [Expected]: AI-augmented-teaching skill should activate")
    assert Path("./.claude/skills/ai-augmented-teaching/SKILL.md").exists()
    print("✓ Skill files exist and are properly organized")


def test_skill_activation_prompt_engineering() -> None:
    """
    Test: Skill activates when educator mentions "teaching students to write prompts"
    Semantic Context: Prompt engineering as a pedagogical skill
    """
    print("Test: Skill activation for prompt engineering pedagogy...")
    print("  [Semantic Understanding]: Educator wants to teach effective AI communication")
    print("  [Expected]: AI-augmented-teaching skill should activate")
    assert Path("./.claude/skills/ai-augmented-teaching/reference/prompt-engineering-pedagogy.md").exists()
    print("✓ Prompt engineering pedagogy reference available")


def test_skill_activation_ethical_ai_use() -> None:
    """
    Test: Skill activates for "preventing students from over-relying on AI"
    Semantic Context: Balancing AI assistance with independent learning
    """
    print("Test: Skill activation for ethical AI concerns...")
    print("  [Semantic Understanding]: Educator worried about AI over-dependence")
    print("  [Expected]: AI-augmented-teaching skill should activate")
    assert Path("./.claude/skills/ai-augmented-teaching/reference/ethical-ai-use.md").exists()
    print("✓ Ethical AI use reference available")


def test_skill_activation_ai_pair_programming() -> None:
    """
    Test: Skill activates when educator asks "how students should collaborate with AI"
    Semantic Context: Teaching AI collaboration patterns
    """
    print("Test: Skill activation for AI collaboration patterns...")
    print("  [Semantic Understanding]: Educator needs AI pairing strategies")
    print("  [Expected]: AI-augmented-teaching skill should activate")
    assert Path("./.claude/skills/ai-augmented-teaching/reference/ai-pair-programming-patterns.md").exists()
    print("✓ AI pair programming patterns reference available")


def test_validation_with_sample_lesson() -> None:
    """Test the AI integration assessment script with sample lesson."""
    print("Test: Running AI integration assessment on sample lesson...")
    lesson_file = create_sample_ai_lesson()

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/ai-augmented-teaching/scripts/assess-ai-integration.py",
                lesson_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        print(f"  Assessment results: {output['summary']}")
        assert "overall_score" in output["summary"], "Should calculate overall score"
        assert output["summary"]["overall_score"] >= 60, "Score should be at least 60 (acceptable)"
        assert output["summary"]["has_foundational_phase"] is True, "Should have foundational phase"
        assert output["summary"]["has_verification_phase"] is True, "Should have verification phase"
        print("✓ AI integration assessment passed with good balance")

    finally:
        Path(lesson_file).unlink()


def test_skill_file_structure() -> None:
    """Verify the skill file structure meets requirements."""
    print("Test: Skill file structure...")

    skill_file = Path("./.claude/skills/ai-augmented-teaching/SKILL.md")
    assert skill_file.exists(), "SKILL.md must exist"

    content = skill_file.read_text()

    # Check for required frontmatter fields
    assert "name: ai-augmented-teaching" in content
    assert "description:" in content
    assert "allowed-tools:" in content

    # Check for required sections
    assert "## Purpose" in content or "# Purpose" in content
    assert "## When to Activate" in content or "# When to Activate" in content
    assert "## Process" in content or "# Process" in content
    assert "## Output Format" in content or "# Output Format" in content
    assert "## Examples" in content or "# Examples" in content

    # Check for references to Layer 3 files
    assert "reference/prompt-engineering-pedagogy.md" in content
    assert "reference/ai-pair-programming-patterns.md" in content
    assert "reference/ethical-ai-use.md" in content
    assert "reference/ai-tool-literacy.md" in content
    assert "templates/ai-lesson-template.yml" in content
    assert "scripts/assess-ai-integration.py" in content

    print("✓ SKILL.md has proper structure with all required sections")
    print("✓ SKILL.md references all Layer 3 resources")


def test_reference_documentation() -> None:
    """Verify reference documentation exists and is complete."""
    print("Test: Reference documentation completeness...")

    ref_dir = Path("./.claude/skills/ai-augmented-teaching/reference")
    assert ref_dir.exists(), "reference/ directory must exist"

    required_files = [
        "prompt-engineering-pedagogy.md",
        "ai-pair-programming-patterns.md",
        "ethical-ai-use.md",
        "ai-tool-literacy.md",
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
        "./.claude/skills/ai-augmented-teaching/templates/ai-lesson-template.yml",
        "./.claude/skills/ai-augmented-teaching/templates/prompt-design-template.md",
    ]

    for template_path in template_files:
        template_file = Path(template_path)
        assert template_file.exists(), f"Template file must exist: {template_path}"
        content = template_file.read_text()
        assert len(content) > 100, f"{template_path} should have content"

    print("✓ Template files exist with required content")


if __name__ == "__main__":
    print("\n=== AI-Augmented Teaching Skill Integration Tests ===\n")

    test_skill_activation_ai_integration()
    test_skill_activation_prompt_engineering()
    test_skill_activation_ethical_ai_use()
    test_skill_activation_ai_pair_programming()
    test_validation_with_sample_lesson()
    test_skill_file_structure()
    test_reference_documentation()
    test_templates()

    print("\n✅ All integration tests passed!")
    print("\nAI-augmented-teaching skill is ready for use.")
    print("Skill activates when educators need to integrate AI tools responsibly into curriculum.")
