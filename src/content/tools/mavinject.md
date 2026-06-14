---
id: windows-execution-mavinject
namespace: windows:execution:mavinject
name: mavinject
description: 'Used by App-v in Windows Located at: C:\Windows\System32\mavinject.exe; C:\Windows\SysWOW64\mavinject.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- system.file.alternate-data-stream
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
  - filesystem_write
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
- mavinject
parameters: []
features: []
execution:
  template: mavinject
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Inject evil.dll into a process with PID 3110. (Inject dll file into running process)
  command: MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll}
- description: Inject file.dll stored as an Alternate Data Stream (ADS) into a process with PID 4172 (Inject dll file into running process)
  command: Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll
references:
- label: '941315826107510784'
  url: https://twitter.com/gN3mes1s/status/941315826107510784
- label: '776122138063409152'
  url: https://twitter.com/Hexcorn/status/776122138063409152
- label: ''
  url: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.013
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml
- type: ioc
  description: mavinject.exe should not run unless APP-v is in use on the workstation
install:
- method: choco
  package_name: mavinject
  commands:
  - choco install mavinject
---


# mavinject

mavinject is a Windows LOLBin. Used by App-v in Windows Located at: C:\Windows\System32\mavinject.exe; C:\Windows\SysWOW64\mavinject.exe.
