---
id: impacket-samrdump
namespace: security:impacket:credential
name: impacket-samrdump
description: Dumps SAM (Security Account Manager) information from remote systems.
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
  template: impacket-samrdump --help
  sandbox: execFile
examples:
- description: Display help for impacket-samrdump
  command: impacket-samrdump --help
references:
- label: impacket-samrdump Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-samrdump
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
