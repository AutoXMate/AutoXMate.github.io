---
id: windows-credential-createdump
namespace: windows:credential:createdump
name: createdump
description: 'Microsoft .NET Runtime Crash Dump Generator (included in .NET Core)
  Located at: C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe;
  C:\Program Files (x86)\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe;
  C:\Program Files\Microsoft Visual Studio\<version>\Community\dotnet\runtime\shared\Microsoft.NETCore.App\6.0.0\createdump.exe.'
author: mr.d0x, Daniel Santos
version: 1.0.0
capabilities:
- credential.dump
platforms:
- windows
risk_level: critical
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
- createdump
parameters: []
features:
- file-system
- local
- pipes-stdout
- process-manip
execution:
  template: createdump
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Dump process by PID and create a minidump file. If "-f dump.dmp" is
    not specified, the file is created as '%TEMP%\dump.%p.dmp' where %p is the PID
    of the target process. (Dump process memory contents using PID.)
  command: createdump.exe -n -f {PATH:.dmp} {PID}
references:
- label: '1366400799199272960'
  url: https://twitter.com/bopin2020/status/1366400799199272960
- label: lab-1-3-capture-core-crash-dumps
  url: https://docs.microsoft.com/en-us/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/lab-1-3-capture-core-crash-dumps
techniques:
- credential-access
mitre_ids:
- T1003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_proc_dump_createdump.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_renamed_createdump.yml
- type: ioc
  description: createdump.exe process with a command line containing the lsass.exe
    process id
install:
- method: choco
  package_name: createdump
  commands:
  - choco install createdump
---

# createdump

createdump is a Windows LOLBin. Microsoft .NET Runtime Crash Dump Generator (included in .NET Core) Located at: C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe; C:\Program Files (x86)\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe; C:\Program Files\Microsoft Visual Studio\<version>\Community\dotnet\runtime\shared\Microsoft.NETCore.App\6.0.0\createdump.exe.
