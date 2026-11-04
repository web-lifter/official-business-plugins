# Official Business Plugins - contributor contract

Work only in this repository unless requested otherwise. Inspect live files before
editing. Use Australian English and distinguish evidence, assumptions and risk.

Keep one shared skill tree. Claude manifests plus the root Claude catalogue are
the source metadata; run `python scripts/sync-openai.py` to update native manifests,
marketplace metadata and skill UI metadata. Do not hand-edit generated metadata.
New or changed plugin content requires an increasing release version in both
source locations. Never merge or publish without an explicit request.

Skills require scalar `name`, `description`, quoted `argument-hint` and `effort`;
name must match the directory. Keep SKILL.md under 500 lines, link its RUNTIME.md,
and bundle the referenced template, example and licence. Runtime guides override
host-specific legacy terminology. Tool names do not grant permissions. Optional
connectors/subagents must have an honest fallback.

Keep installed plugin trees read-only. No startup package installation hooks.
Use explicit setup, persistent runtime data, bounded network calls and separate
planning from deployment. Treat credentials and user data as sensitive.

Run metadata parity, portability, version checks and pytest before a PR. Run the
official Claude validator when available; report absence rather than substituting
a static check and claiming equivalence. Do not claim live ChatGPT import, prompt
quality, browser tests or integrations were verified without actually testing them.

Preserve useful skill identifiers. Deprecation requires migration guidance and
usage/evaluation evidence; overlap alone is not proof that a skill is obsolete.
