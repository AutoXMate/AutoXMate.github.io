---
id: windows-execution-customshellhost
namespace: windows:execution:customshellhost
name: customshellhost
description: 'A host process that is used by custom shells when using Windows in Kiosk mode. Located at: C:\Windows\System32\CustomShellHost.exe.'
author: Wietze Beukema
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
- customshellhost
parameters: []
features: []
execution:
  template: customshellhost
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes explorer.exe (with command-line argument /NoShellRegistrationCheck) if present in the current working folder. (Can be used to evade defensive counter-measures)
  command: CustomShellHost.exe
references:
- label: '1381353520088113154'
  url: https://twitter.com/YoSignals/status/1381353520088113154
- label: kiosk-shelllauncher
  url: https://docs.microsoft.com/en-us/windows/configuration/kiosk-shelllauncher
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: CustomShellHost.exe is unlikely to run on normal workstations
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_customshellhost.yml
install:
- method: choco
  package_name: customshellhost
  commands:
  - choco install customshellhost
---


# customshellhost

customshellhost is a Windows LOLBin. A host process that is used by custom shells when using Windows in Kiosk mode. Located at: C:\Windows\System32\CustomShellHost.exe.
