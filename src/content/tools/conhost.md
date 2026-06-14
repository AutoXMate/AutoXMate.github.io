---
id: windows-execution-conhost
namespace: windows:execution:conhost
name: conhost
description: 'Console Window host Located at: c:\windows\system32\conhost.exe.'
author: Wietze Beukema
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
- conhost
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: conhost
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute a command line with conhost.exe as parent process (Use conhost.exe
    as a proxy binary to evade defensive counter-measures)
  command: conhost.exe {CMD}
- description: Execute a command line with conhost.exe as parent process (Specify
    --headless parameter to hide child process window (if applicable))
  command: conhost.exe --headless {CMD}
references:
- label: ''
  url: https://www.hexacorn.com/blog/2020/05/25/how-to-con-your-host/
- label: '1511397781159751680'
  url: https://twitter.com/Wietze/status/1511397781159751680
- label: '1559410767564181504'
  url: https://twitter.com/embee_research/status/1559410767564181504
- label: '1561683123816972288'
  url: https://twitter.com/ankit_anubhav/status/1561683123816972288
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: ioc
  description: conhost.exe spawning unexpected processes
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml
install:
- method: choco
  package_name: conhost
  commands:
  - choco install conhost
---

# conhost

conhost is a Windows LOLBin. Console Window host Located at: c:\windows\system32\conhost.exe.
