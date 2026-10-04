# agent-forge

A collection of Claude Code subagents and skills.

## Agents

Located in [`agents/`](agents/).

| Agent | Model | Description |
|-------|-------|-------------|
| [market-analyst](agents/market-analyst.md) | haiku | Analyzes OSS positioning vs incumbents and proposes a Blue Ocean pivot. Use for market/niche/competitor questions. |
| [product-owner](agents/product-owner.md) | haiku | Converts raw feature ideas into production-ready Agile specifications with strict Gherkin acceptance criteria. |
| [test-architect](agents/test-architect.md) | sonnet | Builds a plain-English unit and security test plan from `src/` code and writes it to `sentries_test_plan.md`. |

## Skills

Located in [`skills/`](skills/). Each skill folder holds a `.skill` file and a plugin `.zip`.

| Skill | Description |
|-------|-------------|
| [expertise-poesie](skills/expertise-poesie/) | Analyzes rap, slam, and lyrics (quality, rhymes, punchlines, flow, references) and checks references on the web. Very concise output, in French. |
| [negotiation](skills/negotiation/) | Coaches you through any negotiation or disagreement: prepare, role-play, draft messages, run it live, or debrief. |

## Usage

Copy agent files into `.claude/agents/` (project) or `~/.claude/agents/` (user), and skill folders into `.claude/skills/` or `~/.claude/skills/`.
