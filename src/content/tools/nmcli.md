---
id: nmcli
namespace: network:linux:manager
name: nmcli
description: Command-line client for NetworkManager. Manages network connections, devices, and Wi-Fi from the terminal.
version: "1.0.0"
capabilities:
  - network-diagnostics
  - information-gathering
  - reconnaissance
features:
  - local
  - batch
install:
  - method: apt
    commands:
      - "apt-get install -y network-manager"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        nmcli
  background_templates: []
examples:
  - cmd: "nmcli --help"
    description: "Display help and usage information for nmcli"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nmcli
---