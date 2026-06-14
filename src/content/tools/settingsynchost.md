---
id: windows-execution-settingsynchost
namespace: windows:execution:settingsynchost
name: settingsynchost
description: 'Host Process for Setting Synchronization Located at: C:\Windows\System32\SettingSyncHost.exe;
  C:\Windows\SysWOW64\SettingSyncHost.exe.'
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
- settingsynchost
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: settingsynchost
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute file specified in %COMSPEC% (Can be used to evade defensive
    countermeasures or to hide as a persistence mechanism)
  command: SettingSyncHost -LoadAndRunDiagScript {PATH:.exe}
- description: Execute a batch script in the background (no window ever pops up) which
    can be subverted to running arbitrary programs by setting the current working
    directory to %TMP% and creating files such as reg.bat/reg.exe in that directory
    thereby causing them to execute instead of the ones in C:\Windows\System32. (Can
    be used to evade defensive countermeasures or to hide as a persistence mechanism.
    Additionally, effectively act as a -WindowStyle Hidden option (as there is in
    PowerShell) for any arbitrary batch file.)
  command: SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat}
references:
- label: ''
  url: https://www.hexacorn.com/blog/2020/02/02/settingsynchost-exe-as-a-lolbin/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_settingsynchost.yml
- type: ioc
  description: SettingSyncHost.exe should not be run on a normal workstation
install:
- method: choco
  package_name: settingsynchost
  commands:
  - choco install settingsynchost
---

# settingsynchost

settingsynchost is a Windows LOLBin. Host Process for Setting Synchronization Located at: C:\Windows\System32\SettingSyncHost.exe; C:\Windows\SysWOW64\SettingSyncHost.exe.
