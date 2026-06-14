---
id: sec-smbclient
namespace: security:smb:client
name: smbclient
description: SMB/CIFS client for accessing SMB shares on remote servers.
version: 1.0.0
capabilities:
- security.authentication
- security.auditing
- security.directory-services
platforms:
- linux
features:
- local
mitre_ids:
- T1021
parameters: []
execution:
  template: smbclient --help
  sandbox: execFile
examples:
- description: Display help for smbclient
  command: smbclient --help
references:
- label: smbclient Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/smbclient
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y smbclient
---
