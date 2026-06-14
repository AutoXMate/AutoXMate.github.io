---
id: rwinsta
namespace: remote:ts
name: rwinsta
description: Resets (logs off) a Remote Desktop Services session on a remote server.
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
        rwinsta
  background_templates: []
examples:
  - cmd: "rwinsta /?"
    description: "Display help and usage information for rwinsta"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rwinsta
---