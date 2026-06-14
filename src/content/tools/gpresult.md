---
id: gpresult
namespace: system:windows:policy
name: gpresult
description: Displays the Resultant Set of Policy (RSoP) information for a target user and computer including applied GPOs.
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
        gpresult
  background_templates: []
examples:
  - cmd: "gpresult /?"
    description: "Display help and usage information for gpresult"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult
---