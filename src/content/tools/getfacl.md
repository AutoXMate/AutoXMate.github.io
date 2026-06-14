---
id: sys-getfacl
namespace: system:linux:permissions
name: getfacl
description: Gets file access control lists (ACLs).
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: getfacl --help
  sandbox: execFile
examples:
- description: Display help for getfacl
  command: getfacl --help
references:
- label: getfacl Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/getfacl
---
