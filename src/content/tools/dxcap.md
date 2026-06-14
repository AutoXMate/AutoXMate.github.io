---
id: windows-execution-dxcap
namespace: windows:execution:dxcap
name: dxcap
description: 'DirectX diagnostics/debugger included with Visual Studio. Located at:
  C:\Windows\System32\dxcap.exe; C:\Windows\SysWOW64\dxcap.exe.'
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
- dxcap
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: dxcap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch specified executable as a subprocess of dxcap.exe. Note that
    you should have write permissions in the current working directory for the command
    to succeed; alternatively, add '-file c:\path\to\writable\location.ext' as first
    argument. (Local execution of a process as a subprocess of dxcap.exe)
  command: Dxcap.exe -c {PATH_ABSOLUTE:.exe}
- description: Once executed, `dxcap.exe` will execute `xperf.exe` in the same folder.
    Thus, if `dxcap.exe` is copied to a folder and an arbitrary executable is renamed
    to `xperf.exe`, `dxcap.exe` will spawn it. (Execute an arbitrary executable via
    trusted system executable.)
  command: dxcap.exe -usage
references:
- label: '992008180904419328'
  url: https://twitter.com/harr0ey/status/992008180904419328
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_dxcap.yml
- type: ioc
  description: dxcap.exe executing from outside of System32/SysWOW64
- type: ioc
  description: dxcap.exe spawning Xperf.exe
- type: ioc
  description: Xperf.exe executing from unusual directories (if not running from ADK
    path)
install:
- method: choco
  package_name: dxcap
  commands:
  - choco install dxcap
---

# dxcap

dxcap is a Windows LOLBin. DirectX diagnostics/debugger included with Visual Studio. Located at: C:\Windows\System32\dxcap.exe; C:\Windows\SysWOW64\dxcap.exe.
