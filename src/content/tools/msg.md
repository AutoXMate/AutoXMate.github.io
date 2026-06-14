---
id: cmd-msg
namespace: system:windows:communication
name: msg
description: Sends popup messages to users on local or remote machines.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids: []
parameters: []
execution:
  template: msg /?
  sandbox: execFile
examples:
- description: Run msg with default options
  command: msg /?
references:
- label: msg Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msg
---
