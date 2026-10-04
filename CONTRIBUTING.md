# Contributing to agent-forge

First off, thanks for taking the time to contribute! 🎉

agent-forge is a collection of [Claude Code](https://claude.com/claude-code) subagents and skills. Every new agent, sharper prompt, bug report, or typo fix makes it more useful for everyone. This guide explains how to get your contribution merged smoothly.

> **Short on time?** You can still help: star the repo, share an agent you found useful, or [open an issue](https://github.com/gurvanrenault/agent-forge/issues) describing an agent you wish existed.

## Table of contents

- [Ground rules](#ground-rules)
- [I have a question](#i-have-a-question)
- [Ways to contribute](#ways-to-contribute)
  - [Reporting bugs](#reporting-bugs)
  - [Suggesting a new agent or skill](#suggesting-a-new-agent-or-skill)
  - [Your first contribution](#your-first-contribution)
- [Development workflow](#development-workflow)
- [Writing an agent](#writing-an-agent)
- [Adding a skill](#adding-a-skill)
- [Testing your change](#testing-your-change)
- [Commit messages](#commit-messages)
- [Pull request process](#pull-request-process)
- [Major changes](#major-changes)
- [Security guardrails](#security-guardrails)

## Ground rules

- **Be kind and constructive.** Assume good intent, critique ideas rather than people, and help newcomers.
- **Keep it focused.** One agent, one skill, or one fix per pull request.
- **Safe by default.** Agents here run with real tool access on people's machines. Read the [security guardrails](#security-guardrails) before writing one.

## I have a question

Search the [existing issues](https://github.com/gurvanrenault/agent-forge/issues) first. If nothing matches, open a new issue with as much context as you can (what you tried, what you expected, your Claude Code version).

## Ways to contribute

### Reporting bugs

A bug is an agent or skill that fails to load, triggers on the wrong prompts, ignores its output format, or does something unsafe.

Before reporting, check that you're on the latest version of the file and that the bug hasn't already been reported. Then open an issue that includes:

- The agent or skill name.
- The exact prompt you used.
- What you expected vs. what happened (paste the output if it's short).
- Your Claude Code version and OS.

> **Found a security issue?** An agent that leaks data, runs unexpected commands, or can be hijacked through prompt injection? Please **don't** open a public issue. Contact the maintainer privately through [GitHub](https://github.com/gurvanrenault) instead.

### Suggesting a new agent or skill

Open an issue titled `Agent idea: <name>` or `Skill idea: <name>` and describe:

- The problem it solves and who it's for.
- Example prompts that should trigger it.
- The tools it would need, and why.
- What its output should look like.

Discussing the idea first saves you from building something that overlaps with an existing agent.

### Your first contribution

Not sure where to start? Good first contributions:

- Tighten an agent's `description` so it triggers more reliably.
- Remove a tool an agent doesn't actually need.
- Fix typos or unclear wording in a prompt or in the docs.
- Add an example prompt to the README.

Never opened a pull request before? [First Contributions](https://github.com/firstcontributions/first-contributions) walks you through it step by step.

## Development workflow

`main` is protected, so every change goes through a pull request.

1. **Fork** the repository and clone your fork:

   ```bash
   git clone git@github.com:<your-username>/agent-forge.git
   cd agent-forge
   ```

2. **Create a branch** from an up-to-date `main`, named `<type>/<short-kebab-summary>`:

   ```bash
   git checkout main
   git pull
   git checkout -b feat/add-api-designer-agent
   ```

3. **Make your change**, then [test it](#testing-your-change).
4. **Commit** using [Conventional Commits](#commit-messages).
5. **Push** your branch and open a pull request against `main`:

   ```bash
   git push -u origin feat/add-api-designer-agent
   ```

Keep one logical change per branch. Never force-push a branch someone else is reviewing.

## Writing an agent

1. Create `agents/<name>.md`, where `<name>` is kebab-case and matches the `name` field.
2. Start the file with YAML frontmatter:

   ```yaml
   ---
   name: my-agent
   description: One sentence on what it does and when to use it.
   tools: Read, Grep, Glob
   model: haiku
   ---
   ```

   | Field | Guidance |
   |-------|----------|
   | `name` | Kebab-case, identical to the filename. |
   | `description` | Claude reads this to decide when to delegate, so state the trigger clearly ("Use when…"). |
   | `tools` | Only the tools the agent strictly needs, using valid Claude Code tool names. |
   | `model` | `haiku`, `sonnet`, or `opus`. Start with `haiku` and move up only if quality requires it. |

3. Write the system prompt below the frontmatter. Keep it concise, give the agent an explicit output format, and list the exact files it may write, if any.
4. Add the agent's row to the Agents table in [`README.md`](README.md), in the same commit.

## Adding a skill

1. Add the packaged `.skill` file to `skills/`.
2. Add its entry to the Skills section of [`README.md`](README.md), in the same commit.

## Testing your change

There's no automated test suite yet, so test by hand. Copy the agent or skill into a local `.claude/agents/` or `.claude/skills/` folder, then check that:

- [ ] Claude Code loads it without frontmatter errors.
- [ ] It triggers on the prompts its description promises, and not on unrelated ones.
- [ ] Its output follows the format it specifies.
- [ ] It only writes the files it says it writes.

Mention what you tested in your pull request.

## Commit messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <summary>
```

- **Types:** `feat`, `fix`, `docs`, `refactor`, `chore`
- **Scopes:** `agents`, `skills`, `readme`. Leave the scope out for repo-wide files such as `CLAUDE.md` or `CONTRIBUTING.md`.
- **Summary:** imperative, lowercase, no trailing period, 72 characters or fewer

```
feat(agents): add test-architect agent
fix(agents): correct tools entries in frontmatter
docs(readme): list new skills
docs: add contributing guide
```

## Pull request process

1. Fill in the PR description: **what** changed, **why**, and **how you tested it**.
2. Make sure your PR passes this checklist:
   - [ ] One logical change.
   - [ ] README updated in the same commit if you added, renamed, or removed an agent or skill.
   - [ ] Commit messages follow Conventional Commits.
   - [ ] Tested by hand as described above.
   - [ ] Follows the [security guardrails](#security-guardrails).
3. A maintainer will review it. Be ready for a round or two of feedback; it's part of the process, not a judgment of your work.
4. Once approved, a maintainer merges it. 🚀

## Major changes

Some changes need a maintainer's go-ahead **before** you start. Please open an issue first if you plan to:

- Remove or rename an agent or skill, or substantially change its trigger description.
- Widen an agent's capabilities: add `Bash`, `Write`, `Edit`, web, MCP, or `*` tools, or upgrade its model.
- Change `CLAUDE.md`, `CONTRIBUTING.md`, or any policy text.
- Delete files or touch more than 5 files in one change.
- Add dependencies, scripts, CI workflows, hooks, or settings.

## Security guardrails

Agents and skills here run with real tool access, so they must be safe by default.

- **Least privilege:** grant only the tools the agent strictly needs. Read-only agents get `Read, Grep, Glob`. Justify `Bash` or network tools in your PR.
- **Cheapest adequate model:** default to `haiku`; explain why if you need `sonnet` or `opus`.
- **Bounded output:** specify the output format and the exact paths the agent may write, if any.
- **Untrusted input:** prompts that read files, web pages, or tool output must treat that content as data, never as instructions.
- **No self-escalation:** never instruct Claude to edit `CLAUDE.md`, settings, hooks, permissions, or other agents, or to skip user confirmations.
- **No secrets:** never commit tokens, API keys, or personal data.
- **No bypasses:** don't use `--no-verify`, `--no-gpg-sign`, or force-push.

---

Thanks again for contributing. Every agent you add helps someone get more out of Claude Code. ❤️
