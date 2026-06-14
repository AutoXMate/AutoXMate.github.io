---
id: windows-execution-pixtool
namespace: windows:execution:pixtool
name: pixtool
description: 'Command line utility for taking and analyzing PIX GPU captures. Located at: C:\Program Files\Microsoft PIX\pixtool.exe; C:\Program Files (x86)\Microsoft PIX\pixtool.exe.'
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
- pixtool
parameters: []
features: []
execution:
  template: pixtool
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launches an executable via PIX command-line utility. (Executes an executable under a trusted, Microsoft signed binary.)
  command: pixtool.exe launch {PATH_ABSOLUTE:.exe}
references:
- label: ''
  url: https://devblogs.microsoft.com/pix/pixtool/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: pixtool
  commands:
  - choco install pixtool
---


# pixtool

pixtool is a Windows LOLBin. Command line utility for taking and analyzing PIX GPU captures. Located at: C:\Program Files\Microsoft PIX\pixtool.exe; C:\Program Files (x86)\Microsoft PIX\pixtool.exe.
