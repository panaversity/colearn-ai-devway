#!/usr/bin/env python3
"""
Check completeness of technical explanations.

Usage: python check-completeness.py <explanation.md>

Returns: Exit code 0 on success, 1 on failure
Outputs: JSON with completeness analysis
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List


def check_completeness(text: str, filename: str = "") -> Dict[str, Any]:
    """
    Analyze technical explanation for completeness.

    Args:
        text: Explanation text to analyze
        filename: Name of file being analyzed

    Returns:
        Dictionary with completeness assessment
    """
    result = {
        "success": True,
        "filename": filename,
        "completeness_score": 0,  # 0-100
        "missing_elements": [],
        "warnings": [],
        "statistics": {}
    }

    # Basic statistics
    lines = text.split('\n')
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    words = text.split()

    result["statistics"] = {
        "line_count": len(lines),
        "paragraph_count": len(paragraphs),
        "word_count": len(words),
        "has_code_blocks": '```' in text
    }

    score = 100
    missing = []
    warnings = []

    # Check 1: Prerequisites mentioned
    has_prerequisites = any(
        keyword in text.lower()
        for keyword in ['prerequisite', 'before reading', 'assumes', 'requires understanding']
    )
    if not has_prerequisites:
        missing.append({
            "element": "Prerequisites",
            "severity": "moderate",
            "description": "No prerequisites or assumed knowledge stated",
            "recommendation": "Add a section listing what readers should know first"
        })
        score -= 15

    # Check 2: Examples provided
    code_block_count = text.count('```')
    has_examples = code_block_count >= 2  # At least one code block pair

    if not has_examples:
        missing.append({
            "element": "Code Examples",
            "severity": "critical",
            "description": "No code examples found",
            "recommendation": "Add concrete code examples demonstrating concepts"
        })
        score -= 25
    elif code_block_count < 4:
        warnings.append("Limited examples (consider adding more)")
        score -= 5

    # Check 3: Definitions for technical terms
    # Look for patterns like "X is", "X means", "X (definition)"
    definition_patterns = [
        r'\w+ is (?:a|an|the)',
        r'\w+ means',
        r'\w+ \([^)]+\)',  # Term (definition)
    ]

    definition_count = sum(
        len(re.findall(pattern, text, re.IGNORECASE))
        for pattern in definition_patterns
    )

    if definition_count < 2:
        missing.append({
            "element": "Term Definitions",
            "severity": "moderate",
            "description": "Few or no term definitions found",
            "recommendation": "Define technical terms explicitly"
        })
        score -= 10

    # Check 4: Context/motivation (why)
    has_why = any(
        keyword in text.lower()
        for keyword in ['because', 'reason', 'why', 'purpose', 'benefit']
    )
    if not has_why:
        missing.append({
            "element": "Context/Motivation",
            "severity": "moderate",
            "description": "No explanation of 'why' (purpose/benefits)",
            "recommendation": "Explain why concepts matter or when to use them"
        })
        score -= 15

    # Check 5: Expected output shown
    has_output = any(
        keyword in text.lower()
        for keyword in ['output:', 'result:', 'produces:', 'returns:', '# output', '# result']
    )
    if has_examples and not has_output:
        warnings.append("Code examples present but expected output not shown")
        score -= 10

    # Check 6: Error cases or common mistakes
    has_errors = any(
        keyword in text.lower()
        for keyword in ['error', 'mistake', 'common pitfall', 'gotcha', 'warning', 'note:']
    )
    if not has_errors:
        warnings.append("No mention of common mistakes or error cases")
        score -= 5

    # Check 7: Structure (headings)
    heading_count = len(re.findall(r'^#{1,6} ', text, re.MULTILINE))
    if heading_count < 2:
        missing.append({
            "element": "Document Structure",
            "severity": "minor",
            "description": "Few or no section headings",
            "recommendation": "Add headings to organize content"
        })
        score -= 5

    # Check 8: Paragraph length (readability)
    long_paragraphs = sum(1 for p in paragraphs if len(p.split()) > 150)
    if long_paragraphs > 0:
        warnings.append(f"{long_paragraphs} very long paragraph(s) - consider breaking up")

    # Check 9: Very short content
    if len(words) < 50:
        missing.append({
            "element": "Content Depth",
            "severity": "critical",
            "description": "Explanation is very brief (<50 words)",
            "recommendation": "Expand with more detail, examples, and context"
        })
        score -= 20

    result["completeness_score"] = max(0, score)
    result["missing_elements"] = missing
    result["warnings"] = warnings

    return result


def main():
    """Main entry point for completeness checking."""
    if len(sys.argv) != 2:
        print("Usage: python check-completeness.py <explanation.md>", file=sys.stderr)
        sys.exit(1)

    text_file = Path(sys.argv[1])

    if not text_file.exists():
        print(f"Error: File not found: {text_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        result = check_completeness(text, filename=str(text_file))
        print(json.dumps(result, indent=2))

        # Exit with warning if completeness score is low
        if result["completeness_score"] < 60:
            sys.exit(1)

        sys.exit(0)
    except Exception as e:
        error_result = {
            "success": False,
            "error": str(e)
        }
        print(json.dumps(error_result, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
