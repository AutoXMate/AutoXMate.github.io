---
id: csvde
namespace: security:ad:export
name: csvde
description: Imports and exports Active Directory objects using comma-separated-value (CSV) format files.
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
        csvde
  background_templates: []
examples:
  - cmd: "csvde /?"
    description: "Display help and usage information for csvde"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/csvde
---