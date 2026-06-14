---
id: ksetup
namespace: security:kerberos
name: ksetup
description: Configures Kerberos settings including realm mappings, keytab files, and encryption types.
version: "1.0.0"
capabilities:
  - windows-command
  - system-administration
  - information-gathering
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
  method: cmd
  templates:
    - template: |
        ksetup
  background_templates: []
examples:
  - cmd: "ksetup /?"
    description: "Display help and usage information for ksetup"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ksetup
---