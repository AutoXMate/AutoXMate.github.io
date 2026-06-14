---
id: sys-uname
namespace: system:linux:info
name: uname
description: Prints system information like kernel name, hostname, OS, and architecture.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: uname --help
  sandbox: execFile
examples:
- description: Display help for uname
  command: uname --help
references:
- label: uname Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/uname
---
