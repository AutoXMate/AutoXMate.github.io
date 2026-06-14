---
id: driverquery
namespace: system:windows:driver
name: driverquery
description: Displays a list of all installed device drivers and their properties including driver name, type, and module name.
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
        driverquery
  background_templates: []
examples:
  - cmd: "driverquery /?"
    description: "Display help and usage information for driverquery"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/driverquery
---