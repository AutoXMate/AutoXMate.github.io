---
trust_level: community
id: macos-collection-screencapture
namespace: macos:collection:screencapture
name: screencapture
description: Capture a screenshot from command line.
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- collection.data
platforms:
- macos
techniques:
- collection
execution:
  template: screencapture
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Continuously capture screenshots: The following command demonstrates
    how an attacker can use the tool to capture screenshots every 10 seconds. The
    -x flag prevents snapshot sounds from being played.'
  command: while true; do ts=$(date +"%Y%m%d-%H%M%S"); o="/tmp/screenshots"; screencapture
    -x "$o/ss-$ts.png"; sleep 10; done
install:
- method: custom
  commands:
  - /usr/sbin/screencapture
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_screencapture.yml
  description: 'Sigma: Screen Capture - macOS'
references:
- label: SS64 screencapture man page
  url: https://ss64.com/osx/screencapture.html
features:
- interactive
---

A tools that allows users to take screenshots of their desktop or specific app windows. The tool can be used by malicious actors to collect sensitive information from the targeted system.
