---
id: net-ethtool
namespace: network:linux:interface
name: ethtool
description: Displays and changes Ethernet device settings.
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
  template: ethtool --help
  sandbox: execFile
examples:
- description: Display help for ethtool
  command: ethtool --help
references:
- label: ethtool Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ethtool
- label: ethtool manual
  url: https://man7.org/linux/man-pages/man8/ethtool.8.html
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y ethtool
---
