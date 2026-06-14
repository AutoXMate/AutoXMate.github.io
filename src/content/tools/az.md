---
id: sys-az
namespace: system:cloud:azure
name: az
description: Azure CLI - manages Azure resources from the command line.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: az --help
  sandbox: execFile
examples:
- description: Display help for az
  command: az --help
references:
- label: az Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/az
install:
- method: custom
  description: Install via package manager
  commands:
  - curl -sL https://aka.ms/InstallAzureCLIDeb | bash
---
