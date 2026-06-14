---
id: cmd-wevtutil
namespace: system:windows:logging
name: wevtutil
description: Retrieves information about event logs and publishers, exports, archives,
  and clears event logs.
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
  template: wevtutil /?
  sandbox: execFile
examples:
- description: Run wevtutil with default options
  command: wevtutil /?
references:
- label: wevtutil Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil
---
