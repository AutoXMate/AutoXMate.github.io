---
id: windows-execution-cl-mutexverifiers
namespace: windows:execution:cl-mutexverifiers
name: cl-mutexverifiers
description: 'Proxy execution with CL_Mutexverifiers.ps1 Located at: C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1; C:\Windows\diagnostics\system\Audio\CL_Mutexverifiers.ps1; C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1.'
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
- cl-mutexverifiers
parameters: []
features: []
execution:
  template: cl-mutexverifiers
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Import the PowerShell Diagnostic CL_Mutexverifiers script and call runAfterCancelProcess to launch an executable. (Proxy execution)
  command: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1   \nrunAfterCancelProcess {PATH:.ps1}
references:
- label: '995111125447577600'
  url: https://twitter.com/pabraeken/status/995111125447577600
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cl_mutexverifiers.yml
install:
- method: choco
  package_name: cl-mutexverifiers
  commands:
  - choco install cl-mutexverifiers
---


# cl-mutexverifiers

cl-mutexverifiers is a Windows LOLBin. Proxy execution with CL_Mutexverifiers.ps1 Located at: C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1; C:\Windows\diagnostics\system\Audio\CL_Mutexverifiers.ps1; C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1.
