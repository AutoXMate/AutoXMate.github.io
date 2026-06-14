---
id: win-lodctr
namespace: system:windows:performance
name: lodctr
description: Registers performance counter names for services.
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
  template: lodctr /?
  sandbox: execFile
examples:
- description: Display help for lodctr
  command: lodctr /?
references:
- label: lodctr Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lodctr
---
