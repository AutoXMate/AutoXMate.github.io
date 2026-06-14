---
trust_level: community
id: macos-discovery-dsconfigad
namespace: macos:discovery:dsconfigad
name: dsconfigad
description: retrieves/changes configuration for Directory Services Active Directory
  Plugin.
author: Ethan Nay
version: 1.0.0
capabilities:
- discovery.enumerate
platforms:
- macos
techniques:
- discovery
execution:
  template: dsconfigad
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Retrieves the Active Directory configuration: Retrieves the Active
    Directory configuration'
  command: dsconfigad -show
- description: 'Retrieves the Active Directory name: Retrieves the Active Directory
    name'
  command: dsconfigad -show |awk '/Active Directory Domain/{print $NF}'
install:
- method: custom
  commands:
  - /usr/sbin/dsconfigad
detections:
- type: other
  description: No detections at time of publishing
references:
- label: macOS/binaries/dsconfigad
  url: https://macosbin.com/bin/dsconfigad
- label: dsconfigad man page
  url: https://www.unix.com/man-page/osx/8/dsconfigad/
features:
- process-manip
---

This tool allows command-line configuration of the Active Directory Plug-in. dsconfigad has the same functionality for configuring the Active Directory plugin as the Directory Utility application. It requires "admin" privileges to the local workstation and to the Directory to make changes.
