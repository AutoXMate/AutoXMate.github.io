---
id: sec-ldapwhoami
namespace: security:ldap:query
name: ldapwhoami
description: Sends an LDAP WhoAmI extended operation to a directory server.
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
  template: ldapwhoami --help
  sandbox: execFile
examples:
- description: Display help for ldapwhoami
  command: ldapwhoami --help
references:
- label: ldapwhoami Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ldapwhoami
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y ldap-utils
---
