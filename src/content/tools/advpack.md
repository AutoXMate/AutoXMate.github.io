---
id: windows-execution-advpack
namespace: windows:execution:advpack
name: advpack
description: 'Utility for installing software and drivers with rundll32.exe Located
  at: c:\windows\system32\advpack.dll; c:\windows\syswow64\advpack.dll.'
author: LOLBAS Team
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- advpack
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
- stealth
execution:
  template: advpack
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll
    in the .inf file by calling an information file directive (section name specified).
    (Run local or remote script(let) code through INF file specification.)
  command: rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},DefaultInstall_SingleUser,1,
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll
    in the .inf file by calling an information file directive (DefaultInstall section
    implied). (Run local or remote script(let) code through INF file specification.)
  command: rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},,1,
- description: Launch a DLL payload by calling the RegisterOCX function. (Load a DLL
    payload.)
  command: rundll32.exe advpack.dll,RegisterOCX {PATH:.dll}
- description: Launch an executable by calling the RegisterOCX function. (Run an executable
    payload.)
  command: rundll32.exe advpack.dll,RegisterOCX {PATH:.exe}
- description: Launch command line by calling the RegisterOCX function. (Run an executable
    payload.)
  command: rundll32 advpack.dll, RegisterOCX {CMD}
references:
- label: ''
  url: https://bohops.com/2018/02/26/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence/
- label: '967859147977850880'
  url: https://twitter.com/ItsReallyNick/status/967859147977850880
- label: '974497123101179904'
  url: https://twitter.com/bohops/status/974497123101179904
- label: '977848311603380224'
  url: https://twitter.com/moriarty_meng/status/977848311603380224
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml
install:
- method: choco
  package_name: advpack
  commands:
  - choco install advpack
---

# advpack

advpack is a Windows LOLBin. Utility for installing software and drivers with rundll32.exe Located at: c:\windows\system32\advpack.dll; c:\windows\syswow64\advpack.dll.
