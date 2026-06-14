---
id: cmd-sfc
namespace: system:windows:integrity
name: sfc
description: System File Checker scans and verifies protected system files, replacing
  corrupted versions from the cache.
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
  template: sfc /?
  sandbox: execFile
examples:
- description: Run sfc with default options
  command: sfc /?
references:
- label: sfc Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc
---
