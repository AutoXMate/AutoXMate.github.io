---
id: windows-execution-syssetup
namespace: windows:execution:syssetup
name: syssetup
description: 'Windows NT System Setup Located at: c:\windows\system32\syssetup.dll; c:\windows\syswow64\syssetup.dll.'
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
- syssetup
parameters: []
features: []
execution:
  template: syssetup
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified). (Run local or remote script(let) code through INF file specification (Note May pop an error window).)
  command: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
- description: Launch an executable file via the SetupInfObjectInstallAction function and .inf file section directive. (Load an executable payload.)
  command: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
references:
- label: '994392481927258113'
  url: https://twitter.com/pabraeken/status/994392481927258113
- label: '975350238184697857'
  url: https://twitter.com/harr0ey/status/975350238184697857
- label: '975549525938135040'
  url: https://twitter.com/bohops/status/975549525938135040
- label: syssetup_dll.html
  url: https://windows10dll.nirsoft.net/syssetup_dll.html
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___syssetup.yml
install:
- method: choco
  package_name: syssetup
  commands:
  - choco install syssetup
---


# syssetup

syssetup is a Windows LOLBin. Windows NT System Setup Located at: c:\windows\system32\syssetup.dll; c:\windows\syswow64\syssetup.dll.
