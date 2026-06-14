---
trust_level: community
id: argument-injection-psql
namespace: argument:injection:psql
name: psql
description: "Argument injection via psql"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "psql"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The `--output` argument pipes data through external commands when the value is prefixed with `|`."
    command: "psql -o'|id>/tmp/foo'
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/psql/"
---

# psql

GTFOArgs entry for psql. This binary can be used to inject arguments for execution, file operations, or other capabilities.
