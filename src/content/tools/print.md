---
id: windows-copy-print
namespace: windows:copy:print
name: print
description: 'Used by Windows to send files to the printer Located at: C:\Windows\System32\print.exe;
  C:\Windows\SysWOW64\print.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- system.file.copy
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
  - filesystem_write
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
- print
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: print
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Copy file.exe into the Alternate Data Stream (ADS) of file.txt. (Hide
    binary file in alternate data stream to potentially bypass defensive counter measures)
  command: print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe}
- description: Copy file from source to destination (Copy files)
  command: print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_ABSOLUTE:.source.exe}
- description: Copy File.exe from a network share to the target c:\OutFolder\outfile.exe.
    (Copy/Download file from remote server)
  command: print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe}
references:
- label: '985518877076541440'
  url: https://twitter.com/Oddvarmoe/status/985518877076541440
- label: watch?v=nPBcSP8M7KE&lc=z22fg1cbdkabdf3x404t1aokgwd
  url: https://www.youtube.com/watch?v=nPBcSP8M7KE&lc=z22fg1cbdkabdf3x404t1aokgwd2zxasf2j3rbozrswnrk0h00410
techniques:
- defense-evasion
- collection
- exfiltration
mitre_ids:
- T1564.004
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml
- type: ioc
  description: Print.exe retrieving files from internet
- type: ioc
  description: Print.exe creating executable files on disk
install:
- method: choco
  package_name: print
  commands:
  - choco install print
---

# print

print is a Windows LOLBin. Used by Windows to send files to the printer Located at: C:\Windows\System32\print.exe; C:\Windows\SysWOW64\print.exe.
