---
id: windows-execution-odbcconf
namespace: windows:execution:odbcconf
name: odbcconf
description: 'Used in Windows for managing ODBC connections Located at: C:\Windows\System32\odbcconf.exe;
  C:\Windows\SysWOW64\odbcconf.exe.'
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
- odbcconf
parameters: []
features:
- network-intensive
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: odbcconf
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute DllRegisterServer from DLL specified. (Execute a DLL file using
    technique that can evade defensive counter measures)
  command: odbcconf /a {REGSVR {PATH_ABSOLUTE:.dll}}
- description: Install a driver and load the DLL. Requires administrator privileges.
    (Execute dll file using technique that can evade defensive counter measures)
  command: 'odbcconf INSTALLDRIVER "lolbas-project|Driver={PATH_ABSOLUTE:.dll}|APILevel=2"

    odbcconf configsysdsn "lolbas-project" "DSN=lolbas-project"

    '
- description: Load DLL specified in target .RSP file. See the Code Sample section
    for an example .RSP file. (Execute dll file using technique that can evade defensive
    counter measures)
  command: odbcconf -f {PATH:.rsp}
references:
- label: 6ef02ce3fd623483137b45f65017352b
  url: https://gist.github.com/NickTyrer/6ef02ce3fd623483137b45f65017352b
- label: application-restriction-bypasses
  url: https://github.com/woanware/application-restriction-bypasses
- label: ''
  url: https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.008
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_odbcconf_response_file_susp.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
install:
- method: choco
  package_name: odbcconf
  commands:
  - choco install odbcconf
---

# odbcconf

odbcconf is a Windows LOLBin. Used in Windows for managing ODBC connections Located at: C:\Windows\System32\odbcconf.exe; C:\Windows\SysWOW64\odbcconf.exe.
