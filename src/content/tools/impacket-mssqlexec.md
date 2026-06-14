---
id: impacket-mssqlexec
namespace: security:impacket:database
name: impacket-mssqlexec
description: Impacket MSSQLexec - executes commands via MSSQL server.
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
  template: impacket-mssqlexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-mssqlexec
  command: impacket-mssqlexec --help
references:
- label: impacket-mssqlexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-mssqlexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
