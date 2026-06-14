---
id: windows-execution-mftrace
namespace: windows:execution:mftrace
name: mftrace
description: 'Trace log generation tool for Media Foundation Tools. Located at: C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x64\mftrace.exe; C:\Program Files (x86)\Windows Kits\10\bin\x86\mftrace.exe.'
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
- mftrace
parameters: []
features: []
execution:
  template: mftrace
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch specified executable as a subprocess of Mftrace.exe. (Local execution of cmd.exe as a subprocess of Mftrace.exe.)
  command: Mftrace.exe {PATH:.exe}
references:
- label: '988911181422186496'
  url: https://twitter.com/0rbz_/status/988911181422186496
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_mftrace.yml
install:
- method: choco
  package_name: mftrace
  commands:
  - choco install mftrace
---


# mftrace

mftrace is a Windows LOLBin. Trace log generation tool for Media Foundation Tools. Located at: C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x64\mftrace.exe; C:\Program Files (x86)\Windows Kits\10\bin\x86\mftrace.exe.
