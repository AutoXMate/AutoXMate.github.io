---
trust_level: community
id: macos-discovery-dscacheutil
namespace: macos:discovery:dscacheutil
name: dscacheutil
description: gather information, statistics and initiate queries to the Directory Service cache.
author: Ethan Nay
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "dscacheutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Lookup  a user: List the user information"
    command: "dscacheutil -q user -a name <USER_NAME>"
  - description: "Lookup all users: List all user information"
    command: "dscacheutil -q user"
install:
  - method: custom
    commands:
      - "/usr/bin/dscacheutil"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "macOS/binaries/dscacheutil"
    url: "https://macosbin.com/bin/dscacheutil"
  - label: "dscacheutil man page"
    url: "https://ss64.com/osx/dscacheutil.html"
---

dscacheutil does various operations against the Directory Service cache including gathering statistics, initiating lookups, inspection, cache flush, etc.
This tool replaces most of the functionality of the lookupd tool previously available in the OS.