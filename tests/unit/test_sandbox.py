#!/usr/bin/env python3
"""Unit tests for sandbox-executor.py"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def test_successful_execution() -> None:
    """Test successful Python code execution."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write('print("Hello, World!")')
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/_shared/sandbox-executor.py",
                temp_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["exit_code"] == 0, "Should succeed with exit code 0"
        assert "Hello, World!" in output["stdout"], "Should capture stdout"
        assert output["timeout"] is False, "Should not timeout"
        print("✓ test_successful_execution passed")

    finally:
        Path(temp_file).unlink()


def test_file_not_found() -> None:
    """Test handling of non-existent file."""
    result = subprocess.run(
        [sys.executable, "./.claude/skills/_shared/sandbox-executor.py", "nonexistent.py"],
        capture_output=True,
        text=True,
    )

    output = json.loads(result.stdout)
    assert output["exit_code"] == 1, "Should fail with exit code 1"
    assert "not found" in output["stderr"].lower(), "Should indicate file not found"
    print("✓ test_file_not_found passed")


def test_code_with_error() -> None:
    """Test code that raises an exception."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("raise ValueError('Test error')")
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/_shared/sandbox-executor.py",
                temp_file,
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["exit_code"] != 0, "Should fail"
        assert "ValueError" in output["stderr"], "Should capture error message"
        print("✓ test_code_with_error passed")

    finally:
        Path(temp_file).unlink()


def test_timeout_execution() -> None:
    """Test execution timeout."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("import time; time.sleep(10)")
        temp_file = f.name

    try:
        result = subprocess.run(
            [
                sys.executable,
                "./.claude/skills/_shared/sandbox-executor.py",
                temp_file,
                "--timeout",
                "1",
            ],
            capture_output=True,
            text=True,
        )

        output = json.loads(result.stdout)
        assert output["timeout"] is True, "Should indicate timeout"
        assert output["exit_code"] == 124, "Should use timeout exit code"
        print("✓ test_timeout_execution passed")

    finally:
        Path(temp_file).unlink()


if __name__ == "__main__":
    test_successful_execution()
    test_file_not_found()
    test_code_with_error()
    test_timeout_execution()
    print("\nAll tests passed! ✓")
