#!/usr/bin/env node
/**
 * check-validate.mjs
 *
 * Runs `claude plugin validate <plugin-path>` for every plugin listed in this
 * repo's root `.claude-plugin/marketplace.json`. Delegates YAML/manifest
 * checking to the official Claude Code CLI, so we never drift from the
 * install-time schema.
 *
 * Usage:
 *   node scripts/check-validate.mjs
 *
 * Exit codes:
 *   0 — every plugin validates clean
 *   1 — any plugin fails validation, or the `claude` CLI is unavailable
 */

import { readFile } from "node:fs/promises";
import { resolve, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __filename = fileURLToPath(import.meta.url);
const repoRoot = resolve(dirname(__filename), "..");

const red = (s) => `\x1b[31m${s}\x1b[0m`;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const yellow = (s) => `\x1b[33m${s}\x1b[0m`;
const bold = (s) => `\x1b[1m${s}\x1b[0m`;

const marketplacePath = join(repoRoot, ".claude-plugin", "marketplace.json");

let marketplace;
try {
  marketplace = JSON.parse(await readFile(marketplacePath, "utf8"));
} catch (err) {
  console.error(red(`✗ Failed to read ${marketplacePath}: ${err.message}`));
  process.exit(1);
}

if (!Array.isArray(marketplace.plugins) || marketplace.plugins.length === 0) {
  console.error(red("✗ marketplace.json has no plugins array or it is empty"));
  process.exit(1);
}

// On Windows, the `claude` launcher is a .cmd / .ps1 shim, so we need shell
// resolution to pick it up via PATHEXT. We pass the full command as one string
// (avoids Node's DEP0190 shell-arg-escape deprecation) and quote embedded paths.
const quote = (s) => `"${String(s).replace(/"/g, '\\"')}"`;

const probe = spawnSync("claude --version", { encoding: "utf8", shell: true });
if (probe.status !== 0) {
  console.error(
    red(`✗ \`claude\` CLI not available on PATH. Install Claude Code or add it to PATH.`),
  );
  process.exit(1);
}
console.log(bold(`\nPlugin validation sweep — ${marketplace.name}`));
console.log(`Using ${(probe.stdout || "").trim()}\n`);

const failures = [];
let passCount = 0;

for (const entry of marketplace.plugins) {
  const { name, source } = entry;
  if (typeof source !== "string") {
    console.log(`  ${yellow("–")} ${String(name).padEnd(28)} (non-relative source)`);
    continue;
  }

  const pluginDir = join(repoRoot, source);
  const result = spawnSync(`claude plugin validate ${quote(pluginDir)}`, {
    encoding: "utf8",
    shell: true,
  });
  const output = (result.stdout || "") + (result.stderr || "");

  if (result.status === 0) {
    console.log(`  ${green("✓")} ${name.padEnd(28)} validation passed`);
    passCount += 1;
  } else {
    console.log(`  ${red("✗")} ${name.padEnd(28)} validation FAILED`);
    failures.push({ name, source, output: output.trim() });
  }
}

if (failures.length > 0) {
  console.error(`\n${red(bold(`✗ ${failures.length} plugin(s) failed validation:`))}\n`);
  for (const f of failures) {
    console.error(red(`── ${f.name}  (${f.source}) ──`));
    console.error(f.output);
    console.error("");
  }
  console.error(
    "Fix the errors above before publishing — these match the validation Claude Code does at install time.",
  );
  process.exit(1);
}

console.log(green(bold(`\n✓ All ${passCount} plugins validate clean against the CLI.\n`)));
