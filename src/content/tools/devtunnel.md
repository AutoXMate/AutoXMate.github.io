---
id: windows-download-devtunnel
namespace: windows:download:devtunnel
name: devtunnel
description: 'Binary to enable forwarded ports on windows operating systems. Located
  at: C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe; C:\Users\<username>\AppData\Local\Temp\DevTunnels\devtunnel.exe.'
author: Kamran Saifullah
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
- devtunnel
parameters: []
features:
- local
- network-intensive
- pipes-stdout
execution:
  template: devtunnel
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Enabling a forwarded port for locally hosted service at port 8080 to
    be exposed on the internet. (Download Files, Upload Files, Data Exfiltration)
  command: devtunnel.exe host -p 8080
references:
- label: port-forwarding
  url: https://code.visualstudio.com/docs/editor/port-forwarding
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
- type: ioc
  description: devtunnel.exe binary spawned
- type: ioc
  description: '*.devtunnels.ms'
- type: ioc
  description: '*.*.devtunnels.ms'
- type: other
  url: https://cydefops.com/vscode-data-exfiltration
install:
- method: choco
  package_name: devtunnel
  commands:
  - choco install devtunnel
---

# devtunnel

devtunnel is a Windows LOLBin. Binary to enable forwarded ports on windows operating systems. Located at: C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe; C:\Users\<username>\AppData\Local\Temp\DevTunnels\devtunnel.exe.
