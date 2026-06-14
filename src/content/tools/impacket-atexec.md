---
id: impacket-atexec
namespace: security:impacket:execution
name: impacket-atexec
description: Impacket ATexec - executes commands via Windows Task Scheduler.
version: 1.0.0
capabilities:
- security.authentication
- security.auditing
- security.directory-services
platforms:
- linux
features:
- local
mitre_ids:
- T1053
parameters: []
execution:
  template: impacket-atexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-atexec
  command: impacket-atexec --help
references:
- label: impacket-atexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-atexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
