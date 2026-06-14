---
id: windows-execution-scriptrunner
namespace: windows:execution:scriptrunner
name: scriptrunner
description: 'Execute binary through proxy binary to evade defensive counter measures
  Located at: C:\Windows\System32\scriptrunner.exe; C:\Windows\SysWOW64\scriptrunner.exe.'
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
- scriptrunner
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
- remote
- stealth
execution:
  template: scriptrunner
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes executable (Execute binary through proxy binary to evade defensive
    counter measures)
  command: Scriptrunner.exe -appvscript {PATH:.exe}
- description: Executes cmd file from remote server (Execute binary through proxy
    binary from external server to evade defensive counter measures)
  command: ScriptRunner.exe -appvscript {PATH_SMB:.cmd}
references:
- label: '914800377580503040'
  url: https://twitter.com/KyleHanslovan/status/914800377580503040
- label: '914234924655312896'
  url: https://twitter.com/NickTyrer/status/914234924655312896
- label: Code-Execution
  url: https://github.com/MoooKitty/Code-Execution
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml
- type: ioc
  description: Scriptrunner.exe should not be in use unless App-v is deployed
install:
- method: choco
  package_name: scriptrunner
  commands:
  - choco install scriptrunner
---

# scriptrunner

scriptrunner is a Windows LOLBin. Execute binary through proxy binary to evade defensive counter measures Located at: C:\Windows\System32\scriptrunner.exe; C:\Windows\SysWOW64\scriptrunner.exe.
