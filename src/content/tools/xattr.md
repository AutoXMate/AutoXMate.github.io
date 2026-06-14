---
trust_level: community
id: macos-execution-xattr
namespace: macos:execution:xattr
name: xattr
description: Display and manipulate extended attributes.
author: Jason Trost (@jason_trost)
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - execution
  - defense-evasion
execution:
  template: "xattr"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Bypass Gatekeeper via xattr: Use xattr to remove quarantine extended attribute from a file."
    command: "xattr -d com.apple.quarantine FILE"
  - description: "Bypass Gatekeeper via xattr: Use xattr to remove quarantine extended attribute from multiple files or directories."
    command: "xattr -d -r com.apple.quarantine *"
install:
  - method: custom
    commands:
      - "/usr/bin/xattr"
detections:
  - type: other
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_xattr_gatekeeper_bypass.yml"
    description: "Gatekeeper Bypass via Xattr"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/xattr_extended_attributes_activity"
    description: "Jamf Protect: Detect activity related to xattr and extended attributes"
references:
  - label: "Threat Hunting the macOS edition Megan Carney (Report)"
    url: "https://megancarney.com/presentations/ExternalReport_ThreatHuntingMacOS.pdf"
  - label: "GrrCon 2018: Threat Hunting the macOS edition Megan Carney"
    url: "https://www.youtube.com/watch?v=_K4gnSuDkRM&feature=youtu.be"
---

The xattr command can be used to display, modify or remove the extended attributes of one or more files, including directories and symbolic links.  Extended attributes are arbitrary metadata stored with a file, but separate from the filesystem attributes (such as modification time or file size).  The metadata is often a null-terminated UTF-8 string, but can also be arbitrary binary data.  xattr can be used to bypass Gatekeeper.