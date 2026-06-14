---
id: arc-gunzip
namespace: archive:linux:compression
name: gunzip
description: Decompresses gzip-compressed (.gz) files.
version: 1.0.0
capabilities:
- filesystem.compression
- filesystem.management
- system.commands
platforms:
- linux
- macos
features:
- local
mitre_ids: []
parameters: []
execution:
  template: gunzip --help
  sandbox: execFile
examples:
- description: Display help for gunzip
  command: gunzip --help
references:
- label: gunzip Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gunzip
---
