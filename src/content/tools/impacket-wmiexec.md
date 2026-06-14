---
id: impacket-wmiexec
namespace: security:impacket:execution
name: impacket-wmiexec
description: Impacket WMIexec - executes commands via WMI protocol.
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
  template: impacket-wmiexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-wmiexec
  command: impacket-wmiexec --help
references:
- label: impacket-wmiexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-wmiexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
