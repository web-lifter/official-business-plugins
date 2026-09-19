---
name: seo-status
description: Report locally configured SEO providers without revealing credentials or making paid/network requests.
argument-hint: "[local environment or supplied configuration]"
allowed-tools: Read Glob Grep Bash
effort: low
---

# seo-status

## User Context

$ARGUMENTS

## Phase 1: Read capability and input

Read [the runtime guide](../../RUNTIME.md). `$ARGUMENTS` selects the environment to inspect. Without local access, inspect only supplied redacted configuration or connector availability and state that the user's machine was not checked.

## Phase 2: Check

With local Python, run `../../scripts/seo_status.py --json` relative to this skill directory using the user's interpreter. This script uses only the standard library; no virtualenv bootstrap or session restart is required. It detects credential-file and environment-variable presence, including complete multi-part credentials.

## Phase 3: Report

Use the [status template](templates/output-template.md). Show provider name and configured yes/no only, never secret values. An invalid configuration is an error, not 'no providers configured'. File edits are re-read on each call. This check makes no API calls and does not prove credentials are valid, authorised or funded. Do not mutate files.
