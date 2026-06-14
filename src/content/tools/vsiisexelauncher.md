---
id: windows-execution-vsiisexelauncher
namespace: windows:execution:vsiisexelauncher
name: vsiisexelauncher
description: 'Binary will execute specified binary. Part of VS/VScode installation.
  Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Web
  Tools\ProjectSystem\VSIISExeLauncher.exe.'
author: timwhite
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
- vsiisexelauncher
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: vsiisexelauncher
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: The above binary will execute other binary. (Execute any binary with
    given arguments.)
  command: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
references:
- label: timwhitez
  url: https://github.com/timwhitez
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml
- type: ioc
  description: VSIISExeLauncher.exe spawned an unknown process
install:
- method: choco
  package_name: vsiisexelauncher
  commands:
  - choco install vsiisexelauncher
---

# vsiisexelauncher

vsiisexelauncher is a Windows LOLBin. Binary will execute specified binary. Part of VS/VScode installation. Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Web Tools\ProjectSystem\VSIISExeLauncher.exe.
