---
trust_level: community
id: argument-injection-env
namespace: argument:injection:env
name: env
description: "Argument injection via env"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "env"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The `--split-string` parameter accepts multiple additional arguments. The first positional argument without an `=` executes as a command."
    command: "env '--split-string=sh -c \"id > /tmp/pwned\"' foo
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/env/"
---

# env

GTFOArgs entry for env. This binary can be used to inject arguments for execution, file operations, or other capabilities.
