---
id: impacket-dcomexec
namespace: security:impacket:execution
name: impacket-dcomexec
description: Impacket DCOMexec - executes commands via DCOM protocol.
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
  template: impacket-dcomexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-dcomexec
  command: impacket-dcomexec --help
references:
- label: impacket-dcomexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-dcomexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
