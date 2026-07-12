# adr-writer — references

## Canonical template

- **Nygard, Michael.** *Documenting Architecture Decisions.* Cognitect blog, 15 November 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
  - The five-section template (status / context / decision / consequences / alternatives) is taken verbatim from this post.

## Supporting practice

- **Thoughtworks Technology Radar — ADRs ("Adopt", 2018).** ADRs are a long-standing "adopt" recommendation in the Technology Radar.
- **ADR GitHub organisation.** <https://adr.github.io/> — community-maintained collection of ADR templates and tooling, including Markdown Any Decision Records (MADR).

## Rules this skill enforces

1. **Five sections, in order:** context, decision, consequences, alternatives, status. Do not innovate the template.
2. **At least two alternatives.** A decision with no alternatives is not a decision worth recording.
3. **Consequences include negatives.** A consequences section that is all-positive is a marketing pitch, not an ADR.
4. **Supersede, do not delete.** Old ADRs get `status: superseded by ADR-NNN` and forward-link. The history is the point.
5. **One decision per ADR.** If you find yourself recording two decisions, write two ADRs.

See `startups/SOURCES.md` for the broader citation context.
