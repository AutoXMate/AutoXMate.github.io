---
id: windows-execution-microsoft-workflow-compiler
namespace: windows:execution:microsoft-workflow-compiler
name: microsoft-workflow-compiler
description: 'A utility included with .NET that is capable of compiling and executing
  C# or VB.net code. Located at: C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe.'
author: Conor Richard
version: 1.0.0
capabilities:
- security.execution.command
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
- microsoft-workflow-compiler
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: microsoft-workflow-compiler
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Compile and execute C# or VB.net code in a XOML file referenced in
    the first argument (any extension accepted). (Compile and run code)
  command: Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
- description: Compile and execute C# or VB.net code in a XOML file referenced in
    the test.txt file. (Compile and run code)
  command: Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
- description: Compile and execute C# or VB.net code in a XOML file referenced in
    the test.txt file. (Compile and run code)
  command: Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
references:
- label: '1030445200475185154'
  url: https://twitter.com/mattifestation/status/1030445200475185154
- label: arbitrary-unsigned-code-execution-vector-in-micros
  url: https://posts.specterops.io/arbitrary-unsigned-code-execution-vector-in-microsoft-workflow-compiler-exe-3d9294bc5efb
- label: 3e28d391adbd7fe3e0c722a107a25aba#file-workflowcomp
  url: https://gist.github.com/mattifestation/3e28d391adbd7fe3e0c722a107a25aba#file-workflowcompilerdetectiontests-ps1
- label: 7ba8fc8f724600a9f525714c9cf767fd#file-createcompil
  url: https://gist.github.com/mattifestation/7ba8fc8f724600a9f525714c9cf767fd#file-createcompilerinputxml-ps1
- label: using-c-post-powershell-attacks
  url: https://www.forcepoint.com/blog/security-labs/using-c-post-powershell-attacks
- label: ''
  url: https://www.fortynorthsecurity.com/microsoft-workflow-compiler-exe-veil-and-cobalt-strike/
- label: undetectable-c-c-reverse-shells-fab4c0ec4f15
  url: https://medium.com/@Bank_Security/undetectable-c-c-reverse-shells-fab4c0ec4f15
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_workflow_compiler.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/961a81d4a5cb5c5febec4894d6d812497171a85c/detections/endpoint/suspicious_microsoft_workflow_compiler_usage.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_microsoft_workflow_compiler_rename.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Microsoft.Workflow.Compiler.exe would not normally be run on workstations.
- type: ioc
  description: The presence of csc.exe or vbc.exe as child processes of Microsoft.Workflow.Compiler.exe
- type: ioc
  description: Presence of "<CompilerInput" in a text file.
install:
- method: choco
  package_name: microsoft-workflow-compiler
  commands:
  - choco install microsoft-workflow-compiler
---

# microsoft-workflow-compiler

microsoft-workflow-compiler is a Windows LOLBin. A utility included with .NET that is capable of compiling and executing C# or VB.net code. Located at: C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe.
