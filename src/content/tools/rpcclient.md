---
id: sec-rpcclient
namespace: security:rpc:client
name: rpcclient
description: SMB/CIFS RPC client for MS-RPC protocol operations.
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
  template: rpcclient --help
  sandbox: execFile
examples:
- description: Display help for rpcclient
  command: rpcclient --help
references:
- label: rpcclient Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rpcclient
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y smbclient
---
