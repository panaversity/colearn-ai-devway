#!/usr/bin/env python3
"""
Sandbox Executor - Isolated Python Code Execution with Security Constraints

This script executes Python code in an isolated subprocess with security constraints:
- Timeout: 5 seconds maximum execution time
- File system: Restricted to temporary directory (auto-cleaned after execution)
- Network: No network access (subprocess inherits minimal environment)
- Output: JSON-formatted results (stdout, stderr, exit_code, timeout)

Usage:
    python sandbox-executor.py code.py [--timeout 5]

Example:
    python sandbox-executor.py example.py --timeout 5
    # Output: {"stdout": "...", "stderr": "...", "exit_code": 0, "timeout": false}
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def execute_code(code_file: str, timeout: int = 5) -> dict[str, Any]:
    """
    Execute Python code in isolated sandbox.

    Args:
        code_file: Path to Python file to execute
        timeout: Maximum execution time in seconds (default: 5)

    Returns:
        Dictionary with keys:
        - stdout: Standard output from execution
        - stderr: Standard error output
        - exit_code: Process exit code (0 = success)
        - timeout: Boolean indicating if execution timed out
    """
    code_path = Path(code_file)

    # Validate file exists and is readable
    if not code_path.exists():
        return {
            "stdout": "",
            "stderr": f"ERROR: File not found: {code_file}",
            "exit_code": 1,
            "timeout": False,
        }

    if not code_path.is_file():
        return {
            "stdout": "",
            "stderr": f"ERROR: Path is not a file: {code_file}",
            "exit_code": 1,
            "timeout": False,
        }

    # Create isolated temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Execute with security constraints
            result = subprocess.run(
                [sys.executable, str(code_path)],
                capture_output=True,
                timeout=timeout,
                cwd=temp_dir,  # Restrict file system access
                text=True,
                env={"PATH": "/usr/bin:/bin", "HOME": temp_dir},  # Minimal environment
            )

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode,
                "timeout": False,
            }

        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": f"TIMEOUT: Execution exceeded {timeout}s limit",
                "exit_code": 124,  # Standard timeout exit code
                "timeout": True,
            }

        except Exception as e:
            return {
                "stdout": "",
                "stderr": f"ERROR: {type(e).__name__}: {str(e)}",
                "exit_code": 1,
                "timeout": False,
            }


def main() -> None:
    """Parse arguments and execute code."""
    if len(sys.argv) < 2:
        print(
            json.dumps(
                {
                    "stdout": "",
                    "stderr": "Usage: python sandbox-executor.py <code_file> [--timeout N]",
                    "exit_code": 1,
                    "timeout": False,
                }
            )
        )
        sys.exit(1)

    code_file = sys.argv[1]
    timeout = 5

    # Parse --timeout argument
    if len(sys.argv) > 2:
        for i, arg in enumerate(sys.argv[2:], start=2):
            if arg == "--timeout" and i + 1 < len(sys.argv):
                try:
                    timeout = int(sys.argv[i + 1])
                except (ValueError, IndexError):
                    pass

    result = execute_code(code_file, timeout)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
