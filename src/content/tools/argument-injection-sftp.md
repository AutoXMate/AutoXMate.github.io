---
trust_level: community
id: argument-injection-sftp
namespace: argument:injection:sftp
name: sftp
description: "Argument injection via sftp"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "sftp"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Can be used to execute any command or file on a system, but without stdin/stdout/stderr."
    command: "sftp -D\"touch /tmp/korewashere\"
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/sftp/"
---

# sftp

GTFOArgs entry for sftp. This binary can be used to inject arguments for execution, file operations, or other capabilities.
