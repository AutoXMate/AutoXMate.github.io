---
id: windows-execution-pcalua
namespace: windows:execution:pcalua
name: pcalua
description: 'Program Compatibility Assistant Located at: C:\Windows\System32\pcalua.exe.'
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
- pcalua
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: pcalua
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Open the target .EXE using the Program Compatibility Assistant. (Proxy
    execution of binary)
  command: pcalua.exe -a {PATH:.exe}
- description: Open the target .DLL file with the Program Compatibilty Assistant.
    (Proxy execution of remote dll file)
  command: pcalua.exe -a {PATH_SMB:.dll}
- description: Open the target .CPL file with the Program Compatibility Assistant.
    (Execution of CPL files)
  command: pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java
references:
- label: '912659279806640128'
  url: https://twitter.com/KyleHanslovan/status/912659279806640128
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml
install:
- method: choco
  package_name: pcalua
  commands:
  - choco install pcalua
---

# pcalua

pcalua is a Windows LOLBin. Program Compatibility Assistant Located at: C:\Windows\System32\pcalua.exe.
