---
id: shutdown
namespace: system:windows:admin
name: shutdown
description: Allows shutdown, restart, or logoff of local or remote computers with scheduled timing and comment support.
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
        shutdown
  background_templates: []
examples:
  - cmd: "shutdown /?"
    description: "Display help and usage information for shutdown"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown
---