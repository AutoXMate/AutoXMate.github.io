---
id: sec-ldapdomaindump
namespace: security:ldap:dump
name: ldapdomaindump
description: Dumps LDAP domain information from Active Directory.
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
  template: ldapdomaindump --help
  sandbox: execFile
examples:
- description: Display help for ldapdomaindump
  command: ldapdomaindump --help
references:
- label: ldapdomaindump Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ldapdomaindump
install:
- method: custom
  description: Install via package manager
  commands:
  - pipx install ldapdomaindump
---
