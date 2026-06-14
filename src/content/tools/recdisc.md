---
id: recdisc
namespace: system:windows:recovery
name: recdisc
description: Creates a system repair disc that can be used to boot into Windows Recovery Environment.
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
        recdisc
  background_templates: []
examples:
  - cmd: "recdisc /?"
    description: "Display help and usage information for recdisc"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/recdisc
---