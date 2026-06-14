---
id: windows-execution-explorer
namespace: windows:execution:explorer
name: explorer
description: 'Binary used for managing files and system components within Windows
  Located at: C:\Windows\explorer.exe; C:\Windows\SysWOW64\explorer.exe.'
author: Jai Minton
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
- explorer
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: explorer
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute specified .exe with the parent process spawning from a new
    instance of explorer.exe (Performs execution of specified file with explorer parent
    process breaking the process tree, can be used for defense evasion.)
  command: explorer.exe /root,"{PATH_ABSOLUTE:.exe}"
- description: Execute notepad.exe with the parent process spawning from a new instance
    of explorer.exe (Performs execution of specified file with explorer parent process
    breaking the process tree, can be used for defense evasion.)
  command: explorer.exe {PATH_ABSOLUTE:.exe}
references:
- label: 1273597319322058752?s=20
  url: https://twitter.com/CyberRaiju/status/1273597319322058752?s=20
- label: '1276356245541335048'
  url: https://twitter.com/bohops/status/1276356245541335048
- label: '986984122563391488'
  url: https://twitter.com/bohops/status/986984122563391488
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_lolbin_execution.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/f2bc0c685d83db7db395fc3dc4b9729759cd4329/rules/windows/initial_access_via_explorer_suspicious_child_parent_args.toml
- type: ioc
  description: Multiple instances of explorer.exe or explorer.exe using the /root
    command line is suspicious.
install:
- method: choco
  package_name: explorer
  commands:
  - choco install explorer
---

# explorer

explorer is a Windows LOLBin. Binary used for managing files and system components within Windows Located at: C:\Windows\explorer.exe; C:\Windows\SysWOW64\explorer.exe.
