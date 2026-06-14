---
id: tasklist
namespace: system:windows:process
name: tasklist
description: Displays a list of currently running processes on the local or remote machine with PID, session name, and memory usage.
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
        tasklist
  background_templates: []
examples:
  - cmd: "tasklist"
    description: "Display verbose task listing"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist
---