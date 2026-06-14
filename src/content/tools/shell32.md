---
id: windows-execution-shell32
namespace: windows:execution:shell32
name: shell32
description: 'Windows Shell Common Dll Located at: c:\windows\system32\shell32.dll; c:\windows\syswow64\shell32.dll.'
author: LOLBAS Team
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
- shell32
parameters: []
features: []
execution:
  template: shell32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch a DLL payload by calling the Control_RunDLL function. (Load a DLL payload.)
  command: rundll32.exe shell32.dll,Control_RunDLL {PATH_ABSOLUTE:.dll}
- description: Launch an executable by calling the ShellExec_RunDLL function. (Run an executable payload.)
  command: rundll32.exe shell32.dll,ShellExec_RunDLL {PATH:.exe}
- description: Launch command line by calling the ShellExec_RunDLL function. (Run an executable payload.)
  command: rundll32 SHELL32.DLL,ShellExec_RunDLL {PATH:.exe} {CMD:args}
- description: Load a DLL/CPL by calling undocumented Control_RunDLLNoFallback function. (Load a DLL/CPL payload.)
  command: rundll32.exe shell32.dll,#44 {PATH:.dll}
references:
- label: '885258886428725250'
  url: https://twitter.com/Hexacorn/status/885258886428725250
- label: '991768766898941953'
  url: https://twitter.com/pabraeken/status/991768766898941953
- label: '776574940128485376'
  url: https://twitter.com/mattifestation/status/776574940128485376
- label: '905189665120149506'
  url: https://twitter.com/KyleHanslovan/status/905189665120149506
- label: shell32_dll.html
  url: https://windows10dll.nirsoft.net/shell32_dll.html
- label: ''
  url: https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/rundll32_control_rundll_hunt.yml
install:
- method: choco
  package_name: shell32
  commands:
  - choco install shell32
---


# shell32

shell32 is a Windows LOLBin. Windows Shell Common Dll Located at: c:\windows\system32\shell32.dll; c:\windows\syswow64\shell32.dll.
