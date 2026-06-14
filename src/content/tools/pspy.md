---
id: sec-pspy
namespace: security:linux:monitor
name: pspy
description: Process monitor for Linux privilege escalation detection.
version: 1.0.0
capabilities:
- security.authentication
- security.auditing
- security.directory-services
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: pspy --help
  sandbox: execFile
examples:
- description: Display help for pspy
  command: pspy --help
references:
- label: pspy Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pspy
install:
- method: custom
  description: Install via package manager
  commands:
  - wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64
---
