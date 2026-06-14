---
id: windows-execution-openconsole
namespace: windows:execution:openconsole
name: openconsole
description: 'Console Window host for Windows Terminal Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe; C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os86\OpenConsole.exe; C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe.'
author: Nasreddine Bencherchali
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
- openconsole
parameters: []
features: []
execution:
  template: openconsole
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute specified process with OpenConsole.exe as parent process (Use OpenConsole.exe as a proxy binary to evade defensive counter-measures)
  command: OpenConsole.exe {PATH:.exe}
references:
- label: '1537563834478645252'
  url: https://twitter.com/nas_bench/status/1537563834478645252
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: ioc
  description: OpenConsole.exe spawning unexpected processes
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/9e0ef7251b075f15e7abafbbec16d3230c5fa477/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml
install:
- method: choco
  package_name: openconsole
  commands:
  - choco install openconsole
---


# openconsole

openconsole is a Windows LOLBin. Console Window host for Windows Terminal Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe; C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os86\OpenConsole.exe; C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe.
