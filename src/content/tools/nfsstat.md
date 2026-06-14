---
id: net-nfsstat
namespace: network:nfs:stats
name: nfsstat
description: Displays NFS statistics about mounts, RPC calls, and server activity.
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
  template: nfsstat --help
  sandbox: execFile
examples:
- description: Display help for nfsstat
  command: nfsstat --help
references:
- label: nfsstat Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nfsstat
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y nfs-common
---
