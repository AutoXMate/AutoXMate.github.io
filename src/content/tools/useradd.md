---
id: useradd
namespace: system:linux:user
name: useradd
description: Creates a new user account on the system with specified options for home directory, shell, groups, and expiry.
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
        useradd
  background_templates: []
examples:
  - cmd: "useradd --help"
    description: "Display help and usage information for useradd"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/useradd
---