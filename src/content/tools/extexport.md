---
id: windows-execution-extexport
namespace: windows:execution:extexport
name: extexport
description: 'Load a DLL located in the c:\test folder with a specific name. Located at: C:\Program Files\Internet Explorer\Extexport.exe; C:\Program Files (x86)\Internet Explorer\Extexport.exe.'
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
- extexport
parameters: []
features: []
execution:
  template: extexport
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load a DLL located in the specified folder with one of the following names mozcrt19.dll, mozsqlite3.dll, or sqlite.dll. (Execute dll file)
  command: Extexport.exe {PATH_ABSOLUTE:folder} foo bar
references:
- label: ''
  url: http://www.hexacorn.com/blog/2018/04/24/extexport-yet-another-lolbin/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extexport.yml
- type: ioc
  description: Extexport.exe loads dll and is execute from other folder the original path
install:
- method: choco
  package_name: extexport
  commands:
  - choco install extexport
---


# extexport

extexport is a Windows LOLBin. Load a DLL located in the c:\test folder with a specific name. Located at: C:\Program Files\Internet Explorer\Extexport.exe; C:\Program Files (x86)\Internet Explorer\Extexport.exe.
