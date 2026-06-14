---
id: cmd-dcdiag
namespace: security:ad:diagnostic
name: dcdiag
description: Domain Controller diagnostics tool for analyzing AD domain controllers.
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
  template: dcdiag /?
  sandbox: execFile
examples:
- description: Run dcdiag with default options
  command: dcdiag /?
references:
- label: dcdiag Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dcdiag
---
