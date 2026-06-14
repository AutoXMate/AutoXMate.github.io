---
id: windows-execution-sqltoolsps
namespace: windows:execution:sqltoolsps
name: sqltoolsps
description: 'Tool included with Microsoft SQL that loads SQL Server cmdlts. A replacement
  for sqlps.exe. Successor to sqlps.exe in SQL Server 2016+. Located at: C:\Program
  files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe.'
author: Oddvar Moe
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
- sqltoolsps
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- remote
execution:
  template: sqltoolsps
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Run a SQL Server PowerShell mini-console without Module and ScriptBlock
    Logging. (Execute PowerShell command.)
  command: SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe}
references:
- label: '993298228840992768'
  url: https://twitter.com/pabraeken/status/993298228840992768
- label: sql-server-powershell?view=sql-server-2017
  url: https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell?view=sql-server-2017
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/aa9f7e0d13a61626c69367290ed1b7b71d1281fd/docs/_posts/2021-10-05-suspicious_copy_on_system32.md
install:
- method: choco
  package_name: sqltoolsps
  commands:
  - choco install sqltoolsps
---

# sqltoolsps

sqltoolsps is a Windows LOLBin. Tool included with Microsoft SQL that loads SQL Server cmdlts. A replacement for sqlps.exe. Successor to sqlps.exe in SQL Server 2016+. Located at: C:\Program files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe.
