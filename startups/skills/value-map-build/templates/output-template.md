# value-map-build template

This skill produces VPC artifacts using the canonical canvas template
at [`shared/templates/vpc-template.md`](../../../../shared/templates/vpc-template.md).

The skill copies that file, substitutes placeholders, and writes to
`03-value-proposition/vpc-{{segment-slug}}-v{{N}}.md`. The VPC body
is validated against
[`shared/schemas/vpc.schema.json`](../../../../shared/schemas/vpc.schema.json)
at write time.

## Substitutions

| Placeholder | Value |
|-------------|-------|
| `{{segment-label}}` | Human-readable segment name from segment frontmatter `title:` |
| `{{segment-slug}}` | kebab-case slug from segment folder name |
| `{{N}}` | Auto-incrementing version number |
| `{{venture-name}}` | From `memex.config.json` or vision sketch frontmatter `owner:` |
| `{{YYYY-MM-DD}}` | Today's date |

## Per-skill notes

- The right half (jobs / pains / gains) is *not* duplicated here. The
  skill writes a one-line `(Imported by reference. See profile.md.)`
  pointer and lets the segment profile remain the source of truth.
- Each pain-reliever row's `Maps to pain` column must reference a row
  ID from the segment profile (e.g. `P-01`). The skill rejects writes
  where this column is empty.
- The `Fit report` section is left as a placeholder; `vpc-fit-check`
  populates it.

See the example at [`examples/example-output.md`](../examples/example-output.md).
