---
trust_level: community
id: macos-defense-evasion-tccutil
namespace: macos:defenseevasion:tccutil
name: tccutil
description: Command-line tool for managing the Transparency, Consent, and Control
  (TCC) permissions database
author: Hare Sudhan (@cyb3rbuff)
version: 1.0.0
capabilities:
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- defense-evasion
execution:
  template: tccutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Use the tccutil to reset specific permissions: Banshee Stealer resets
    the permissions that have already been allowed to applications on the system,
    which will cause the user to be prompted to give them again. This action may be
    intended to trick the user into unknowingly giving authorizations to the malware.'
  command: tccutil reset AppleEvents
- description: 'Use the tccutil to reset specific permissions for an application:
    Attackers use tccutil to reset permissions for services like Camera, Microphone,
    or AppleEvents.'
  command: tccutil reset AppleEvents com.apple.Terminal
install:
- method: custom
  commands:
  - /usr/bin/tccutil
detections:
- type: other
  description: No detections at time of publishing
references:
- label: tccutil
  url: https://ss64.com/mac/tccutil.html
- label: 'Banshee: The Stealer That ''Stole Code'' From MacOS XProtect'
  url: https://research.checkpoint.com/2025/banshee-macos-stealer-that-stole-code-from-macos-xprotect/
features:
- file-system
- pipes-stdin
- stealth
---

tccutil is a command-line tool for managing the Transparency, Consent, and Control (TCC) permissions database. It allows users to revoke permissions for applications to access certain system resources, such as the camera, microphone, and location.
