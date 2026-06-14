---
id: windows-tamper-fsutil
namespace: windows:tamper:fsutil
name: fsutil
description: 'File System Utility Located at: C:\Windows\System32\fsutil.exe; C:\Windows\SysWOW64\fsutil.exe.'
author: Elliot Killick
version: 1.0.0
capabilities:
- security.defense-evasion.tamper
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
  - filesystem_write
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
- fsutil
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: fsutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Zero out a file (Can be used to forensically erase a file)
  command: fsutil.exe file setZeroData offset=0 length=9999999999 {PATH_ABSOLUTE}
- description: Delete the USN journal volume to hide file creation activity (Can be
    used to hide file creation activity)
  command: 'fsutil.exe usn deletejournal /d c:'
- description: Executes a pre-planted binary named netsh.exe from the current directory.
    (Spawn a pre-planted executable from fsutil.exe.)
  command: fsutil.exe trace decode
references:
- label: '1720724516324704404'
  url: https://twitter.com/0gtweet/status/1720724516324704404
techniques:
- defense-evasion
- impact
- execution
mitre_ids:
- T1485
- T1218
detections:
- type: ioc
  description: fsutil.exe should not be run on a normal workstation
- type: ioc
  description: file setZeroData (not case-sensitive) in the process arguments
- type: ioc
  description: Sysmon Event ID 1
- type: ioc
  description: Execution of process fsutil.exe with trace decode could be suspicious
- type: ioc
  description: Non-Windows netsh.exe execution
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_susp_fsutil_usage.yml
install:
- method: choco
  package_name: fsutil
  commands:
  - choco install fsutil
---

# fsutil

fsutil is a Windows LOLBin. File System Utility Located at: C:\Windows\System32\fsutil.exe; C:\Windows\SysWOW64\fsutil.exe.
