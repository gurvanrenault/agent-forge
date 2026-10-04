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

Located in [`skills/`](skills/). Each skill folder holds a `.skill` file and a plugin `.zip`.

| Skill | Description |
|-------|-------------|
| [expertise-poesie](skills/expertise-poesie/) | Analyzes rap, slam, and lyrics (quality, rhymes, punchlines, flow, references) and checks references on the web. Very concise output, in French. |
| [negotiation](skills/negotiation/) | Coaches you through any negotiation or disagreement: prepare, role-play, draft messages, run it live, or debrief. |

## Usage

Agents are plain `.md` files. Skills ship as `<name>.skill` (a zip holding `<name>/SKILL.md` plus any `references/`) and as a plugin `.zip` (the same skill under `.claude-plugin/`).

### Claude Code

- **Agents:** copy the `.md` file into `.claude/agents/` (project) or `~/.claude/agents/` (user).
- **Skills:** unzip the `.skill` file into `.claude/skills/` or `~/.claude/skills/`, so you get `skills/<name>/SKILL.md`.
  ```sh
  unzip skills/negotiation/negotiation.skill -d ~/.claude/skills/
  ```
- **As a plugin:** unzip the plugin `.zip` into a folder and start Claude Code with `claude --plugin-dir <folder>`.

### Claude.ai and Claude Desktop

- **Skills:** go to **Settings → Capabilities → Skills**, choose **Upload skill**, and pick the `.skill` file.
- **Agents:** create a Project and paste the agent's body (everything below the `---` frontmatter) into the project instructions.

### ChatGPT

ChatGPT doesn't read Claude's `SKILL.md` or agent formats, but the instructions work as plain text:

1. Create a custom GPT (**Explore GPTs → Create → Configure**) or a Project.
2. Open the `.skill` file as a zip and paste the body of `SKILL.md` (everything below the `---` frontmatter) into **Instructions**. For an agent, paste the body of its `.md` file.
3. Upload any `references/*.md` files as **Knowledge** (custom GPT) or project files.
4. Give it the skill's name, and use the frontmatter `description` as its description.

Tool settings (`tools`, `model`) in agent frontmatter are Claude Code–specific and don't carry over.
