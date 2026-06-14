---
id: impacket-gettgt
namespace: security:impacket:kerberos
name: impacket-getTGT
description: Gets Kerberos Ticket Granting Tickets (TGT) from a KDC.
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
  template: impacket-getTGT --help
  sandbox: execFile
examples:
- description: Display help for impacket-getTGT
  command: impacket-getTGT --help
references:
- label: impacket-getTGT Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-getTGT
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
