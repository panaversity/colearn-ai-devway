#!/usr/bin/env python3
"""
Readability Analyzer - Calculate readability metrics for text

This script analyzes text for readability using standard metrics:
- Flesch-Kincaid Grade Level: 0-18+ scale (lower = easier to read)
- Average Sentence Length: words per sentence
- Complex Words Ratio: percentage of words with 3+ syllables
- Vocabulary Complexity: unique words / total words

Usage:
    python readability-analyzer.py text.md

Example:
    python readability-analyzer.py explanation.md
    # Output: JSON with metrics
"""

import json
import re
import sys
from pathlib import Path
from typing import Any


def count_syllables(word: str) -> int:
    """
    Estimate syllable count for a word.

    Simple heuristic: count vowel groups, adjust for silent e, etc.
    """
    word = word.lower()
    if len(word) <= 3:
        return 1

    vowels = "aeiouy"
    syllable_count = 0
    previous_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel

    # Adjust for silent e at end
    if word.endswith("e"):
        syllable_count -= 1

    # Adjust for -le ending
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1

    return max(1, syllable_count)


def analyze_readability(text: str) -> dict[str, Any]:
    """
    Analyze text readability metrics.

    Returns dictionary with:
    - flesch_kincaid_grade: Grade level (0-18+)
    - avg_sentence_length: Average words per sentence
    - complex_words_ratio: Percentage of 3+ syllable words
    - vocabulary_diversity: Unique words / total words
    - total_words: Total word count
    - total_sentences: Total sentence count
    - total_unique_words: Unique word count
    """
    # Normalize text
    text = text.strip()

    # Extract sentences (simple heuristic: split on . ! ?)
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    if sentence_count == 0:
        return {
            "flesch_kincaid_grade": 0,
            "avg_sentence_length": 0,
            "complex_words_ratio": 0,
            "vocabulary_diversity": 0,
            "total_words": 0,
            "total_sentences": 0,
            "total_unique_words": 0,
            "error": "No sentences found in text",
        }

    # Extract words (lowercase, remove punctuation)
    words = re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)?\b", text.lower())
    word_count = len(words)

    if word_count == 0:
        return {
            "flesch_kincaid_grade": 0,
            "avg_sentence_length": 0,
            "complex_words_ratio": 0,
            "vocabulary_diversity": 0,
            "total_words": 0,
            "total_sentences": 0,
            "total_unique_words": 0,
            "error": "No words found in text",
        }

    # Calculate metrics
    unique_words = set(words)
    unique_count = len(unique_words)

    # Count complex words (3+ syllables)
    complex_word_count = sum(1 for word in words if count_syllables(word) >= 3)

    # Calculate syllable total for Flesch-Kincaid
    total_syllables = sum(count_syllables(word) for word in words)

    # Flesch-Kincaid Grade Level formula:
    # 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
    fk_grade = (
        0.39 * (word_count / sentence_count)
        + 11.8 * (total_syllables / word_count)
        - 15.59
    )

    # Ensure grade is in reasonable range
    fk_grade = max(0, min(18, fk_grade))

    return {
        "flesch_kincaid_grade": round(fk_grade, 1),
        "avg_sentence_length": round(word_count / sentence_count, 1),
        "complex_words_ratio": round(100 * complex_word_count / word_count, 1),
        "vocabulary_diversity": round(100 * unique_count / word_count, 1),
        "total_words": word_count,
        "total_sentences": sentence_count,
        "total_unique_words": unique_count,
    }


def main() -> None:
    """Parse arguments and analyze text."""
    if len(sys.argv) < 2:
        print(
            json.dumps(
                {
                    "error": "Usage: python readability-analyzer.py <text_file>",
                }
            )
        )
        sys.exit(1)

    text_file = sys.argv[1]

    # Check file exists
    if not Path(text_file).exists():
        print(json.dumps({"error": f"File not found: {text_file}"}))
        sys.exit(1)

    # Read file
    try:
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(json.dumps({"error": f"Failed to read file: {str(e)}"}))
        sys.exit(1)

    # Analyze
    result = analyze_readability(text)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
