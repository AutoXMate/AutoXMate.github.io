---
id: cmd-nltest
namespace: security:ad:trust
name: nltest
description: Network test tool for querying and managing Active Directory trust relationships.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids: []
parameters: []
execution:
  template: nltest /?
  sandbox: execFile
examples:
- description: Run nltest with default options
  command: nltest /?
references:
- label: nltest Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nltest
---
