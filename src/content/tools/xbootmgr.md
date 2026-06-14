---
id: windows-execution-xbootmgr
namespace: windows:execution:xbootmgr
name: xbootmgr
description: 'Windows Performance Toolkit binary used to start performance traces.
  Located at: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe;
  C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe.'
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
- xbootmgr
parameters: []
features:
- compression
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: xbootmgr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes an executable after the trace is complete using the callBack
    parameter. (Executes code as part of post-trace automation flow.)
  command: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -callBack
    {PATH:.exe}
- description: Executes an executable before each trace run using the preTraceCmd
    parameter. (Executes code as part of pre-trace automation or staging.)
  command: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -preTraceCmd
    {PATH:.exe}
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
  package_name: xbootmgr
  commands:
  - choco install xbootmgr
---

# xbootmgr

xbootmgr is a Windows LOLBin. Windows Performance Toolkit binary used to start performance traces. Located at: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe; C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe.
