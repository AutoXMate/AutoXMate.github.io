---
id: impacket-ticketer
namespace: security:impacket:kerberos
name: impacket-ticketer
description: Creates golden/silver Kerberos tickets.
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
- T1558
parameters: []
execution:
  template: impacket-ticketer --help
  sandbox: execFile
examples:
- description: Display help for impacket-ticketer
  command: impacket-ticketer --help
references:
- label: impacket-ticketer Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-ticketer
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
