---
id: windows-execution-xbootmgrsleep
namespace: windows:execution:xbootmgrsleep
name: xbootmgrsleep
description: 'Windows Performance Toolkit binary used for tracing and analyzing system performance during sleep and resume transitions. Located at: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe; C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe.'
author: Avihay Eldad
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
risk_level: high
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
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- xbootmgrsleep
parameters: []
features: []
execution:
  template: xbootmgrsleep
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute executable via XBootMgrSleep, with a 1 second (=1000 milliseconds) delay. Alternatively, it is also possible to replace the delay with any string for immediate execution. (Performs execution of specified executable, can be used as a defense evasion)
  command: xbootmgrsleep.exe 1000 {PATH:.exe}
references:
- label: reference
  url: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections: []
install:
- method: choco
  package_name: xbootmgrsleep
  commands:
  - choco install xbootmgrsleep
---


# xbootmgrsleep

xbootmgrsleep is a Windows LOLBin. Windows Performance Toolkit binary used for tracing and analyzing system performance during sleep and resume transitions. Located at: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe; C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe.
