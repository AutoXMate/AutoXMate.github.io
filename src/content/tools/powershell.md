---
id: windows-execution-powershell
namespace: windows:execution:powershell
name: powershell
description: 'Powershell.exe is a a task-based command-line shell built on .NET. Located
  at: C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe; C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe.'
author: Everyone
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
- powershell
parameters: []
features:
- interactive
- pipes-stdin
- pipes-stdout
execution:
  template: powershell
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Set the execution policy to bypass and execute a PowerShell script
    without warning (Execute PowerShell cmdlets, .NET code, and just about anything
    else your heart desires)
  command: powershell.exe -ep bypass -file c:\path\to\a\script.ps1
- description: Set the execution policy to bypass and execute a PowerShell command
    (Execute PowerShell cmdlets, .NET code, and just about anything else your heart
    desires)
  command: powershell.exe -ep bypass -command "Invoke-AllTheThings..."
- description: Set the execution policy to bypass and execute a very malicious PowerShell
    encoded command (Execute PowerShell cmdlets, .NET code, and just about anything
    else your heart desires)
  command: powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA==
references:
- label: about_powershell_exe?view=powershell-5.1
  url: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1
- label: ''
  url: https://attack.mitre.org/techniques/T1059/001/
techniques:
- execution
mitre_ids:
- T1059.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/tree/71ae004b32bb3c7fb04714f8a051fc8e5edda68c/rules/windows/powershell
install:
- method: choco
  package_name: powershell
  commands:
  - choco install powershell
---

# powershell

powershell is a Windows LOLBin. Powershell.exe is a a task-based command-line shell built on .NET. Located at: C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe; C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe.
