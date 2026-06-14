---
id: impacket-smbexec
namespace: security:impacket:execution
name: impacket-smbexec
description: Impacket SMBexec - executes commands via SMB protocol.
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
  template: impacket-smbexec --help
  sandbox: execFile
examples:
- description: Display help for impacket-smbexec
  command: impacket-smbexec --help
references:
- label: impacket-smbexec Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-smbexec
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
