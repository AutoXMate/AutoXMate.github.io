---
trust_level: community
id: macos-defense-evasion-log
namespace: macos:defenseevasion:log
name: log
description: Access system log messages from Apple Unified Logging (AUL).
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- security.defenseevasion.bypass
- credential.dump
platforms:
- macos
techniques:
- defense-evasion
- credential-access
execution:
  template: log
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Remove all log messages: An attacker can cover up their tracks by
    removing all log messages using the following command. Requires root privileges.'
  command: log erase --all
- description: 'Search log messages for tokens: An attacker can potentially search
    log messages and review if they do contain sensitive information like jwt tokens.'
  command: log show --info --debug --predicate 'eventMessage CONTAINS[d] "eyJ"'
install:
- method: custom
  commands:
  - /usr/bin/log
detections:
- type: other
  description: No detections at time of publishing
references:
- label: Living off the land in macOS (Daniel Stinson)
  url: https://shellcromancer.io/posts/living-off-of-macos/
features:
- stealth
---

The log command can be used to access system log messages from Apple Unified Logging (AUL). The tool can be used to inspect existing logs, stream logs in realtime, and delete logs. This tool is normally used by system admins and application developers for troubleshooting purposes but can be used by an adversary to gain an understanding of the user's behavior or to cover up their tracks by deleting log messages.
