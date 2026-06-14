---
id: windows-execution-tttracer
namespace: windows:execution:tttracer
name: tttracer
description: 'Used by Windows 1809 and newer to Debug Time Travel Located at: C:\Windows\System32\tttracer.exe; C:\Windows\SysWOW64\tttracer.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
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
- tttracer
parameters: []
features: []
execution:
  template: tttracer
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute specified executable from tttracer.exe. Requires administrator privileges. (Spawn process using other binary)
  command: tttracer.exe {PATH_ABSOLUTE:.exe}
- description: Dumps process using tttracer.exe. Requires administrator privileges (Dump process by PID)
  command: TTTracer.exe -dumpFull -attach {PID}
references:
- label: '1191329746069655553'
  url: https://twitter.com/oulusoyum/status/1191329746069655553
- label: '1196390321783025666'
  url: https://twitter.com/mattifestation/status/1196390321783025666
- label: 002877.html
  url: https://lists.samba.org/archive/cifs-protocol/2016-April/002877.html
techniques:
- execution
- defense-evasion
- credential-access
mitre_ids:
- T1127
- T1003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_tttracer_mod_load.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- type: ioc
  description: Parent child relationship. Tttracer parent for executed command
install:
- method: choco
  package_name: tttracer
  commands:
  - choco install tttracer
---


# tttracer

tttracer is a Windows LOLBin. Used by Windows 1809 and newer to Debug Time Travel Located at: C:\Windows\System32\tttracer.exe; C:\Windows\SysWOW64\tttracer.exe.
