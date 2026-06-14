---
id: windows-execution-remote
namespace: windows:execution:remote
name: remote
description: 'Debugging tool included with Windows Debugging Tools Located at: C:\Program
  Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe; C:\Program Files (x86)\Windows
  Kits\10\Debuggers\x86\remote.exe.'
author: mr.d0x
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- remote
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- remote
- stealth
execution:
  template: remote
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawns specified executable as a child process of remote.exe (Executes
    a process under a trusted Microsoft signed binary)
  command: Remote.exe /s {PATH:.exe} anythinghere
- description: Spawns specified executable as a child process of remote.exe (Executes
    a process under a trusted Microsoft signed binary)
  command: Remote.exe /s {PATH:.exe} anythinghere
- description: Run a remote file (Executing a remote binary without saving file to
    disk)
  command: Remote.exe /s {PATH_SMB:.exe} anythinghere
references:
- label: ''
  url: https://blog.thecybersecuritytutor.com/Exeuction-AWL-Bypass-Remote-exe-LOLBin/
techniques:
- defense-evasion
- execution
mitre_ids:
- T1127
detections:
- type: ioc
  description: remote.exe process spawns
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml
install:
- method: choco
  package_name: remote
  commands:
  - choco install remote
---

# remote

remote is a Windows LOLBin. Debugging tool included with Windows Debugging Tools Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\remote.exe.
