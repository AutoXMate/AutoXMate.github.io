---
id: security-exploit-msfconsole
namespace: security:exploit:msfconsole
name: msfconsole
description: Metasploit console, can execute Ruby code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - ruby
  - metasploit
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
    - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 128
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 128
  network: low
  disk_io: low
allowed-tools:
  - msfconsole
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "msfconsole -q -x 'irb'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via msfconsole
    command: |
      msfconsole -q -x 'irb'
      exec "/bin/sh"
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/msfconsole/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "metasploit-framework"
    commands:
      - "apt-get install -y metasploit-framework"
items:
  - Password
  - Hash
  - Shell
  - NoCreds
services:
  - HTTP
  - SMB
  - Kerberos
  - LDAP
  - SSH
  - FTP
  - WinRM
  - DNS
---
