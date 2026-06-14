---
id: windows-execution-msconfig
namespace: windows:execution:msconfig
name: msconfig
description: 'MSConfig is a troubleshooting tool which is used to temporarily disable
  or re-enable software, device drivers or Windows services that run during startup
  process to help the user determine the cause of a problem with Windows Located at:
  C:\Windows\System32\msconfig.exe.'
author: Oddvar Moe
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
- msconfig
parameters: []
features:
- compression
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: msconfig
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes command embeded in crafted c:\windows\system32\mscfgtlc.xml.
    (Code execution using Msconfig.exe)
  command: Msconfig.exe -5
references:
- label: '991314564896690177'
  url: https://twitter.com/pabraeken/status/991314564896690177
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_uac_bypass_msconfig_gui.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml
- type: ioc
  description: mscfgtlc.xml changes in system32 folder
install:
- method: choco
  package_name: msconfig
  commands:
  - choco install msconfig
---

# msconfig

msconfig is a Windows LOLBin. MSConfig is a troubleshooting tool which is used to temporarily disable or re-enable software, device drivers or Windows services that run during startup process to help the user determine the cause of a problem with Windows Located at: C:\Windows\System32\msconfig.exe.
