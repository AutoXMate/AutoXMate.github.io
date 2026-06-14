---
id: qwinsta
namespace: remote:ts
name: qwinsta
description: Displays information about Remote Desktop Services sessions on a remote server.
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
        qwinsta
  background_templates: []
examples:
  - cmd: "qwinsta /?"
    description: "Display help and usage information for qwinsta"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/qwinsta
---