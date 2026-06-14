---
id: net-showmount
namespace: network:nfs:export
name: showmount
description: Shows NFS server export lists and mount information.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: showmount --help
  sandbox: execFile
examples:
- description: Display help for showmount
  command: showmount --help
references:
- label: showmount Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/showmount
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y nfs-common
---
