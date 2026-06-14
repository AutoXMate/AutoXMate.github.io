---
id: windows-execution-agentexecutor
namespace: windows:execution:agentexecutor
name: agentexecutor
description: 'Intune Management Extension included on Intune Managed Devices Located
  at: C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe.'
author: Eleftherios Panos
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
- agentexecutor
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: agentexecutor
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawns powershell.exe and executes a provided powershell script with
    ExecutionPolicy Bypass argument (Execute unsigned powershell scripts)
  command: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}"
    "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "C:\Windows\SysWOW64\WindowsPowerShell\v1.0"
    0 1
- description: If we place a binary named powershell.exe in the specified folder path,
    agentexecutor.exe will execute it successfully (Execute a provided EXE)
  command: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}"
    "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}"
    0 1
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor_susp_usage.yml
install:
- method: choco
  package_name: agentexecutor
  commands:
  - choco install agentexecutor
---

# agentexecutor

agentexecutor is a Windows LOLBin. Intune Management Extension included on Intune Managed Devices Located at: C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe.
