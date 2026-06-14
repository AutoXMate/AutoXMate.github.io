---
id: windows-recon-nmcap
namespace: windows:recon:nmcap
name: nmcap
description: 'Command-line packet capture utility from Microsoft Network Monitor 3.x. Located at: C:\Program Files\Microsoft Network Monitor 3\nmcap.exe; C:\Program Files (x86)\Microsoft Network Monitor 3\nmcap.exe.'
author: Avihay Eldad
version: 1.0.0
capabilities:
- recon.enumeration
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
- nmcap
parameters: []
features: []
execution:
  template: nmcap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: "Start capture on all network adapters and save to specified .cap (circular) file.\nOptionally, one can add:\n- `/TerminateWhen /TimeAfter 30 seconds` to auto-terminate after a relative times (e.g. 30 seconds);\n- `/TerminateWhen /Time 04:52:00 AM 9/17/2025` to auto-terminate after a specific date/time;\n- `/TerminateWhen /KeyPress x` to terminate when a specific key is pressed.\n (Capture network traffic on windows to collect sensitive data.)"
  command: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
references:
- label: network-monitor-3
  url: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/network-monitor-3
techniques:
- discovery
mitre_ids:
- T1040
detections: []
install:
- method: choco
  package_name: nmcap
  commands:
  - choco install nmcap
---


# nmcap

nmcap is a Windows LOLBin. Command-line packet capture utility from Microsoft Network Monitor 3.x. Located at: C:\Program Files\Microsoft Network Monitor 3\nmcap.exe; C:\Program Files (x86)\Microsoft Network Monitor 3\nmcap.exe.
