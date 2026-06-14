---
id: windows-execution-wab
namespace: windows:execution:wab
name: wab
description: 'Windows address book manager Located at: C:\Program Files\Windows Mail\wab.exe;
  C:\Program Files (x86)\Windows Mail\wab.exe.'
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
- wab
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: wab
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Change HKLM\Software\Microsoft\WAB\DLLPath and execute DLL of choice
    (Execute dll file. Bypass defensive counter measures)
  command: wab.exe
references:
- label: '991447379864932352'
  url: https://twitter.com/Hexacorn/status/991447379864932352
- label: ''
  url: http://www.hexacorn.com/blog/2018/05/01/wab-exe-as-a-lolbin/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml
- type: ioc
  description: WAB.exe should normally never be used
install:
- method: choco
  package_name: wab
  commands:
  - choco install wab
---

# wab

wab is a Windows LOLBin. Windows address book manager Located at: C:\Program Files\Windows Mail\wab.exe; C:\Program Files (x86)\Windows Mail\wab.exe.
