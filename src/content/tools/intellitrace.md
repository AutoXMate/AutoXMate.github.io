---
id: windows-execution-intellitrace
namespace: windows:execution:intellitrace
name: intellitrace
description: 'Visual Studio command-line tool for collecting and managing diagnostic trace files. Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe; C:\Program Files (x86)\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe.'
author: Avihay Eldad
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
- intellitrace
parameters: []
features: []
execution:
  template: intellitrace
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launches an executable via Visual Studio command line utility. (Executes an executable under a trusted microsoft signed binary.)
  command: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
references:
- label: intellitrace
  url: https://learn.microsoft.com/en-us/visualstudio/debugger/intellitrace
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: intellitrace
  commands:
  - choco install intellitrace
---


# intellitrace

intellitrace is a Windows LOLBin. Visual Studio command-line tool for collecting and managing diagnostic trace files. Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe; C:\Program Files (x86)\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe.
