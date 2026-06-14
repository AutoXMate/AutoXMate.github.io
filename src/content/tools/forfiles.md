---
id: windows-execution-forfiles
namespace: windows:execution:forfiles
name: forfiles
description: 'Selects and executes a command on a file or set of files. This command
  is useful for batch processing. Located at: C:\Windows\System32\forfiles.exe; C:\Windows\SysWOW64\forfiles.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- system.file.alternate-data-stream
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
- forfiles
parameters: []
features:
- batch
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- streaming
execution:
  template: forfiles
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes specified command since there is a match for notepad.exe in
    the c:\windows\System32 folder. (Use forfiles to start a new process to evade
    defensive counter measures)
  command: forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}"
- description: Executes the evil.exe Alternate Data Stream (AD) since there is a match
    for notepad.exe in the c:\windows\system32 folder. (Use forfiles to start a new
    process from a binary hidden in an alternate data stream)
  command: forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe"
references:
- label: '896049052642533376'
  url: https://twitter.com/vector_sec/status/896049052642533376
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: ''
  url: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_forfiles.yml
install:
- method: choco
  package_name: forfiles
  commands:
  - choco install forfiles
---

# forfiles

forfiles is a Windows LOLBin. Selects and executes a command on a file or set of files. This command is useful for batch processing. Located at: C:\Windows\System32\forfiles.exe; C:\Windows\SysWOW64\forfiles.exe.
