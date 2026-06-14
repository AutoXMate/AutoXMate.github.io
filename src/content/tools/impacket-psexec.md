---
id: impacket-psexec
namespace: security:impacket:execution
name: impacket-psexec
description: Impacket PsExec - executes processes on remote Windows systems.
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
- T1047
parameters: []
execution:
  template: impacket-psexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-psexec
  command: impacket-psexec --help
references:
- label: impacket-psexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-psexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
