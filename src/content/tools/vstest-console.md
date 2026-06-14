---
id: windows-bypass-vstest-console
namespace: windows:bypass:vstest-console
name: vstest-console
description: 'VSTest.Console.exe is the command-line tool to run tests Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe; C:\Program Files (x86)\Microsoft Visual Studio\2022\TestAgent\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe.'
author: Onat Uzunyayla
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
- vstest-console
parameters: []
features: []
execution:
  template: vstest-console
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: VSTest functionality may allow an adversary to executes their malware by wrapping it as a test method then build it to a .exe or .dll file to be later run by vstest.console.exe. This may both allow AWL bypass or defense bypass in general (Proxy Execution and AWL bypass, Adversaries may run malicious code embedded inside the test methods of crafted dll/exe)
  command: vstest.console.exe {PATH:.dll}
references:
- label: vstest-console-options?view=vs-2022
  url: https://learn.microsoft.com/en-us/visualstudio/test/vstest-console-options?view=vs-2022
techniques:
- defense-evasion
mitre_ids:
- T1127
detections:
- type: ioc
  description: vstest.console.exe spawning unexpected processes
install:
- method: choco
  package_name: vstest-console
  commands:
  - choco install vstest-console
---


# vstest-console

vstest-console is a Windows LOLBin. VSTest.Console.exe is the command-line tool to run tests Located at: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe; C:\Program Files (x86)\Microsoft Visual Studio\2022\TestAgent\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe.
