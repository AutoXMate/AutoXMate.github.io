---
id: ethtool
namespace: network:interface
name: ethtool
description: Displays and changes Ethernet device settings including speed, duplex, auto-negotiation, and driver info.
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
      - "apt-get install -y ethtool"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        ethtool
  background_templates: []
examples:
  - cmd: "ethtool --help"
    description: "Display help and usage information for ethtool"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ethtool
---