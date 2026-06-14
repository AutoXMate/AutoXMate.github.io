---
id: windows-execution-ieframe
namespace: windows:execution:ieframe
name: ieframe
description: 'Internet Browser DLL for translating HTML code. Located at: c:\windows\system32\ieframe.dll;
  c:\windows\syswow64\ieframe.dll.'
author: LOLBAS Team
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
- ieframe
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: ieframe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch an executable payload via proxy through a(n) URL (information)
    file by calling OpenURL. (Load an executable payload by calling a .url file with
    or without quotes. The .url file extension can be renamed.)
  command: rundll32.exe ieframe.dll,OpenURL {PATH_ABSOLUTE:.url}
references:
- label: ''
  url: http://www.hexacorn.com/blog/2018/03/15/running-programs-via-proxy-jumping-on-a-edr-bypass-trampoline-part-5/
- label: ''
  url: https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/
- label: '997690405092290561'
  url: https://twitter.com/bohops/status/997690405092290561
- label: ieframe_dll.html
  url: https://windows10dll.nirsoft.net/ieframe_dll.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
install:
- method: choco
  package_name: ieframe
  commands:
  - choco install ieframe
---

# ieframe

ieframe is a Windows LOLBin. Internet Browser DLL for translating HTML code. Located at: c:\windows\system32\ieframe.dll; c:\windows\syswow64\ieframe.dll.
