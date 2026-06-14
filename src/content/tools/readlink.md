---
id: sys-readlink
namespace: system:linux:file
name: readlink
description: Displays the target of a symbolic link.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
- macos
features:
- local
mitre_ids: []
parameters: []
execution:
  template: readlink --help
  sandbox: execFile
examples:
- description: Display help for readlink
  command: readlink --help
references:
- label: readlink Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/readlink
---
