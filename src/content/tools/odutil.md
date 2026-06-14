---
trust_level: community
id: macos-discovery-odutil
namespace: macos:discovery:odutil
name: odutil
description: odutil allows caller to examine or change state of opendirectoryd
author: Ethan Nay
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "odutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Listing the available node names: List all available node names"
    command: "odutil show nodenames"
  - description: "Retrieves active session: Retrieves all active sessions"
    command: "odutil show sessions"
  - description: "Retrieves \"Default search policy\": Retrieves the configuration of \"Default search policy\""
    command: "odutil show configuration /Search"
  - description: "Retrieves \"Contact search policy\": Retrieves the configuration of \"Contact search policy\""
    command: "odutil show configuration /Contacts"
install:
  - method: custom
    commands:
      - "/usr/bin/odutil"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "macOS/binaries/odutil"
    url: "https://macosbin.com/bin/odutil"
  - label: "odutil man page"
    url: "https://www.unix.com/man-page/osx/1/odutil/"
---

To look at internal state information for opendirectoryd, enable or disable logging, or change statistics settings.