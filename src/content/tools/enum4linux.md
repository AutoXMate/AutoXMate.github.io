---
id: sec-enum4linux
namespace: security:smb:enumeration
name: enum4linux
description: Enumerates SMB/NetBIOS information from Windows systems.
version: 1.0.0
capabilities:
- security.authentication
- security.auditing
- security.directory-services
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: enum4linux --help
  sandbox: execFile
examples:
- description: Display help for enum4linux
  command: enum4linux --help
references:
- label: enum4linux Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/enum4linux
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y enum4linux
---
