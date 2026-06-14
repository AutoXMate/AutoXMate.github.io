---
id: getmac
namespace: network:interface
name: getmac
description: Returns the MAC address (physical address) of network adapters on the system.
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
        getmac
  background_templates: []
examples:
  - cmd: "getmac /?"
    description: "Display help and usage information for getmac"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/getmac
---