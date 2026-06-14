---
id: windows-uacbypass-wsreset
namespace: windows:uacbypass:wsreset
name: wsreset
description: 'Used to reset Windows Store settings according to its manifest file
  Located at: C:\Windows\System32\wsreset.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.privilege-escalation.uac-bypass
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
  - privilege_escalation
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
- wsreset
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- requires-root
- stealth
execution:
  template: wsreset
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: During startup, wsreset.exe checks the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
    for the command to run. Binary will be executed as a high-integrity process without
    a UAC prompt being displayed to the user. (Execute a binary or script as a high-integrity
    process without a UAC prompt.)
  command: wsreset.exe
references:
- label: windows-uac-bypass
  url: https://www.activecyber.us/activelabs/windows-uac-bypass
- label: '1106644790114947073'
  url: https://twitter.com/ihack4falafel/status/1106644790114947073
- label: README.md
  url: https://github.com/hfiref0x/UACME/blob/master/README.md
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset_integrity_level.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml#
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/wsreset_uac_bypass.yml
- type: ioc
  description: wsreset.exe launching child process other than mmc.exe
- type: ioc
  description: Creation or modification of the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
- type: ioc
  description: Microsoft Defender Antivirus as Behavior:Win32/UACBypassExp.T!gen
install:
- method: choco
  package_name: wsreset
  commands:
  - choco install wsreset
---

# wsreset

wsreset is a Windows LOLBin. Used to reset Windows Store settings according to its manifest file Located at: C:\Windows\System32\wsreset.exe.
