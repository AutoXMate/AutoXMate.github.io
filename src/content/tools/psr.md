---
id: windows-recon-psr
namespace: windows:recon:psr
name: psr
description: 'Windows Problem Steps Recorder, used to record screen and clicks. Located at: c:\windows\system32\psr.exe; c:\windows\syswow64\psr.exe.'
author: Leon Rodenko
version: 1.0.0
capabilities:
- recon.enumeration
platforms:
- windows
risk_level: low
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
- psr
parameters: []
features: []
execution:
  template: psr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Record a user screen without creating a GUI. You should use "psr.exe /stop" to stop recording and create output file. (Can be used to take screenshots of the user environment)
  command: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
references:
- label: 51722.windows-problem-steps-recorder-psr-quick-and
  url: https://social.technet.microsoft.com/wiki/contents/articles/51722.windows-problem-steps-recorder-psr-quick-and-easy-documenting-of-your-steps-and-procedures.aspx
techniques:
- discovery
- collection
mitre_ids:
- T1113
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml
- type: ioc
  description: psr.exe spawned
- type: ioc
  description: suspicious activity when running with "/gui 0" flag
install:
- method: choco
  package_name: psr
  commands:
  - choco install psr
---


# psr

psr is a Windows LOLBin. Windows Problem Steps Recorder, used to record screen and clicks. Located at: c:\windows\system32\psr.exe; c:\windows\syswow64\psr.exe.
