---
id: windows-download-bcp
namespace: windows:download:bcp
name: bcp
description: 'Microsoft SQL Server Bulk Copy Program utility for importing and exporting data between SQL Server instances and data files. Located at: C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe; C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe; C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe.'
author: Mahir Ali Khan
version: 1.0.0
capabilities:
- network.transfer.download
platforms:
- windows
risk_level: medium
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
- bcp
parameters: []
features: []
execution:
  template: bcp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Export binary payload stored in SQL Server database to file system. (Extract malicious executable from database storage to local file system for execution.)
  command: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c
references:
- label: bcp-utility
  url: https://docs.microsoft.com/en-us/sql/tools/bcp-utility
- label: ''
  url: https://asec.ahnlab.com/en/61000/
- label: ''
  url: https://asec.ahnlab.com/en/78944/
- label: attacking-mssql-servers
  url: https://www.huntress.com/blog/attacking-mssql-servers
- label: attacking-mssql-servers-pt-ii
  url: https://www.huntress.com/blog/attacking-mssql-servers-pt-ii
- label: ''
  url: https://news.sophos.com/en-us/2024/08/07/sophos-mdr-hunt-tracks-mimic-ransomware-campaign-against-organizations-in-india/
- label: ''
  url: https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: Process creation of bcp.exe with queryout or Out parameter
- type: ioc
  description: bcp.exe writing executable files to temp or users directories
- type: ioc
  description: Network connections from bcp.exe to SQL Server followed by file creation
- type: ioc
  description: Event ID 4688 - Process creation for bcp.exe
- type: ioc
  description: Event ID 4663 - File system access by bcp.exe
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml
install:
- method: choco
  package_name: bcp
  commands:
  - choco install bcp
---


# bcp

bcp is a Windows LOLBin. Microsoft SQL Server Bulk Copy Program utility for importing and exporting data between SQL Server instances and data files. Located at: C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe; C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe; C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe.
