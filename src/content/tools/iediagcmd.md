---
id: windows-execution-iediagcmd
namespace: windows:execution:iediagcmd
name: iediagcmd
description: 'Diagnostics Utility for Internet Explorer Located at: C:\Program Files\Internet
  Explorer\iediagcmd.exe.'
author: manasmbellani
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
- iediagcmd
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: iediagcmd
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes binary that is pre-planted at C:\test\system32\netsh.exe.
    (Spawn a pre-planted executable from iediagcmd.exe.)
  command: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe
    /out:{PATH_ABSOLUTE:.cab}
references:
- label: '1507516393859731456'
  url: https://twitter.com/Hexacorn/status/1507516393859731456
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/manasmbellani/mycode_public/blob/master/sigma/rules/win_proc_creation_lolbin_iediagcmd.yml
- type: ioc
  description: Sysmon Event ID 1
- type: ioc
  description: Execution of process iediagcmd.exe with /out could be suspicious
install:
- method: choco
  package_name: iediagcmd
  commands:
  - choco install iediagcmd
---

# iediagcmd

iediagcmd is a Windows LOLBin. Diagnostics Utility for Internet Explorer Located at: C:\Program Files\Internet Explorer\iediagcmd.exe.
