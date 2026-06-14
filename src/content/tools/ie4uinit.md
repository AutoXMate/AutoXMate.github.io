---
id: windows-execution-ie4uinit
namespace: windows:execution:ie4uinit
name: ie4uinit
description: 'Executes commands from a specially prepared ie4uinit.inf file. Located
  at: c:\windows\system32\ie4uinit.exe; c:\windows\sysWOW64\ie4uinit.exe; c:\windows\system32\ieuinit.inf.'
author: Oddvar Moe
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
- ie4uinit
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: ie4uinit
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes commands from a specially prepared ie4uinit.inf file. (Get
    code execution by copy files to another location)
  command: ie4uinit.exe -BaseSettings
references:
- label: ''
  url: https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: ie4uinit.exe copied outside of %windir%
- type: ioc
  description: ie4uinit.exe loading an inf file (ieuinit.inf) from outside %windir%
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml
install:
- method: choco
  package_name: ie4uinit
  commands:
  - choco install ie4uinit
---

# ie4uinit

ie4uinit is a Windows LOLBin. Executes commands from a specially prepared ie4uinit.inf file. Located at: c:\windows\system32\ie4uinit.exe; c:\windows\sysWOW64\ie4uinit.exe; c:\windows\system32\ieuinit.inf.
