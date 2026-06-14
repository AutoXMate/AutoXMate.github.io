---
trust_level: community
id: macos-discovery-softwareupdate
namespace: macos:discovery:softwareupdate
name: softwareupdate
description: Interact with the macOS software update service.
author: Jonathan Bar Or (@yo_yo_yo_jbo)
version: 1.0.0
capabilities:
- discovery.enumerate
platforms:
- macos
techniques:
- discovery
execution:
  template: softwareupdate
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Get OS and browser version information: Determine OS and Safari version
    by enumerating the available software updates.'
  command: softwareupdate --list
- description: 'Get OS update policy: Use the --schedule flag to return the OS update
    policy.'
  command: softwareupdate --schedule
install:
- method: custom
  commands:
  - /usr/sbin/softwareupdate
detections:
- type: other
  description: No detections at time of publishing
references:
- label: softwareupdate Man Page
  url: https://ss64.com/osx/softwareupdate.html
features:
- process-manip
---

A command-line utility for running software updates.
