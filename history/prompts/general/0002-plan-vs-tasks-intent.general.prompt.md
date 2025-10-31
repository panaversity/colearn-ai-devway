id: "0002"
feature: "general"
stage: general
title: "Plan vs Tasks Intent"
created: 2025-10-31
prompt_type: documentation_review
---

# Prompt History Record: Plan vs Tasks Intent

## PROMPT_TEXT

Sometimes when we use command sp.plan, it also creates tasks.md file which was actually supposed to be generated with sp.tasks command. Check all files attached to find if this intent is mentioned any of these documents.  (See <attachments> above for file contents. You may not need to search or read the file again.)

## RESPONSE_TEXT

- sp.plan.md: No intent to generate tasks.md; outputs are research.md, data-model.md, contracts/, quickstart.md, and agent context update.
- sp.tasks.md: Explicitly defines generating an actionable tasks.md under the feature directory from spec/plan (+ optional artifacts).
- sp.implement.md: Assumes tasks.md exists and advises running /sp.tasks if missing.
- CLAUDE.md: Conceptually groups Phase 2 as "PLAN + TASKS" and references specs/<feature>/tasks.md, but this is guidance, not a command contract.

Conclusion: Only /sp.tasks is documented to create tasks.md; /sp.plan should not.
