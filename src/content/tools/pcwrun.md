---
id: windows-execution-pcwrun
namespace: windows:execution:pcwrun
name: pcwrun
description: 'Program Compatibility Wizard Located at: C:\Windows\System32\pcwrun.exe.'
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
- pcwrun
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: pcwrun
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Open the target .EXE file with the Program Compatibility Wizard. (Proxy
    execution of binary)
  command: Pcwrun.exe {PATH_ABSOLUTE:.exe}
- description: Leverage the MSDT follina vulnerability through Pcwrun to execute arbitrary
    commands and binaries. Note that this specific technique will not work on a patched
    system with the June 2022 Windows Security update. (Proxy execution of binary)
  command: Pcwrun.exe /../../$(calc).exe
references:
- label: '991335019833708544'
  url: https://twitter.com/pabraeken/status/991335019833708544
- label: '1535663791362519040'
  url: https://twitter.com/nas_bench/status/1535663791362519040
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml
install:
- method: choco
  package_name: pcwrun
  commands:
  - choco install pcwrun
---

# pcwrun

pcwrun is a Windows LOLBin. Program Compatibility Wizard Located at: C:\Windows\System32\pcwrun.exe.
