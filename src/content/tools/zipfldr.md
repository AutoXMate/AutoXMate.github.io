---
id: windows-execution-zipfldr
namespace: windows:execution:zipfldr
name: zipfldr
description: 'Compressed Folder library Located at: c:\windows\system32\zipfldr.dll;
  c:\windows\syswow64\zipfldr.dll.'
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
- zipfldr
parameters: []
features:
- compression
- file-system
- pipes-stdin
- pipes-stdout
execution:
  template: zipfldr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch an executable payload by calling RouteTheCall. (Launch an executable.)
  command: rundll32.exe zipfldr.dll,RouteTheCall {PATH:.exe}
- description: Launch an executable payload by calling RouteTheCall (obfuscated).
    (Launch an executable.)
  command: rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
references:
- label: '977848311603380224'
  url: https://twitter.com/moriarty_meng/status/977848311603380224
- label: '997896811904929792'
  url: https://twitter.com/bohops/status/997896811904929792
- label: zipfldr_dll.html
  url: https://windows10dll.nirsoft.net/zipfldr_dll.html
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
  package_name: zipfldr
  commands:
  - choco install zipfldr
---

# zipfldr

zipfldr is a Windows LOLBin. Compressed Folder library Located at: c:\windows\system32\zipfldr.dll; c:\windows\syswow64\zipfldr.dll.
