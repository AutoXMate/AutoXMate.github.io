---
id: windows-copy-dtutil
namespace: windows:copy:dtutil
name: dtutil
description: 'Microsoft command line utility used to manage SQL Server Integration
  Services packages. Located at: C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe;
  C:\Program Files (x86)\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe.'
author: Avihay Eldad
version: 1.0.0
capabilities:
- system.file.copy
platforms:
- windows
risk_level: low
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
  - filesystem_write
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
- dtutil
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- remote
execution:
  template: dtutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Copy file from source to destination (Use to copies the source file
    to the destination file)
  command: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
references:
- label: dtutil-utility?view=sql-server-ver16
  url: https://learn.microsoft.com/en-us/sql/integration-services/dtutil-utility?view=sql-server-ver16
techniques:
- collection
- exfiltration
mitre_ids:
- T1105
detections: []
install:
- method: choco
  package_name: dtutil
  commands:
  - choco install dtutil
---

# dtutil

dtutil is a Windows LOLBin. Microsoft command line utility used to manage SQL Server Integration Services packages. Located at: C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe; C:\Program Files (x86)\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe.
