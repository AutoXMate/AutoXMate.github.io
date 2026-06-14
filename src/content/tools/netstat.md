---
id: netstat
namespace: network:monitoring
name: netstat
description: Displays active TCP connections, listening ports, routing tables, and network protocol statistics.
version: "1.0.0"
capabilities:
  - network-diagnostics
  - information-gathering
  - reconnaissance
features:
  - local
  - batch
install:
  - method: native
    commands:
      - ""
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        netstat
  background_templates: []
examples:
  - cmd: "netstat"
    description: "Display all active connections and listening ports"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat
---