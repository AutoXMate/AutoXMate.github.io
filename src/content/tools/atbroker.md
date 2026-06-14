---
id: windows-execution-atbroker
namespace: windows:execution:atbroker
name: atbroker
description: 'Helper binary for Assistive Technology (AT) Located at: C:\Windows\System32\Atbroker.exe; C:\Windows\SysWOW64\Atbroker.exe.'
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
- atbroker
parameters: []
features: []
execution:
  template: atbroker
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Start a registered Assistive Technology (AT). (Executes code defined in registry for a new AT. Modifications must be made to the system registry to either register or modify an existing Assistive Technology (AT) service entry.)
  command: ATBroker.exe /start malware
references:
- label: ''
  url: http://www.hexacorn.com/blog/2016/07/22/beyond-good-ol-run-key-part-42/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_atbroker.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml
- type: ioc
  description: Changes to HKCU\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
- type: ioc
  description: Changes to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
- type: ioc
  description: Unknown AT starting C:\Windows\System32\ATBroker.exe /start malware
install:
- method: choco
  package_name: atbroker
  commands:
  - choco install atbroker
---


# atbroker

atbroker is a Windows LOLBin. Helper binary for Assistive Technology (AT) Located at: C:\Windows\System32\Atbroker.exe; C:\Windows\SysWOW64\Atbroker.exe.
