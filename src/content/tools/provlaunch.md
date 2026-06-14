---
id: windows-execution-provlaunch
namespace: windows:execution:provlaunch
name: provlaunch
description: 'Launcher process Located at: c:\windows\system32\provlaunch.exe.'
author: Grzegorz Tworek
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
- provlaunch
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: provlaunch
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes command defined in the Registry. Requires 3 levels of the
    key structure containing some keywords. Such keys may be created with two reg.exe
    commands, e.g. `reg.exe add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1
    /v altitude /t REG_DWORD /d 0` and `reg add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1\dummy2
    /v Commandline /d calc.exe`. Registry keys are deleted after successful execution.
    (Executes arbitrary command)
  command: provlaunch.exe LOLBin
references:
- label: '1674399582162153472'
  url: https://twitter.com/0gtweet/status/1674399582162153472
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml
- type: ioc
  description: c:\windows\system32\provlaunch.exe executions
- type: ioc
  description: Creation/existence of HKLM\SOFTWARE\Microsoft\Provisioning\Commands
    subkeys
install:
- method: choco
  package_name: provlaunch
  commands:
  - choco install provlaunch
---

# provlaunch

provlaunch is a Windows LOLBin. Launcher process Located at: c:\windows\system32\provlaunch.exe.
