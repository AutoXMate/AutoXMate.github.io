---
id: windows-execution-mpiexec
namespace: windows:execution:mpiexec
name: mpiexec
description: 'Command-line tool for running Message Passing Interface (MPI) applications. Located at: C:\Program Files\Microsoft MPI\Bin\mpiexec.exe; C:\Program Files (x86)\Microsoft MPI\Bin\mpiexec.exe.'
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
- mpiexec
parameters: []
features: []
execution:
  template: mpiexec
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes a command via MPI command-line tool. (Executes commands under a trusted, Microsoft signed binary.)
  command: mpiexec.exe {CMD}
references:
- label: mpiexec
  url: https://learn.microsoft.com/en-us/powershell/high-performance-computing/mpiexec
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: mpiexec
  commands:
  - choco install mpiexec
---


# mpiexec

mpiexec is a Windows LOLBin. Command-line tool for running Message Passing Interface (MPI) applications. Located at: C:\Program Files\Microsoft MPI\Bin\mpiexec.exe; C:\Program Files (x86)\Microsoft MPI\Bin\mpiexec.exe.
