---
id: windows-credential-dsdbutil
namespace: windows:credential:dsdbutil
name: dsdbutil
description: 'Dsdbutil is a command-line tool that is built into Windows Server. It
  is available if you have the AD LDS server role installed. Can be used as a command
  line utility to export Active Directory. Located at: C:\Windows\System32\dsdbutil.exe;
  C:\Windows\SysWOW64\dsdbutil.exe.'
author: Ekitji
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
related_tools:
- dsDbUtil
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
- dsdbutil
parameters: []
features:
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: dsdbutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: dsdbutil supports VSS snapshot creation (Snapshoting of Active Directory
    NTDS.dit database)
  command: dsdbutil.exe "activate instance ntds" "snapshot" "create" "quit" "quit"
- description: Mounting the snapshot with its GUID (Mounting the snapshot to access
    the ntds.dit with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`)
  command: dsdbutil.exe "activate instance ntds" "snapshot" "mount {GUID}" "quit"
    "quit"
- description: Deletes the mount of the snapshot (Deletes the snapshot)
  command: dsdbutil.exe "activate instance ntds" "snapshot" "delete {GUID}" "quit"
    "quit"
- description: Mounting with snapshot identifier (Mounting the snapshot identifier
    1 and accessing it with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`)
  command: dsdbutil.exe "activate instance ntds" "snapshot" "create" "list all" "mount
    1" "quit" "quit"
- description: Deletes the mount of the snapshot (deletes the snapshot)
  command: dsdbutil.exe "activate instance ntds" "snapshot" "list all" "delete 1"
    "quit" "quit"
references:
- label: 88561ca40998e83deb3d1da90289e358
  url: https://gist.github.com/bohops/88561ca40998e83deb3d1da90289e358
- label: ntds_dit_security_active_directory.html
  url: https://www.netwrix.com/ntds_dit_security_active_directory.html
techniques:
- credential-access
mitre_ids:
- T1003.003
detections:
- type: ioc
  description: Event ID 4688
- type: ioc
  description: dsdbutil.exe process creation
- type: ioc
  description: Event ID 4663
- type: ioc
  description: Regular and Volume Shadow Copy attempts to read or modify ntds.dit
- type: ioc
  description: Event ID 4656
- type: ioc
  description: Regular and Volume Shadow Copy attempts to read or modify ntds.dit
install:
- method: choco
  package_name: dsdbutil
  commands:
  - choco install dsdbutil
---

# dsdbutil

dsdbutil is a Windows LOLBin. Dsdbutil is a command-line tool that is built into Windows Server. It is available if you have the AD LDS server role installed. Can be used as a command line utility to export Active Directory. Located at: C:\Windows\System32\dsdbutil.exe; C:\Windows\SysWOW64\dsdbutil.exe.
