---
id: windows-execution-register-cimprovider
namespace: windows:execution:register-cimprovider
name: register-cimprovider
description: 'Used to register new wmi providers Located at: C:\Windows\System32\Register-cimprovider.exe; C:\Windows\SysWOW64\Register-cimprovider.exe.'
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
- register-cimprovider
parameters: []
features: []
execution:
  template: register-cimprovider
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load the target .DLL. (Execute code within dll file)
  command: Register-cimprovider -path {PATH_ABSOLUTE:.dll}
references:
- label: '992021361106268161'
  url: https://twitter.com/PhilipTsukerman/status/992021361106268161
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_susp_register_cimprovider.yml
- type: ioc
  description: Register-cimprovider.exe execution and cmdline DLL load may be supsicious
install:
- method: choco
  package_name: register-cimprovider
  commands:
  - choco install register-cimprovider
---


# register-cimprovider

register-cimprovider is a Windows LOLBin. Used to register new wmi providers Located at: C:\Windows\System32\Register-cimprovider.exe; C:\Windows\SysWOW64\Register-cimprovider.exe.
