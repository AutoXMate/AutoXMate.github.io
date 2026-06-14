---
id: tscon
namespace: remote:ts
name: tscon
description: Connects a Remote Desktop Services session to a different session, enabling session hijacking.
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
        tscon
  background_templates: []
examples:
  - cmd: "tscon /?"
    description: "Display help and usage information for tscon"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tscon
---