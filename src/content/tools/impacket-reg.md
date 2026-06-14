---
id: impacket-reg
namespace: security:impacket:registry
name: impacket-reg
description: Remote registry manipulation tool from Impacket.
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
  template: impacket-reg --help
  sandbox: execFile
examples:
- description: Display help for impacket-reg
  command: impacket-reg --help
references:
- label: impacket-reg Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-reg
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
