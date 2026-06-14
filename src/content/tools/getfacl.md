---
id: getfacl
namespace: system:linux:permissions
name: getfacl
description: Gets file access control lists (ACLs). Displays the ACL entries for one or more files.
version: "1.0.0"
capabilities:
  - system-administration
  - information-gathering
  - file-system
features:
  - local
  - batch
install:
  - method: native
    commands:
      - ""
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        getfacl
  background_templates: []
examples:
  - cmd: "getfacl --help"
    description: "Display help and usage information for getfacl"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/getfacl
---