---
id: windows-execution-infdefaultinstall
namespace: windows:execution:infdefaultinstall
name: infdefaultinstall
description: 'Binary used to perform installation based on content inside inf files Located at: C:\Windows\System32\Infdefaultinstall.exe; C:\Windows\SysWOW64\Infdefaultinstall.exe.'
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
- infdefaultinstall
parameters: []
features: []
execution:
  template: infdefaultinstall
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes SCT script using scrobj.dll from a command in entered into a specially prepared INF file. (Code execution)
  command: InfDefaultInstall.exe {PATH:.inf}
references:
- label: '911997635455852544'
  url: https://twitter.com/KyleHanslovan/status/911997635455852544
- label: ''
  url: https://blog.conscioushacker.io/index.php/2017/10/25/evading-microsofts-autoruns/
- label: ''
  url: https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
install:
- method: choco
  package_name: infdefaultinstall
  commands:
  - choco install infdefaultinstall
---


# infdefaultinstall

infdefaultinstall is a Windows LOLBin. Binary used to perform installation based on content inside inf files Located at: C:\Windows\System32\Infdefaultinstall.exe; C:\Windows\SysWOW64\Infdefaultinstall.exe.
