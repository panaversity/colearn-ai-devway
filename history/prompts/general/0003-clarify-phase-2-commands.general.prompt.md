id: "0003"
feature: "general"
stage: general
title: "Clarify Phase 2 commands"
created: 2025-10-31
prompt_type: documentation_update
---

# Prompt History Record: Clarify Phase 2 commands

## PROMPT_TEXT

Identify and eliminate the source of confusion in phase-2 (See <attachments> above for file contents. You may not need to search or read the file again.)

## RESPONSE_TEXT

- Updated `CLAUDE.md` to rename "Phase 2: PLAN + TASKS" to "PLAN and TASKS (separate commands)" and added a command mapping: `/sp.plan` produces plan artifacts; `/sp.tasks` generates tasks.md.
- Added an explicit note to `.claude/commands/sp.plan.md` stating it does not generate `tasks.md` and to run `/sp.tasks` afterwards.
- Strengthened `.claude/commands/sp.tasks.md` intro to say it is the authoritative generator of `tasks.md` and is typically run after `/sp.plan`.

Conclusion: Documentation now clearly separates responsibilities and should prevent confusion about which command creates `tasks.md`.
