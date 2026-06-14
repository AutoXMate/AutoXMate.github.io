---
id: windows-execution-ieadvpack
namespace: windows:execution:ieadvpack
name: ieadvpack
description: 'INF installer for Internet Explorer. Has much of the same functionality as advpack.dll. Located at: c:\windows\system32\ieadvpack.dll; c:\windows\syswow64\ieadvpack.dll.'
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
- ieadvpack
parameters: []
features: []
execution:
  template: ieadvpack
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified). (Run local or remote script(let) code through INF file specification.)
  command: rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},DefaultInstall_SingleUser,1,
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (DefaultInstall section implied). (Run local or remote script(let) code through INF file specification.)
  command: rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},,1,
- description: Launch a DLL payload by calling the RegisterOCX function. (Load a DLL payload.)
  command: rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.dll}
- description: Launch an executable by calling the RegisterOCX function. (Run an executable payload.)
  command: rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.exe}
- description: Launch command line by calling the RegisterOCX function. (Run an executable payload.)
  command: rundll32 ieadvpack.dll, RegisterOCX {CMD}
references:
- label: ''
  url: https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
- label: '991695411902599168'
  url: https://twitter.com/pabraeken/status/991695411902599168
- label: '974472392012689408'
  url: https://twitter.com/0rbz_/status/974472392012689408
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
  package_name: ieadvpack
  commands:
  - choco install ieadvpack
---


# ieadvpack

ieadvpack is a Windows LOLBin. INF installer for Internet Explorer. Has much of the same functionality as advpack.dll. Located at: c:\windows\system32\ieadvpack.dll; c:\windows\syswow64\ieadvpack.dll.
