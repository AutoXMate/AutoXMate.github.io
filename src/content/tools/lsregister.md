---
trust_level: community
id: macos-discovery-lsregister
namespace: macos:discovery:lsregister
name: lsregister
description: Interact with the macOS Launch Services database.
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- discovery.enumerate
- impact.destruction
platforms:
- macos
techniques:
- discovery
- impact
execution:
  template: lsregister
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Force an update of the Launch Services database: The -f flag can be
    used to force an update of the Launch Services database. This can be used to quickly
    register a custom URL scheme that points to a malicious app.'
  command: /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister
    -f
- description: 'Get a list of apps and their bindings: The -dump flag can be used
    to get a list of apps and their bindings'
  command: '/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister
    -dump | grep -E "path:|bindings:|name: | more"'
- description: 'Delete the Launch Services database: The -delete flag can be used
    to delete the Launch Services database to impact normal operation of the system.'
  command: lsregister -delete
install:
- method: custom
  commands:
  - /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister
detections:
- type: other
  description: No detections at time of publishing
references:
- label: Remote Mac Exploitation Via Custom URL Schemes
  url: https://www.jamf.com/blog/remote-mac-exploitation-via-custom-url-schemes/
- label: macOS Security & Privilege Escalation
  url: https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation
features:
- process-manip
---

lsregister is used to build, dump, and check the validity of the Launch Services database. This database is often abused to create custom URL scheme handlers that point to malicious apps.
