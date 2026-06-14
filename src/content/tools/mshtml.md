---
id: windows-execution-mshtml
namespace: windows:execution:mshtml
name: mshtml
description: 'Microsoft HTML Viewer Located at: c:\windows\system32\mshtml.dll; c:\windows\syswow64\mshtml.dll.'
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
- mshtml
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: mshtml
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: 'Invoke an HTML Application via mshta.exe (note: pops a security warning
    and a print dialogue box). (Launch an HTA application.)'
  command: rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
references:
- label: '998567549670477824'
  url: https://twitter.com/pabraeken/status/998567549670477824
- label: mshtml_dll.html
  url: https://windows10dll.nirsoft.net/mshtml_dll.html
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
  package_name: mshtml
  commands:
  - choco install mshtml
---

# mshtml

mshtml is a Windows LOLBin. Microsoft HTML Viewer Located at: c:\windows\system32\mshtml.dll; c:\windows\syswow64\mshtml.dll.
