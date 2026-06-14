---
id: bcdedit
namespace: system:windows:boot
name: bcdedit
description: Boot Configuration Data (BCD) editor for managing boot configuration and troubleshooting startup issues.
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
        bcdedit
  background_templates: []
examples:
  - cmd: "bcdedit /?"
    description: "Display help and usage information for bcdedit"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
---