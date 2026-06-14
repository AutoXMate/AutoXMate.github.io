---
id: vssadmin
namespace: system:windows:backup
name: vssadmin
description: Volume Shadow Copy Service administration tool for managing shadow copies, providers, and volumes.
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
        vssadmin
  background_templates: []
examples:
  - cmd: "vssadmin /?"
    description: "Display help and usage information for vssadmin"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin
---