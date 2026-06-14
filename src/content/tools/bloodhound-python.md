---
id: bloodhound-python
namespace: security:ad:analyze
name: bloodhound-python
description: BloodHound Python ingestor for Active Directory relationships.
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
  template: bloodhound-python --help
  sandbox: execFile
examples:
- description: Display help for bloodhound-python
  command: bloodhound-python --help
references:
- label: bloodhound-python Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bloodhound-python
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install bloodhound
---
