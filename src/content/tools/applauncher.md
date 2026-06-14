---
id: windows-execution-applauncher
namespace: windows:execution:applauncher
name: applauncher
description: 'User Experience Virtualization tool that launches applications under monitoring to capture and synchronize user settings. Located at: C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe; C:\Program Files (x86)\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe.'
author: Avihay Eldad
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
- applauncher
parameters: []
features: []
execution:
  template: applauncher
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launches an executable via User Experience Virtualization tool. (Executes an executable under a trusted, Microsoft signed binary.)
  command: AppLauncher.exe {PATH_ABSOLUTE:.exe}
references:
- label: uev-getting-started
  url: https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/ue-v/uev-getting-started
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: applauncher
  commands:
  - choco install applauncher
---


# applauncher

applauncher is a Windows LOLBin. User Experience Virtualization tool that launches applications under monitoring to capture and synchronize user settings. Located at: C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe; C:\Program Files (x86)\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe.
