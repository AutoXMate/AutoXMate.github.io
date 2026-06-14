---
id: impacket-getst
namespace: security:impacket:kerberos
name: impacket-getST
description: Gets Kerberos Service Tickets using credentials.
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
  template: impacket-getST --help
  sandbox: execFile
examples:
- description: Display help for impacket-getST
  command: impacket-getST --help
references:
- label: impacket-getST Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-getST
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
