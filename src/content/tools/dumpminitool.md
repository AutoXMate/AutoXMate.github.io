---
id: windows-credential-dumpminitool
namespace: windows:credential:dumpminitool
name: dumpminitool
description: 'Dump tool part Visual Studio 2022 Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe.'
author: mr.d0x
version: 1.0.0
capabilities:
- credential.dump
platforms:
- windows
risk_level: critical
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
- dumpminitool
parameters: []
features: []
execution:
  template: dumpminitool
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Creates a memory dump of the lsass process (Create memory dump and parse it offline)
  command: DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full
references:
- label: '1511415432888131586'
  url: https://twitter.com/mrd0x/status/1511415432888131586
techniques:
- credential-access
mitre_ids:
- T1003.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
install:
- method: choco
  package_name: dumpminitool
  commands:
  - choco install dumpminitool
---


# dumpminitool

dumpminitool is a Windows LOLBin. Dump tool part Visual Studio 2022 Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe.
