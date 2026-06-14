---
id: impacket-secretsdump
namespace: security:impacket:credential
name: impacket-secretsdump
description: Impacket secretsdump - extracts secrets from Windows systems.
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
- T1003
parameters: []
execution:
  template: impacket-secretsdump --help
  sandbox: execFile
examples:
- description: Display help for impacket-secretsdump
  command: impacket-secretsdump --help
references:
- label: impacket-secretsdump Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-secretsdump
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
