---
id: windows-execution-devtoolslauncher
namespace: windows:execution:devtoolslauncher
name: devtoolslauncher
description: 'Binary will execute specified binary. Part of VS/VScode installation.
  Located at: c:\windows\system32\devtoolslauncher.exe.'
author: felamos
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
- devtoolslauncher
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: devtoolslauncher
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: The above binary will execute other binary. (Execute any binary with
    given arguments and it will call `developertoolssvc.exe`. `developertoolssvc`
    is actually executing the binary.)
  command: devtoolslauncher.exe LaunchForDeploy {PATH_ABSOLUTE:.exe} "{CMD:args}"
    test
- description: The above binary will execute other binary. (Execute any binary with
    given arguments.)
  command: devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test
references:
- label: '1179811992841797632'
  url: https://twitter.com/_felamos/status/1179811992841797632
- label: details
  url: https://www.virustotal.com/gui/file/84877a507af8b70c145777a87eaf28a8327c50a1563fe650f34572bef8a42ff6/details
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml
- type: ioc
  description: DeveloperToolsSvc.exe spawned an unknown process
install:
- method: choco
  package_name: devtoolslauncher
  commands:
  - choco install devtoolslauncher
---

# devtoolslauncher

devtoolslauncher is a Windows LOLBin. Binary will execute specified binary. Part of VS/VScode installation. Located at: c:\windows\system32\devtoolslauncher.exe.
