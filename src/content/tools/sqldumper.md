---
id: windows-credential-sqldumper
namespace: windows:credential:sqldumper
name: sqldumper
description: 'Debugging utility included with Microsoft SQL. Located at: C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe; C:\Program Files (x86)\Microsoft Office\root\vfs\ProgramFilesX86\Microsoft Analysis\AS OLEDB\140\SQLDumper.exe; C:\Program Files\Microsoft Power BI Desktop\bin\SqlDumper.exe.'
author: Oddvar Moe
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
- sqldumper
parameters: []
features: []
execution:
  template: sqldumper
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Dump process by PID and create a dump file (Appears to create a dump file called SQLDmprXXXX.mdmp). (Dump process using PID.)
  command: sqldumper.exe 464 0 0x0110
- description: 0x01100:40 flag will create a Mimikatz compatible dump file. (Dump LSASS.exe to Mimikatz compatible dump using PID.)
  command: sqldumper.exe 540 0 0x01100:40
references:
- label: '910969424215232518'
  url: https://twitter.com/countuponsec/status/910969424215232518
- label: '910977826853068800'
  url: https://twitter.com/countuponsec/status/910977826853068800
- label: how-to-use-the-sqldumper-exe-utility-to-generate-a
  url: https://support.microsoft.com/en-us/help/917825/how-to-use-the-sqldumper-exe-utility-to-generate-a-dump-file-in-sql-se
techniques:
- credential-access
mitre_ids:
- T1003
- T1003.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_lsass_memdump_file_created.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
install:
- method: choco
  package_name: sqldumper
  commands:
  - choco install sqldumper
---


# sqldumper

sqldumper is a Windows LOLBin. Debugging utility included with Microsoft SQL. Located at: C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe; C:\Program Files (x86)\Microsoft Office\root\vfs\ProgramFilesX86\Microsoft Analysis\AS OLEDB\140\SQLDumper.exe; C:\Program Files\Microsoft Power BI Desktop\bin\SqlDumper.exe.
