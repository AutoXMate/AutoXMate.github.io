---
id: reagentc
namespace: system:windows:recovery
name: reagentc
description: Windows Recovery Environment configuration tool for enabling/disabling WinRE and setting recovery image paths.
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
        reagentc
  background_templates: []
examples:
  - cmd: "reagentc /?"
    description: "Display help and usage information for reagentc"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reagentc
---