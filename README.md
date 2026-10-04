# agent-forge

[![Validate](https://github.com/gurvanrenault/agent-forge/actions/workflows/validate.yml/badge.svg)](https://github.com/gurvanrenault/agent-forge/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A collection of Claude Code subagents and skills.

## Agents

Located in [`agents/`](agents/).

| Agent | Model | Description |
|-------|-------|-------------|
| [market-analyst](agents/market-analyst.md) | haiku | Compares a product or project with competitors and suggests one way to stand out. Read-only; replies inline. |
| [product-owner](agents/product-owner.md) | haiku | Turns a rough feature idea into a ready-to-build spec with user stories and Given/When/Then acceptance criteria. Replies inline, or writes `specs/<feature-name>.md` on request. |
| [test-architect](agents/test-architect.md) | sonnet | Reads source code in any language and writes a plain-English unit and security test plan to `TEST_PLAN.md`. |

## Skills

Located in [`skills/`](skills/). Each `.skill` file is a zip archive containing a skill folder with its `SKILL.md`.

| Skill | Language | Description |
|-------|----------|-------------|
| [expertise-poesie](skills/expertise-poesie.skill) | French | Analyzes rap, slam, and lyrics: rhymes, punchlines, flow of ideas, and references (checked on the web). Ultra-concise output. |
| [negotiation](skills/negotiation.skill) | English | Coaches any negotiation or disagreement: prepare, role-play, draft messages, run live, or debrief. Covers salary, contracts, work, family, and everyday disputes. |

## Usage

**Agents:** copy the `.md` file into `.claude/agents/` (project) or `~/.claude/agents/` (user).

```bash
cp agents/test-architect.md ~/.claude/agents/
```

**Skills:** unzip the `.skill` file into `.claude/skills/` (project) or `~/.claude/skills/` (user).

```bash
unzip skills/negotiation.skill -d ~/.claude/skills/
```

Restart Claude Code, or start a new session, to pick them up.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please read our [Code of Conduct](CODE_OF_CONDUCT.md), and report vulnerabilities as described in [`SECURITY.md`](SECURITY.md).

## License

[MIT](LICENSE)
