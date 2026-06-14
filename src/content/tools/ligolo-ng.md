---
id: ligolo-ng
namespace: network:tunnel:proxy
name: ligolo-ng
description: Tunneling/pivoting proxy for network penetration testing.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: ligolo-ng --help
  sandbox: execFile
examples:
- description: Display help for ligolo-ng
  command: ligolo-ng --help
references:
- label: ligolo-ng Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ligolo-ng
install:
- method: custom
  description: Install via package manager
  commands:
  - go install github.com/nicocha30/ligolo-ng/cmd/ligolo-agent@latest
---
