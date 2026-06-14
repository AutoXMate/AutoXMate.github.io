---
id: msg
namespace: system:windows:communication
name: msg
description: Sends popup messages to users on local or remote machines via the Messenger service.
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
        msg
  background_templates: []
examples:
  - cmd: "msg /server:localhost "test message""
    description: "Display help and usage information for msg"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msg
---