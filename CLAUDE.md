# CLAUDE.md

A collection of Claude Code subagents and skills.

## Layout

- `agents/` — subagent definitions (`.md` with YAML frontmatter: `name`, `description`, `model`, `tools`).
- `skills/` — packaged skills (`.skill` files).
- `README.md` — index of agents and skills. Update its tables whenever an agent or skill is added, renamed, or removed.

## Commit policy

- **Ask before every commit.** Propose the files to stage and the commit message, then wait for explicit approval.
- **Commit directly on `main`.** No feature branches or PRs unless asked.
- **Never push** unless explicitly asked.
- **Use Conventional Commits:** `<type>(<scope>): <summary>`
  - Types: `feat`, `fix`, `docs`, `refactor`, `chore`
  - Scopes: `agents`, `skills`, `readme`
  - Summary: imperative, lowercase, no trailing period, ≤ 72 chars
  - Examples: `feat(agents): add test-architect agent`, `fix(agents): correct tools entries in frontmatter`, `docs(readme): list new skills`
- One logical change per commit; keep README updates in the same commit as the agent/skill they describe.
