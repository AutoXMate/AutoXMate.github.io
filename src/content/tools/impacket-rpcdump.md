---
id: impacket-rpcdump
namespace: security:impacket:enumeration
name: impacket-rpcdump
description: Dumps RPC endpoint information from remote systems.
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
  template: impacket-rpcdump --help
  sandbox: execFile
examples:
- description: Display help for impacket-rpcdump
  command: impacket-rpcdump --help
references:
- label: impacket-rpcdump Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/impacket-rpcdump
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install impacket
---
