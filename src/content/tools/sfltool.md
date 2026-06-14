---
trust_level: community
id: macos-discovery-sfltool
namespace: macos:discovery:sfltool
name: sfltool
description: Binary to manage the Shared File List framework.
author: Eliott (@Koyiott)
version: "1.0.0"
capabilities:
  - discovery.enumerate
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - discovery
  - defense-evasion
execution:
  template: "sfltool"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Display Login Items: Identify all current login and background items configured on the system."
    command: "sfltool dumpbtm"
  - description: "Reset Login Items to Defaults: Reset all third-party Login Items and revert to installation defaults."
    command: "sfltool resetbtm"
install:
  - method: custom
    commands:
      - "/usr/bin/sfltool"
detections:
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/sfltool_activity"
    description: "Jamf Protect: Detect attempts to dump BTM or being reverted to installation defaults"
references:
  - label: "sfltool man page"
    url: "https://www.unix.com/man-page/mojave/1/sfltool/"
  - label: "Controlling login and background items"
    url: "https://eclecticlight.co/2023/02/15/controlling-login-and-background-items-in-ventura/"
---

sfltool allows interactions with the Shared File List framework, which can be used to modify application recent documents, favorites, and more.