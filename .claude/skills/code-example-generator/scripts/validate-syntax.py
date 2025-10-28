#!/usr/bin/env python3
"""
Validate Python syntax using AST parsing.

Usage: python validate-syntax.py <code_file.py>

Returns: Exit code 0 on success, 1 on failure
Outputs: JSON with syntax validation results
"""

import ast
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def validate_syntax(code: str, filename: str = "<string>") -> Dict[str, Any]:
    """
    Validate Python syntax by parsing code into AST.

    Args:
        code: Python source code to validate
        filename: Name to use in error messages

    Returns:
        Dictionary with validation results and any errors
    """
    result = {
        "valid": False,
        "errors": [],
        "warnings": [],
        "stats": {}
    }

    if not code.strip():
        result["errors"].append("Code is empty")
        return result

    try:
        # Parse code into Abstract Syntax Tree
        tree = ast.parse(code, filename=filename)
        result["valid"] = True

        # Collect statistics about the code
        result["stats"] = {
            "num_functions": sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)),
            "num_classes": sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef)),
            "num_imports": sum(1 for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))),
            "num_lines": len(code.splitlines())
        }

        # Check for common issues
        warnings = check_common_issues(tree, code)
        result["warnings"] = warnings

    except SyntaxError as e:
        result["errors"].append({
            "type": "SyntaxError",
            "message": str(e.msg),
            "line": e.lineno,
            "offset": e.offset,
            "text": e.text.strip() if e.text else None
        })
    except Exception as e:
        result["errors"].append({
            "type": type(e).__name__,
            "message": str(e)
        })

    return result


def check_common_issues(tree: ast.AST, code: str) -> List[str]:
    """
    Check for common pedagogical and style issues.

    Args:
        tree: AST of the code
        code: Original source code

    Returns:
        List of warning messages
    """
    warnings = []

    # Check for too many functions/classes (overwhelming for teaching)
    num_functions = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    num_classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))

    if num_functions > 5:
        warnings.append(f"Many functions ({num_functions}) - consider breaking into multiple examples")

    if num_classes > 3:
        warnings.append(f"Many classes ({num_classes}) - may be too complex for a single example")

    # Check for undefined names (common mistake)
    try:
        compile(code, '<string>', 'exec')
    except NameError as e:
        warnings.append(f"Potential undefined name: {e}")

    # Check for very long lines (readability)
    lines = code.splitlines()
    for i, line in enumerate(lines, 1):
        if len(line) > 100:
            warnings.append(f"Line {i} is very long ({len(line)} chars) - consider breaking it")

    # Check for missing docstrings in functions/classes
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                name = node.name
                node_type = "Function" if isinstance(node, ast.FunctionDef) else "Class"
                warnings.append(f"{node_type} '{name}' missing docstring")

    # Check for use of print without f-strings (style suggestion)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == 'print':
                # Check if any args are string concatenation
                for arg in node.args:
                    if isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Add):
                        if any(isinstance(operand, ast.Str) for operand in ast.walk(arg)):
                            warnings.append("Consider using f-strings instead of string concatenation")
                            break

    return warnings


def main():
    """Main entry point for syntax validation."""
    if len(sys.argv) != 2:
        print("Usage: python validate-syntax.py <code_file.py>", file=sys.stderr)
        sys.exit(1)

    code_file = Path(sys.argv[1])

    if not code_file.exists():
        print(f"Error: File not found: {code_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(code_file, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    result = validate_syntax(code, filename=str(code_file))
    print(json.dumps(result, indent=2))

    if result["valid"]:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
