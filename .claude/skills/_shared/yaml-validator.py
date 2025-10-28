#!/usr/bin/env python3
"""
YAML Validator - Validate YAML files against JSON Schema

This script validates YAML data files against schema files using basic JSON schema
validation patterns. For complex validation, integrates with external validators.

Usage:
    python yaml-validator.py schema.yml data.yml

Example:
    python yaml-validator.py learning-objective.schema.yml objectives.yml
    # Output: {"valid": true, "errors": []}
"""

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


def load_yaml(file_path: str) -> dict[str, Any] | None:
    """Load YAML file."""
    if yaml is None:
        return None

    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def validate_against_schema(
    schema: dict[str, Any], data: dict[str, Any]
) -> tuple[bool, list[str]]:
    """
    Validate data against schema using basic checks.

    This is a simplified validator. For production use, consider jsonschema library.
    """
    errors: list[str] = []

    # Check required fields
    if "required" in schema:
        for field in schema["required"]:
            if field not in data:
                errors.append(f"Missing required field: {field}")

    # Check field types (basic validation)
    if "properties" in schema:
        for field, field_schema in schema["properties"].items():
            if field in data:
                expected_type = field_schema.get("type", "any")
                value = data[field]

                # Basic type checking
                if expected_type == "string" and not isinstance(value, str):
                    errors.append(
                        f"Field '{field}': expected string, got {type(value).__name__}"
                    )
                elif expected_type == "integer" and not isinstance(value, int):
                    errors.append(
                        f"Field '{field}': expected integer, got {type(value).__name__}"
                    )
                elif expected_type == "array" and not isinstance(value, list):
                    errors.append(
                        f"Field '{field}': expected array, got {type(value).__name__}"
                    )
                elif expected_type == "object" and not isinstance(value, dict):
                    errors.append(
                        f"Field '{field}': expected object, got {type(value).__name__}"
                    )

    return len(errors) == 0, errors


def main() -> None:
    """Parse arguments and validate YAML."""
    if len(sys.argv) < 3:
        print(
            json.dumps(
                {
                    "valid": False,
                    "errors": ["Usage: python yaml-validator.py <schema.yml> <data.yml>"],
                }
            )
        )
        sys.exit(1)

    schema_file = sys.argv[1]
    data_file = sys.argv[2]

    # Check files exist
    if not Path(schema_file).exists():
        print(
            json.dumps(
                {
                    "valid": False,
                    "errors": [f"Schema file not found: {schema_file}"],
                }
            )
        )
        sys.exit(1)

    if not Path(data_file).exists():
        print(
            json.dumps(
                {
                    "valid": False,
                    "errors": [f"Data file not found: {data_file}"],
                }
            )
        )
        sys.exit(1)

    # Load YAML files
    schema = load_yaml(schema_file)
    data = load_yaml(data_file)

    if schema is None:
        print(
            json.dumps(
                {
                    "valid": False,
                    "errors": [f"Failed to parse schema file: {schema_file}"],
                }
            )
        )
        sys.exit(1)

    if data is None:
        print(
            json.dumps(
                {
                    "valid": False,
                    "errors": [f"Failed to parse data file: {data_file}"],
                }
            )
        )
        sys.exit(1)

    # Validate
    is_valid, errors = validate_against_schema(schema, data)

    print(json.dumps({"valid": is_valid, "errors": errors}))
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
