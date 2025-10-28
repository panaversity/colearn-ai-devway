#!/usr/bin/env python3
"""Unit tests for validate-objectives.py"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def test_valid_objective() -> None:
    """Test validation of a properly written objective."""
    yaml_content = """objectives:
  - id: "LO-001"
    statement: "Implement a list comprehension to filter data"
    blooms_level: "Apply"
    context: "Given a list of dictionaries"
    assessment_method: "Code exercise"
    success_criteria:
      - "Code executes without errors"
      - "Output matches expected results"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(yaml_content)
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/learning-objectives/scripts/validate-objectives.py",
                temp_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["summary"]["valid"] >= 1, "Should validate well-written objective"
        print("✓ test_valid_objective passed")

    finally:
        Path(temp_file).unlink()


def test_vague_language_detection() -> None:
    """Test detection of vague language."""
    yaml_content = """objectives:
  - id: "LO-001"
    statement: "Understand list comprehensions"
    blooms_level: "Apply"
    context: "In data processing"
    assessment_method: "Quiz"
    success_criteria:
      - "Can answer questions"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(yaml_content)
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/learning-objectives/scripts/validate-objectives.py",
                temp_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        # Should find vague language error
        obj_errors = output["objectives"][0]["errors"]
        assert any(
            "vague" in error.lower() for error in obj_errors
        ), "Should detect vague language"
        print("✓ test_vague_language_detection passed")

    finally:
        Path(temp_file).unlink()


def test_missing_context() -> None:
    """Test detection of missing context."""
    yaml_content = """objectives:
  - id: "LO-001"
    statement: "Implement a function to sort data"
    blooms_level: "Apply"
    assessment_method: "Code exercise"
    success_criteria:
      - "Code works"
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(yaml_content)
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/learning-objectives/scripts/validate-objectives.py",
                temp_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        obj_errors = output["objectives"][0]["errors"]
        assert any(
            "context" in error.lower() for error in obj_errors
        ), "Should detect missing context"
        print("✓ test_missing_context passed")

    finally:
        Path(temp_file).unlink()


def test_file_not_found() -> None:
    """Test handling of non-existent file."""
    result = subprocess.run(
        [
            sys.executable,
            "./.claude/skills/learning-objectives/scripts/validate-objectives.py",
            "nonexistent.yml",
        ],
        capture_output=True,
        text=True,
    )

    output = json.loads(result.stdout)
    assert output["valid"] is False, "Should fail for missing file"
    assert "not found" in output["error"].lower(), "Should indicate file not found"
    print("✓ test_file_not_found passed")


if __name__ == "__main__":
    test_valid_objective()
    test_vague_language_detection()
    test_missing_context()
    test_file_not_found()
    print("\nAll objective validation tests passed! ✓")
