---
id: windows-execution-setupapi
namespace: windows:execution:setupapi
name: setupapi
description: 'Windows Setup Application Programming Interface Located at: c:\windows\system32\setupapi.dll; c:\windows\syswow64\setupapi.dll.'
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
- setupapi
parameters: []
features: []
execution:
  template: setupapi
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified). (Run local or remote script(let) code through INF file specification.)
  command: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
- description: Launch an executable file via the InstallHinfSection function and .inf file section directive. (Load an executable payload.)
  command: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
references:
- label: evading-autoruns
  url: https://github.com/huntresslabs/evading-autoruns
- label: '994742106852941825'
  url: https://twitter.com/pabraeken/status/994742106852941825
- label: setupapi_dll.html
  url: https://windows10dll.nirsoft.net/setupapi_dll.html
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___setupapi.yml
install:
- method: choco
  package_name: setupapi
  commands:
  - choco install setupapi
---


# setupapi

setupapi is a Windows LOLBin. Windows Setup Application Programming Interface Located at: c:\windows\system32\setupapi.dll; c:\windows\syswow64\setupapi.dll.
