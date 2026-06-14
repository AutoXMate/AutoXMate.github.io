---
id: hostname
namespace: system:windows:cmd
name: hostname
description: Displays the host name portion of the full computer name of the computer.
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
        hostname
  background_templates: []
examples:
  - cmd: "hostname /?"
    description: "Display help and usage information for hostname"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/hostname
---