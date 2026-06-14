---
id: sec-winpeas
namespace: security:windows:enumeration
name: winpeas
description: Windows local privilege escalation enumeration and auditing script.
version: 1.0.0
capabilities:
- security.authentication
- security.auditing
- security.directory-services
platforms:
- windows
features:
- local
mitre_ids: []
parameters: []
execution:
  template: winpeas --help
  sandbox: execFile
examples:
- description: Display help for winpeas
  command: winpeas --help
references:
- label: winpeas Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winpeas
install:
- method: custom
  description: Install via package manager
  commands:
  - curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEAS.bat
---
