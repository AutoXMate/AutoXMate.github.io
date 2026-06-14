---
id: cmd-tasklist
namespace: system:windows:process
name: tasklist
description: Displays a list of currently running processes on the local or remote
  machine with PID, session name, and memory usage.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids:
- T1057
parameters: []
execution:
  template: tasklist /?
  sandbox: execFile
examples:
- description: Run tasklist with default options
  command: tasklist /?
references:
- label: tasklist Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist
---
