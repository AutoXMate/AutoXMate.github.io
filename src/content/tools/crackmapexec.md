---
id: sec-crackmapexec
namespace: security:network:exploit
name: crackmapexec
description: Swiss Army knife for network service exploitation (SMB, WinRM, MSSQL,
  SSH, LDAP).
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
  template: crackmapexec --help
  sandbox: execFile
examples:
- description: Display help for crackmapexec
  command: crackmapexec --help
references:
- label: crackmapexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/crackmapexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install crackmapexec
---
