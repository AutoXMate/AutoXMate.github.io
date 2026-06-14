---
id: tsdiscon
namespace: remote:ts
name: tsdiscon
description: Disconnects a Remote Desktop Services session without ending the session.
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
        tsdiscon
  background_templates: []
examples:
  - cmd: "tsdiscon /?"
    description: "Display help and usage information for tsdiscon"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tsdiscon
---