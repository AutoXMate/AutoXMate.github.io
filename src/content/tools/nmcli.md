---
id: net-nmcli
namespace: network:linux:config
name: nmcli
description: NetworkManager command-line client.
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
  template: nmcli --help
  sandbox: execFile
examples:
- description: Display help for nmcli
  command: nmcli --help
references:
- label: nmcli Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nmcli
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y network-manager
---
