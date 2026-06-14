---
id: windows-bypass-aspnet-compiler
namespace: windows:bypass:aspnet-compiler
name: aspnet-compiler
description: 'ASP.NET Compilation Tool Located at: c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe;
  c:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe.'
author: Jimmy (@bohops)
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
- aspnet-compiler
parameters: []
features:
- pipes-stdout
- stealth
execution:
  template: aspnet-compiler
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute C# code with the Build Provider and proper folder structure
    in place. (Execute proxied payload with Microsoft signed binary to bypass application
    control solutions)
  command: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v
    none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none
    -u
references:
- label: ''
  url: https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/
- label: system.web.compilation.buildprovider.generatecode?
  url: https://docs.microsoft.com/en-us/dotnet/api/system.web.compilation.buildprovider.generatecode?view=netframework-4.8
techniques:
- defense-evasion
mitre_ids:
- T1127
detections:
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_aspnet_compiler.yml
install:
- method: choco
  package_name: aspnet-compiler
  commands:
  - choco install aspnet-compiler
---

# aspnet-compiler

aspnet-compiler is a Windows LOLBin. ASP.NET Compilation Tool Located at: c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe; c:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe.
