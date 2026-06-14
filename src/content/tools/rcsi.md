---
id: windows-execution-rcsi
namespace: windows:execution:rcsi
name: rcsi
description: 'Non-Interactive command line inerface included with Visual Studio. Located
  at: no default.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- security.defense-evasion.bypass
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
- rcsi
parameters: []
features:
- interactive
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: rcsi
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use embedded C# within the csx script to execute the code. (Local execution
    of arbitrary C# code stored in local CSX file.)
  command: rcsi.exe {PATH:.csx}
- description: Use embedded C# within the csx script to execute the code. (Local execution
    of arbitrary C# code stored in local CSX file.)
  command: rcsi.exe {PATH:.csx}
references:
- label: ''
  url: https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
install:
- method: choco
  package_name: rcsi
  commands:
  - choco install rcsi
---

# rcsi

rcsi is a Windows LOLBin. Non-Interactive command line inerface included with Visual Studio. Located at: no default.
