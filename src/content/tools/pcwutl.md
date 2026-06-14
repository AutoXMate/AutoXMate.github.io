---
id: windows-execution-pcwutl
namespace: windows:execution:pcwutl
name: pcwutl
description: 'Microsoft HTML Viewer Located at: c:\windows\system32\pcwutl.dll; c:\windows\syswow64\pcwutl.dll.'
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
- pcwutl
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: pcwutl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch executable by calling the LaunchApplication function. (Launch
    an executable.)
  command: rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
references:
- label: '989617817849876488'
  url: https://twitter.com/harr0ey/status/989617817849876488
- label: pcwutl_dll.html
  url: https://windows10dll.nirsoft.net/pcwutl_dll.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
detections:
- type: other
  url: https://redcanary.com/threat-detection-report/techniques/rundll32/
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
install:
- method: choco
  package_name: pcwutl
  commands:
  - choco install pcwutl
---

# pcwutl

pcwutl is a Windows LOLBin. Microsoft HTML Viewer Located at: c:\windows\system32\pcwutl.dll; c:\windows\syswow64\pcwutl.dll.
