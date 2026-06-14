---
id: windows-execution-cl-invocation
namespace: windows:execution:cl-invocation
name: cl-invocation
description: 'Aero diagnostics script Located at: C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1; C:\Windows\diagnostics\system\Audio\CL_Invocation.ps1; C:\Windows\diagnostics\system\WindowsUpdate\CL_Invocation.ps1.'
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
- cl-invocation
parameters: []
features: []
execution:
  template: cl-invocation
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Import the PowerShell Diagnostic CL_Invocation script and call SyncInvoke to launch an executable. (Proxy execution)
  command: . C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1   \nSyncInvoke {CMD}
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_cl_invocation.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_cl_invocation_lolscript.yml
install:
- method: choco
  package_name: cl-invocation
  commands:
  - choco install cl-invocation
---


# cl-invocation

cl-invocation is a Windows LOLBin. Aero diagnostics script Located at: C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1; C:\Windows\diagnostics\system\Audio\CL_Invocation.ps1; C:\Windows\diagnostics\system\WindowsUpdate\CL_Invocation.ps1.
