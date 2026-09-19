# Runtime and capability contract

Read this guide before a skill. These rules govern host-specific references in the workflow.

## Input and tools

`$ARGUMENTS` means the user's current request and supplied materials when the host does not substitute slash-command arguments. Do not wait for that literal token. Claude tool names (`Read`, `Bash`, `AskUserQuestion`, `Agent`) describe capabilities, not permissions or guaranteed APIs. Use the actual tools available; ask ordinary questions when no question tool exists. Read bundled references relative to the current skill directory, not the user's working directory.

Never invent a connector, command, source, calculation result or successful action. Discover available authorised connectors before using them. An absent optional connector is not a reason to abandon analysis of supplied files. If a required input or capability is missing, identify the precise gap and produce only what the evidence supports. Do not claim a tool run when providing instructions instead.

## Files and execution

In a local project, use the documented `.project/` output path and create its parent directory. In a hosted chat without that project mounted, use an available sandbox and return an actual file link, or deliver the Markdown directly. Never claim to have saved into the user's repository from a chat sandbox. Keep installed plugin files read-only; persistent runtime data belongs in `PLUGIN_DATA`, then `CLAUDE_PLUGIN_DATA`, or a user-selected data directory.

Run helper scripts only when execution is available. Before installing dependencies, downloading models, crawling sites or making paid API calls, explain the need and obtain the appropriate user authorisation. Use bounded reads and requests. Do not expose secrets in chat, logs, reports or source control. Prefer existing authorised connectors to local credential files in ChatGPT.

## Orchestration and evidence

Slash commands are workflow identifiers. Invoke an available skill using the host's supported mechanism. If subagents are unavailable, read the relevant bundled recipe and perform its steps sequentially; never simulate agent output or treat a filename as an installed tool. Cross-plugin handoffs are optional unless their capability is genuinely essential. Preserve standalone outputs when another plugin is absent.

Treat examples as illustrative, not business facts or test evidence. Separate observed data, user assumptions and estimates. Benchmarks require an identifiable source, date and comparable population. Planning does not authorise deploying, charging money, publishing, sending messages or changing production systems. These require explicit user direction and any applicable confirmation.
