---
id: windows-execution-launch-vsdevshell
namespace: windows:execution:launch-vsdevshell
name: launch-vsdevshell
description: 'Locates and imports a Developer PowerShell module and calls the Enter-VsDevShell cmdlet Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1; C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1.'
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
- launch-vsdevshell
parameters: []
features: []
execution:
  template: launch-vsdevshell
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute binaries from the context of the signed script using the "VsWherePath" flag. (Proxy execution)
  command: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsWherePath {PATH_ABSOLUTE:.exe}
- description: Execute binaries and commands from the context of the signed script using the "VsInstallationPath" flag. (Proxy execution)
  command: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;"
references:
- label: '1535981653239255040'
  url: https://twitter.com/nas_bench/status/1535981653239255040
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml
install:
- method: choco
  package_name: launch-vsdevshell
  commands:
  - choco install launch-vsdevshell
---


# launch-vsdevshell

launch-vsdevshell is a Windows LOLBin. Locates and imports a Developer PowerShell module and calls the Enter-VsDevShell cmdlet Located at: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1; C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1.
