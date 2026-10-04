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

Located in `skills/`.

_No skills yet._

## Usage

Copy agent files into `.claude/agents/` (project) or `~/.claude/agents/` (user), and skill folders into `.claude/skills/` or `~/.claude/skills/`.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please read our [Code of Conduct](CODE_OF_CONDUCT.md), and report vulnerabilities as described in [`SECURITY.md`](SECURITY.md).

## License

[MIT](LICENSE)
