#!/usr/bin/env python3
"""Unit tests for readability-analyzer and yaml-validator scripts."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def test_readability_analyzer_simple_text() -> None:
    """Test readability analyzer with simple text."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("The cat sat. The cat ran. The cat slept.")
        temp_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, "./.claude/skills/_shared/readability-analyzer.py", temp_file],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert "flesch_kincaid_grade" in output, "Should include grade level"
        assert output["total_words"] == 9, "Should count words correctly"
        assert output["total_sentences"] == 3, "Should count sentences correctly"
        assert 0 <= output["flesch_kincaid_grade"] <= 18, "Grade should be in valid range"
        print("✓ test_readability_analyzer_simple_text passed")

    finally:
        Path(temp_file).unlink()


def test_readability_analyzer_complex_text() -> None:
    """Test readability analyzer with complex text."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(
            "Understanding object-oriented programming fundamentals requires comprehension of encapsulation principles. "
            "Polymorphism provides extensible implementations. Abstraction simplifies complexity."
        )
        temp_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, "./.claude/skills/_shared/readability-analyzer.py", temp_file],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["flesch_kincaid_grade"] > 10, "Should show higher complexity"
        assert output["complex_words_ratio"] > 30, "Should have high complexity word ratio"
        print("✓ test_readability_analyzer_complex_text passed")

    finally:
        Path(temp_file).unlink()


def test_readability_analyzer_empty_file() -> None:
    """Test readability analyzer with empty file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("")
        temp_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, "./.claude/skills/_shared/readability-analyzer.py", temp_file],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert "error" in output, "Should indicate error for empty file"
        print("✓ test_readability_analyzer_empty_file passed")

    finally:
        Path(temp_file).unlink()


def test_yaml_validator_file_not_found() -> None:
    """Test yaml-validator with missing files."""
    result = subprocess.run(
        [
            sys.executable,
            "./.claude/skills/_shared/yaml-validator.py",
            "nonexistent.yml",
            "nonexistent.yml",
        ],
        capture_output=True,
        text=True,
    )

    output = json.loads(result.stdout)
    assert output["valid"] is False, "Should fail validation"
    assert len(output["errors"]) > 0, "Should report errors"
    print("✓ test_yaml_validator_file_not_found passed")


def test_yaml_validator_missing_required_field() -> None:
    """Test yaml-validator detects missing required fields."""
    # Create schema file
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as schema_f:
        schema_f.write("required:\n  - name\n  - description\n")
        schema_file = schema_f.name

    # Create data file with missing field
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, dir="/tmp"
    ) as data_f:
        data_f.write("name: Test\n")
        data_file = data_f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/_shared/yaml-validator.py",
                schema_file,
                data_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["valid"] is False, "Should fail validation"
        assert any(
            "description" in error for error in output["errors"]
        ), "Should report missing field"
        print("✓ test_yaml_validator_missing_required_field passed")

    finally:
        Path(schema_file).unlink()
        Path(data_file).unlink()


if __name__ == "__main__":
    test_readability_analyzer_simple_text()
    test_readability_analyzer_complex_text()
    test_readability_analyzer_empty_file()
    test_yaml_validator_file_not_found()
    test_yaml_validator_missing_required_field()
    print("\nAll shared script tests passed! ✓")
