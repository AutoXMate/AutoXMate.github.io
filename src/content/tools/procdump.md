---
id: windows-execution-procdump
namespace: windows:execution:procdump
name: procdump
description: 'SysInternals Memory Dump Tool Located at: no default.'
author: Alfie Champion (@ajpc500)
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
related_tools:
- Procdump64
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
- procdump
parameters: []
features: []
execution:
  template: procdump
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads the specified DLL where DLL is configured with a 'MiniDumpCallbackRoutine' exported function. Valid process must be provided as dump still created. (Performs execution of unsigned DLL.)
  command: procdump.exe -md {PATH:.dll} explorer.exe
- description: Loads the specified DLL where configured with DLL_PROCESS_ATTACH execution, process argument can be arbitrary. (Performs execution of unsigned DLL.)
  command: procdump.exe -md {PATH:.dll} foobar
references:
- label: 1448588362382778372?s=20
  url: https://twitter.com/ajpc500/status/1448588362382778372?s=20
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/dump_lsass_via_procdump.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- type: ioc
  description: Process creation with given '-md' parameter
- type: ioc
  description: Anomalous child processes of procdump
- type: ioc
  description: Unsigned DLL load via procdump.exe or procdump64.exe
install:
- method: choco
  package_name: procdump
  commands:
  - choco install procdump
---


# procdump

procdump is a Windows LOLBin. SysInternals Memory Dump Tool Located at: no default.
