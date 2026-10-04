# agent-forge

[![Validate](https://github.com/gurvanrenault/agent-forge/actions/workflows/validate.yml/badge.svg)](https://github.com/gurvanrenault/agent-forge/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A collection of Claude Code subagents and skills.

## Agents

Located in [`agents/`](agents/).

| Agent | Model | Description |
|-------|-------|-------------|
| [market-analyst](agents/market-analyst.md) | haiku | Analyzes OSS positioning vs incumbents and proposes a Blue Ocean pivot. Use for market/niche/competitor questions. |
| [product-owner](agents/product-owner.md) | haiku | Converts raw feature ideas into production-ready Agile specifications with strict Gherkin acceptance criteria. |
| [test-architect](agents/test-architect.md) | sonnet | Builds a plain-English unit and security test plan from `src/` code and writes it to `TEST_PLAN.md`. |

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
