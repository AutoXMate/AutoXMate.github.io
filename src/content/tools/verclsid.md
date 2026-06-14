---
id: windows-execution-verclsid
namespace: windows:execution:verclsid
name: verclsid
description: 'Used to verify a COM object before it is instantiated by Windows Explorer
  Located at: C:\Windows\System32\verclsid.exe; C:\Windows\SysWOW64\verclsid.exe.'
author: '@bohops'
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
- verclsid
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: verclsid
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Used to verify a COM object before it is instantiated by Windows Explorer
    (Run a COM object created in registry to evade defensive counter measures)
  command: verclsid.exe /S /C {CLSID}
references:
- label: 0598b60112eaafe6d07789f7964290d5
  url: https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- label: ''
  url: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.012
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/verclsid_clsid_execution.yml
install:
- method: choco
  package_name: verclsid
  commands:
  - choco install verclsid
---

# verclsid

verclsid is a Windows LOLBin. Used to verify a COM object before it is instantiated by Windows Explorer Located at: C:\Windows\System32\verclsid.exe; C:\Windows\SysWOW64\verclsid.exe.
