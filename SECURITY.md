# Security Policy

agent-forge ships prompts that run inside Claude Code with real tool access, so a flawed agent can do real damage. We take reports seriously.

## Supported versions

Only the latest commit on `main` is supported. Fixes are not backported.

## What counts as a vulnerability

- An agent or skill that can be steered by untrusted content (files, web pages, tool output) into running commands, writing files, or leaking data. In other words, prompt injection.
- An agent that writes outside the paths it declares, or uses tools beyond what its purpose requires.
- Instructions that make Claude bypass user confirmations, edit settings, hooks, or permissions, or disable safety checks.
- Secrets or personal data committed to the repository.

Bugs that don't have a security impact (an agent triggering on the wrong prompt, poor output quality) belong in a regular [issue](https://github.com/gurvanrenault/agent-forge/issues).

## Reporting a vulnerability

**Please don't open a public issue, discussion, or pull request for security problems.**

Report it privately through GitHub's [private vulnerability reporting](https://github.com/gurvanrenault/agent-forge/security/advisories/new). Include:

- The affected agent or skill.
- The prompt or input that triggers the problem.
- What happens, and what impact it could have.
- Your Claude Code version, if relevant.

## What to expect

- **Acknowledgement** within 7 days.
- **Assessment and fix plan** within 30 days, kept up to date in the advisory.
- **Credit** in the published advisory, unless you prefer to stay anonymous.

Please give us a reasonable chance to fix the issue before disclosing it publicly.
