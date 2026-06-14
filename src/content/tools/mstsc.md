---
id: mstsc
namespace: remote:rdp
name: mstsc
description: Remote Desktop Connection client for connecting to remote Windows desktops and applications.
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
        mstsc
  background_templates: []
examples:
  - cmd: "mstsc /?"
    description: "Display help and usage information for mstsc"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc
---