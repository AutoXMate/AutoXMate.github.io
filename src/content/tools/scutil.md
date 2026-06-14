---
trust_level: community
id: macos-discovery-scutil
namespace: macos:discovery:scutil
name: scutil
description: Display basic network information, check the dns config, set the computer hostname and perform several other tasks.
author: Ethan Nay
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "scutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "DNS configuration: Get the current DNS configuration of the systems"
    command: "scutil --dns"
  - description: "Proxy configuration: Get the current proxy configuration of the systems"
    command: "scutil --proxy"
  - description: "Network reachability: Check if the destination host is reachable from your Mac"
    command: "scutil -r { nodename | address | local-address remote-address }"
  - description: "Hostname, localhost name and computername: Display the current hostname, localhost name and computername"
    command: "scutil --get { HostName | LocalHostName | ComputerName }"
install:
  - method: custom
    commands:
      - "/usr/bin/scutil"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "macOS/binaries/scutil"
    url: "https://macosbin.com/bin/scutil"
  - label: "scutil man page"
    url: "https://ss64.com/osx/scutil.html"
---

scutil provides a command line interface to the dynamic store data maintained by configd. Interaction with this data (using the SystemConfiguration.framework SCDynamicStore APIs) is handled with a set of commands read from standard input.