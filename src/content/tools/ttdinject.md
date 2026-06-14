---
id: windows-execution-ttdinject
namespace: windows:execution:ttdinject
name: ttdinject
description: 'Used by Windows 1809 and newer to Debug Time Travel (Underlying call
  of tttracer.exe) Located at: C:\Windows\System32\ttdinject.exe; C:\Windows\Syswow64\ttdinject.exe.'
author: Maxime Nadeau
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
- ttdinject
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: ttdinject
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute a program using ttdinject.exe. Requires administrator privileges.
    A log file will be created in tmp.run. The log file can be changed, but the length
    (7) has to be updated. (Spawn process using other binary)
  command: TTDInject.exe /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /Launch "{PATH:.exe}"
- description: Execute a program using ttdinject.exe. Requires administrator privileges.
    A log file will be created in tmp.run. The log file can be changed, but the length
    (7) has to be updated. (Spawn process using other binary)
  command: ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run
    0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}"
references:
- label: '1196333160470138880'
  url: https://twitter.com/Oddvarmoe/status/1196333160470138880
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/7ea6ed3db65e0bd812b051d9bb4fffd27c4c4d0a/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml
- type: ioc
  description: Parent child relationship. Ttdinject.exe parent for executed command
- type: ioc
  description: Multiple queries made to the IFEO registry key of an untrusted executable
    (Ex. "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\payload.exe")
    from the ttdinject.exe process
install:
- method: choco
  package_name: ttdinject
  commands:
  - choco install ttdinject
---

# ttdinject

ttdinject is a Windows LOLBin. Used by Windows 1809 and newer to Debug Time Travel (Underlying call of tttracer.exe) Located at: C:\Windows\System32\ttdinject.exe; C:\Windows\Syswow64\ttdinject.exe.
