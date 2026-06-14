---
id: sec-ldapsearch
namespace: security:ldap:query
name: ldapsearch
description: LDAP search tool for querying directory services.
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
  template: ldapsearch --help
  sandbox: execFile
examples:
- description: Display help for ldapsearch
  command: ldapsearch --help
references:
- label: ldapsearch Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ldapsearch
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y ldap-utils
---
