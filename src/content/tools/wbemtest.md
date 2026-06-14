---
id: windows-execution-wbemtest
namespace: windows:execution:wbemtest
name: wbemtest
description: 'WMI/WBEM Test Binary Located at: c:\windows\system32\wbem\wbemtest.exe.'
author: saulpanders
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
- wbemtest
parameters: []
features: []
execution:
  template: wbemtest
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitary commands through WMI through a GUI managment interface for Web Based Enterprise Management testing (WBEM). Uses WMI to Create and instance of a Win32_Process WMI class with a commandline argument of the target command to spawn. Spawns a GUI so it requires interactive access. For a demo, see link to blog in resources. (Execute arbitrary commands through WMI classes)
  command: wbemtest.exe
references:
- label: lolbas-wbemtest.html
  url: https://saulpanders.github.io/2025/01/20/lolbas-wbemtest.html
techniques:
- execution
mitre_ids:
- T1047
detections:
- type: ioc
  description: wbemtest.exe binary spawned
install:
- method: choco
  package_name: wbemtest
  commands:
  - choco install wbemtest
---


# wbemtest

wbemtest is a Windows LOLBin. WMI/WBEM Test Binary Located at: c:\windows\system32\wbem\wbemtest.exe.
