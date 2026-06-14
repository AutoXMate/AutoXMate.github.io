---
trust_level: community
id: macos-discovery-nvram
namespace: macos:discovery:nvram
name: nvram
description: Access and manage the host's non-volatile random-access memory (NVRAM).
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "nvram"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Get nvram variables: The -p option prints all the nvram variables that contain some potentially sensitive information like WiFi SSIDs and Bluetooth devices."
    command: "nvram -p"
install:
  - method: custom
    commands:
      - "/usr/sbin/nvram"
detections:
  - type: other
    description: "No detections at time of publishing."
references:
  - label: "SS64 man page"
    url: "https://ss64.com/osx/nvram.html"
---

Access and manage the host's non-volatile random-access memory (NVRAM).