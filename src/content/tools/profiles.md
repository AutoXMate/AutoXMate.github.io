---
trust_level: community
id: macos-discovery-profiles
namespace: macos:discovery:profiles
name: profiles
description: List and remove configuration profiles.
author: Will Huang (@In0de_16)
version: "1.0.0"
capabilities:
  - discovery.enumerate
  - impact.destruction
platforms:
  - macos
techniques:
  - discovery
  - impact
execution:
  template: "profiles"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Collect system DEP information.: The following command determines whether device is DEP(Device Enrolment Program) enabled and output the DEP information."
    command: "sudo profiles show -type enrollment"
  - description: "Remove configuration profiles.: The following command deletes the specified profiles. An optional password used when removing a configuration profile which requires the password removal option."
    command: "profiles remove -identifier com.profile.identifier -password <password>"
install:
  - method: custom
    commands:
      - "/usr/bin/profiles"
detections:
  - type: other
    description: "No detections at time of publishing."
references:
  - label: "macOS MDM introduction."
    url: "https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation/macos-mdm"
---

Profiles on macOS are responsible for managing different types of profiles including configuration, provisioning, bootstraptoken, or enrollment. However, starting from macOS 11.0, this tool cannot be used for installing configuration profiles.