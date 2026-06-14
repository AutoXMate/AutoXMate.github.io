---
id: windows-execution-vsdiagnostics
namespace: windows:execution:vsdiagnostics
name: vsdiagnostics
description: 'Command-line tool used for performing diagnostics. Located at: C:\Program
  Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe.'
author: Bobby Cooke
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
- vsdiagnostics
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: vsdiagnostics
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Starts a collection session with sessionID 1 and calls kernelbase.CreateProcessW
    to launch specified executable. (Proxy execution of binary)
  command: VSDiagnostics.exe start 1 /launch:{PATH:.exe}
- description: Starts a collection session with sessionID 2 and calls kernelbase.CreateProcessW
    to launch specified executable. Arguments specified in launchArgs are passed to
    CreateProcessW. (Proxy execution of binary with arguments)
  command: VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}"
references:
- label: '1679200664013135872'
  url: https://twitter.com/0xBoku/status/1679200664013135872
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/tsale/Sigma_rules/blob/d5b4a09418edfeeb3a2d654f556d5bca82003cd7/LOL_BINs/VSDiagnostics_LoLBin.yml
install:
- method: choco
  package_name: vsdiagnostics
  commands:
  - choco install vsdiagnostics
---

# vsdiagnostics

vsdiagnostics is a Windows LOLBin. Command-line tool used for performing diagnostics. Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe.
