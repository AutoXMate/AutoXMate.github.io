---
id: sec-linpeas
namespace: security:linux:enumeration
name: linpeas
description: Linux local privilege escalation enumeration and auditing script.
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
  template: linpeas --help
  sandbox: execFile
examples:
- description: Display help for linpeas
  command: linpeas --help
references:
- label: linpeas Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/linpeas
install:
- method: custom
  description: Install via package manager
  commands:
  - curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh
---
