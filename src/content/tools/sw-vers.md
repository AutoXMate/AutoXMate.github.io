---
trust_level: community
id: macos-discovery-sw-vers
namespace: macos:discovery:sw-vers
name: sw_vers
description: Prints macOS version information.
author: Eliott (@Koyiott)
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "sw_vers"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Retrieving macOS Version Information: Fetch detailed macOS version information including the build version, product name, and product version."
    command: "sw_vers"
  - description: "Retrieving macOS Product Version: Fetch macOS product version."
    command: "sw_vers -productVersion"
  - description: "Retrieving macOS Product Name: Fetch detailed macOS product name."
    command: "sw_vers -productName"
  - description: "Retrieving macOS Build Version: Fetch detailed macOS build version."
    command: "sw_vers -buildVersion"
install:
  - method: custom
    commands:
      - "/usr/bin/sw_vers"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "macOS/binaries/sw_vers"
    url: "https://macosbin.com/bin/sw_vers"
  - label: "sw_vers man page"
    url: "https://ss64.com/osx/sw_vers.html"
---

sw_vers prints macOS version information, including the exact macOS version number.