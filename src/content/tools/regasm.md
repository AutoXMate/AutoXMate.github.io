---
id: windows-execution-regasm
namespace: windows:execution:regasm
name: regasm
description: 'Part of .NET Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe;
  C:\Windows\Microsoft.NET\Framework64\v2.0.50727\regasm.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\regasm.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- regasm
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: regasm
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads the target .NET DLL file and executes the RegisterClass function.
    (Execute code and bypass Application whitelisting)
  command: regasm.exe {PATH:.dll}
- description: Loads the target .DLL file and executes the UnRegisterClass function.
    (Execute code and bypass Application whitelisting)
  command: regasm.exe /U {PATH:.dll}
references:
- label: ''
  url: https://pentestlab.blog/2017/05/19/applocker-bypass-regasm-and-regsvcs/
- label: ''
  url: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- label: T1218.009.md
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.md
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.009
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_regasm.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bc93e670f5dcb24e96fbe3664d6bcad92df5acad/docs/_stories/suspicious_regsvcs_regasm_activity.md
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_regasm_with_network_connection.yml
- type: ioc
  description: regasm.exe executing dll file
install:
- method: choco
  package_name: regasm
  commands:
  - choco install regasm
---

# regasm

regasm is a Windows LOLBin. Part of .NET Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\regasm.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\regasm.exe.
