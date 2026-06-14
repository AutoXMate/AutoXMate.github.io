---
id: nbtstat
namespace: network:netbios
name: nbtstat
description: Displays NetBIOS over TCP/IP protocol statistics, name tables, and cache information for local and remote machines.
version: "1.0.0"
capabilities:
  - windows-command
  - system-administration
  - information-gathering
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
        nbtstat
  background_templates: []
examples:
  - cmd: "nbtstat /?"
    description: "Display help and usage information for nbtstat"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nbtstat
---