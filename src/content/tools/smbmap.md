---
id: sec-smbmap
namespace: security:smb:enumeration
name: smbmap
description: SMB enumeration tool for share drives, permissions, and directory contents.
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
  template: smbmap --help
  sandbox: execFile
examples:
- description: Display help for smbmap
  command: smbmap --help
references:
- label: smbmap Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/smbmap
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y smbmap
---
