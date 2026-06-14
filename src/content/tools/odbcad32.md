---
id: windows-uacbypass-odbcad32
namespace: windows:uacbypass:odbcad32
name: odbcad32
description: 'ODBC Data Source Administrator to manage User/System DSNs and ODBC drivers.
  Located at: c:\windows\system32\odbcad32.exe; c:\windows\syswow64\odbcad32.exe.'
author: Ekitji
version: 1.0.0
capabilities:
- security.privilege-escalation.uac-bypass
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
  - privilege_escalation
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
- odbcad32
parameters: []
features:
- pipes-stdout
- requires-root
- stealth
execution:
  template: odbcad32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch odbcad32.exe GUI, click 'Tracing' tab, click 'Browsing' button,
    enter abitrary command in the File Dialog's path, press enter. (Execute a binary
    as a high-integrity process without a UAC prompt.)
  command: odbcad32.exe
references:
- label: living-off-the-land-and-living-above-uac-6a66738d2
  url: https://medium.com/@thebinaryhashira/living-off-the-land-and-living-above-uac-6a66738d225c
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: ioc
  description: odbcad32.exe spawning unexpected child processes.
install:
- method: choco
  package_name: odbcad32
  commands:
  - choco install odbcad32
---

# odbcad32

odbcad32 is a Windows LOLBin. ODBC Data Source Administrator to manage User/System DSNs and ODBC drivers. Located at: c:\windows\system32\odbcad32.exe; c:\windows\syswow64\odbcad32.exe.
