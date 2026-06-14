---
id: net-tcpreplay
namespace: network:capture:traffic
name: tcpreplay
description: Replays pcap network traffic for device testing.
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
  template: tcpreplay --help
  sandbox: execFile
examples:
- description: Display help for tcpreplay
  command: tcpreplay --help
references:
- label: tcpreplay Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tcpreplay
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y tcpreplay
---
