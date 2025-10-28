#!/usr/bin/env python3
"""
Assess cognitive load in a scaffolding plan.

Usage: python assess-cognitive-load.py <scaffolding_plan.yml>

Returns: Exit code 0 on success, 1 on failure
Outputs: JSON with cognitive load assessment and warnings
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import yaml


def assess_step_load(step: Dict[str, Any], audience: str) -> Dict[str, Any]:
    """
    Calculate cognitive load for a single scaffolding step.

    Args:
        step: Step data from scaffolding plan
        audience: Target audience level (beginner/intermediate/advanced)

    Returns:
        Dictionary with load assessment and warnings
    """
    warnings = []
    new_concepts = step.get("new_concepts", [])
    num_concepts = len(new_concepts)

    # Define max concepts by audience level
    max_concepts = {
        "beginner": 2,
        "intermediate": 3,
        "advanced": 4
    }

    max_allowed = max_concepts.get(audience, 2)

    # Check concept count
    if num_concepts > max_allowed:
        warnings.append(
            f"Step {step.get('step_number')} introduces {num_concepts} concepts "
            f"(max recommended: {max_allowed} for {audience})"
        )

    # Check prerequisites
    prerequisites = step.get("prerequisites", [])
    if len(prerequisites) > 5:
        warnings.append(
            f"Step {step.get('step_number')} requires {len(prerequisites)} prerequisites "
            f"(may indicate step is too complex)"
        )

    # Assess declared cognitive load
    declared_load = step.get("cognitive_load", "medium")

    # Calculate effective load based on factors
    load_score = 0
    load_score += num_concepts * 2  # Each concept adds load
    load_score += len(prerequisites)  # Prerequisites add load

    # Determine load level
    if load_score <= 3:
        calculated_load = "low"
    elif load_score <= 6:
        calculated_load = "medium"
    else:
        calculated_load = "high"

    # Check if declared load matches calculated
    if declared_load != calculated_load and num_concepts > 0:
        warnings.append(
            f"Step {step.get('step_number')} cognitive load mismatch: "
            f"declared '{declared_load}' but calculated '{calculated_load}'"
        )

    return {
        "step_number": step.get("step_number"),
        "calculated_load": calculated_load,
        "load_score": load_score,
        "num_concepts": num_concepts,
        "num_prerequisites": len(prerequisites),
        "warnings": warnings
    }


def assess_overall_scaffolding(plan: Dict[str, Any]) -> Dict[str, Any]:
    """
    Assess the overall cognitive load of a scaffolding plan.

    Args:
        plan: Complete scaffolding plan

    Returns:
        Dictionary with overall assessment and recommendations
    """
    audience = plan.get("target_audience", "beginner")
    steps = plan.get("scaffolding_steps", [])
    total_steps = len(steps)

    warnings = []
    recommendations = []

    # Check total number of steps
    if total_steps < 3:
        warnings.append(
            f"Only {total_steps} steps provided. "
            f"Complex concepts typically require 3-7 steps."
        )
    elif total_steps > 7:
        warnings.append(
            f"{total_steps} steps may be too many. "
            f"Consider consolidating or breaking into multiple learning sessions."
        )

    # Assess each step
    step_assessments = []
    high_load_count = 0

    for step in steps:
        assessment = assess_step_load(step, audience)
        step_assessments.append(assessment)
        warnings.extend(assessment["warnings"])

        if assessment["calculated_load"] == "high":
            high_load_count += 1

    # Check distribution of cognitive load
    if high_load_count > total_steps // 2:
        warnings.append(
            f"Too many high-load steps ({high_load_count}/{total_steps}). "
            f"Learners may experience cognitive overload."
        )
        recommendations.append(
            "Break high-load steps into smaller substeps or "
            "reduce number of new concepts per step"
        )

    # Check prerequisite chain
    all_prerequisites = set()
    all_new_concepts = set()

    for step in steps:
        all_prerequisites.update(step.get("prerequisites", []))
        all_new_concepts.update(step.get("new_concepts", []))

    # Prerequisites should not include concepts introduced in this plan
    circular_refs = all_prerequisites.intersection(all_new_concepts)
    if circular_refs:
        warnings.append(
            f"Circular dependencies detected: {', '.join(circular_refs)} "
            f"appear as both prerequisites and new concepts"
        )

    # Check for progression
    load_sequence = [s["calculated_load"] for s in step_assessments]
    if load_sequence and load_sequence[0] == "high":
        recommendations.append(
            "Consider starting with lower cognitive load in initial steps"
        )

    # Determine overall load
    avg_score = sum(s["load_score"] for s in step_assessments) / max(len(step_assessments), 1)
    if avg_score <= 3:
        overall_load = "low"
    elif avg_score <= 5:
        overall_load = "medium"
    else:
        overall_load = "high"

    return {
        "success": True,
        "overall_load": overall_load,
        "total_steps": total_steps,
        "target_audience": audience,
        "step_assessments": step_assessments,
        "high_load_steps": high_load_count,
        "warnings": warnings,
        "recommendations": recommendations,
        "total_new_concepts": len(all_new_concepts),
        "total_prerequisites": len(all_prerequisites)
    }


def main():
    """Main entry point for cognitive load assessment."""
    if len(sys.argv) != 2:
        print("Usage: python assess-cognitive-load.py <scaffolding_plan.yml>", file=sys.stderr)
        sys.exit(1)

    plan_file = Path(sys.argv[1])

    if not plan_file.exists():
        print(f"Error: File not found: {plan_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(plan_file, 'r') as f:
            plan = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        assessment = assess_overall_scaffolding(plan)
        print(json.dumps(assessment, indent=2))

        # Exit with warning code if there are warnings
        if assessment.get("warnings"):
            sys.exit(0)  # Still success, but with warnings

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
