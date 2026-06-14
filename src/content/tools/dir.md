---
id: cmd-dir
namespace: system:windows:file
name: dir
description: Displays a list of files and subdirectories in a directory.
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
  template: dir /?
  sandbox: execFile
examples:
- description: Run dir with default options
  command: dir /?
references:
- label: dir Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dir
---
