---
id: windows-execution-schtasks
namespace: windows:execution:schtasks
name: schtasks
description: 'Schedule periodic tasks Located at: c:\windows\system32\schtasks.exe; c:\windows\syswow64\schtasks.exe.'
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
- schtasks
parameters: []
features: []
execution:
  template: schtasks
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Create a recurring task to execute every minute. (Create a recurring task to keep reverse shell session(s) alive)
  command: schtasks /create /sc minute /mo 1 /tn "Reverse shell" /tr "{CMD}"
- description: Create a scheduled task on a remote computer for persistence/lateral movement (Create a remote task to run daily relative to the the time of creation)
  command: schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily
references:
- label: ''
  url: https://isc.sans.edu/forums/diary/Adding+Persistence+Via+Scheduled+Tasks/23633/
techniques:
- execution
mitre_ids:
- T1053.005
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/persistence_local_scheduled_task_creation.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/schtasks_scheduling_job_on_remote_system.yml
- type: ioc
  description: Suspicious task creation events
install:
- method: choco
  package_name: schtasks
  commands:
  - choco install schtasks
---


# schtasks

schtasks is a Windows LOLBin. Schedule periodic tasks Located at: c:\windows\system32\schtasks.exe; c:\windows\syswow64\schtasks.exe.
