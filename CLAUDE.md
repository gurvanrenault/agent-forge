# CLAUDE.md

A collection of Claude Code subagents and skills.

## Layout

- `agents/` — subagent definitions (`.md` with YAML frontmatter: `name`, `description`, `model`, `tools`).
- `skills/` — packaged skills (`.skill` files).
- `README.md` — index of agents and skills. Update its tables whenever an agent or skill is added, renamed, or removed.

## Commit policy

- **Propose a commit after every completed change.** Once a change is finished, don't leave it uncommitted silently: list the files to stage and the proposed commit message, and ask the user to validate it.
- **Ask before every commit.** Never commit until the user explicitly approves the proposed files and message.
- **Commit directly on `main`.** No feature branches or PRs unless asked.
- **Never push** unless explicitly asked.
- **Use Conventional Commits:** `<type>(<scope>): <summary>`
  - Types: `feat`, `fix`, `docs`, `refactor`, `chore`
  - Scopes: `agents`, `skills`, `readme`
  - Summary: imperative, lowercase, no trailing period, ≤ 72 chars
  - Examples: `feat(agents): add test-architect agent`, `fix(agents): correct tools entries in frontmatter`, `docs(readme): list new skills`
- One logical change per commit; keep README updates in the same commit as the agent/skill they describe.
