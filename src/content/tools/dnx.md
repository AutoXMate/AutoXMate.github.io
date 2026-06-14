---
id: windows-execution-dnx
namespace: windows:execution:dnx
name: dnx
description: '.NET Execution environment file included with .NET. Located at: no default.'
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
- dnx
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: dnx
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute C# code located in the specified folder via 'Program.cs' and
    'Project.json' (Note - Requires dependencies) (Local execution of C# project stored
    in consoleapp folder.)
  command: dnx.exe {PATH_ABSOLUTE:folder}
references:
- label: ''
  url: https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dnx.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
install:
- method: choco
  package_name: dnx
  commands:
  - choco install dnx
---

# dnx

dnx is a Windows LOLBin. .NET Execution environment file included with .NET. Located at: no default.
