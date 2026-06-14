---
id: tcpreplay
namespace: network:capture
name: tcpreplay
description: Replays captured network traffic from pcap files, allowing testing of network devices and IDS/IPS systems.
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
      - "apt-get install -y tcpreplay"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        tcpreplay
  background_templates: []
examples:
  - cmd: "tcpreplay --help"
    description: "Display help and usage information for tcpreplay"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tcpreplay
---