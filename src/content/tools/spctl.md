---
trust_level: community
id: macos-defense-evasion-spctl
namespace: macos:defenseevasion:spctl
name: spctl
description: Manage the security assessment policy subsystem, Gatekeeper settings,
  and control which apps are allowed to run on the system.
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- defense-evasion
execution:
  template: spctl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Disable Gatekeeper: The --master-disable switch disables Gatekeeper.
    The command must be run with root/sudo permission.'
  command: sudo spctl --master-disable
install:
- method: custom
  commands:
  - /usr/sbin/spctl
detections:
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/e9baebc2bc18f90ae16501613cd9521a16a38ad7/rules/macos/defense_evasion_attempt_to_disable_gatekeeper.toml
  description: 'Elastic Detection Rules: Attempt to Disable Gatekeeper'
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/cd71edc09ca915f389e50df5b1bbb5ecd4b7f89d/rules/macos/process_creation/proc_creation_macos_disable_security_tools.yml
  description: 'Sigma Rules: Disable Security Tools'
references:
- label: Disable Gatekeeper on macOS Big Sur (11.x)
  url: https://disable-gatekeeper.github.io/
features:
- process-manip
- stealth
---

Manage the security assessment policy subsystem, Gatekeeper settings, and control which apps are allowed to run on the system.
