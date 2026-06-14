---
id: cmd-shutdown
namespace: system:windows:admin
name: shutdown
description: Shutdown, restart, or logoff of local or remote computers.
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
  template: shutdown /?
  sandbox: execFile
examples:
- description: Run shutdown with default options
  command: shutdown /?
references:
- label: shutdown Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown
---
