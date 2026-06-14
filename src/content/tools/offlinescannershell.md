---
id: windows-execution-offlinescannershell
namespace: windows:execution:offlinescannershell
name: offlinescannershell
description: 'Windows Defender Offline Shell Located at: C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe.'
author: Elliot Killick
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
- offlinescannershell
parameters: []
features: []
execution:
  template: offlinescannershell
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute mpclient.dll library in the current working directory (Can be used to evade defensive countermeasures or to hide as a persistence mechanism)
  command: OfflineScannerShell
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbas_offlinescannershell.yml
- type: ioc
  description: OfflineScannerShell.exe should not be run on a normal workstation
install:
- method: choco
  package_name: offlinescannershell
  commands:
  - choco install offlinescannershell
---


# offlinescannershell

offlinescannershell is a Windows LOLBin. Windows Defender Offline Shell Located at: C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe.
