---
trust_level: community
id: macos-execution-caffeinate
namespace: macos:execution:caffeinate
name: caffeinate
description: Prevent the system from sleeping on behalf of a utility.
author: Ethan Nay
version: 1.0.0
capabilities:
- security.execution.command
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- execution
- defense-evasion
execution:
  template: caffeinate
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Fork a process: Make caffeinate fork a process and hold an assertion
    that prevents idle sleep as long as that process is running'
  command: caffeinate -i /tmp/evil
- description: 'Prevent a sleep: Prevent a macOS from going to sleep for 4 hours (14400
    seconds)'
  command: caffeinate -u -t 14400
install:
- method: custom
  commands:
  - /usr/bin/caffeinate
detections:
- type: other
  description: No detections at time of publishing
references:
- label: macOS/binaries/caffeinate
  url: https://macosbin.com/bin/caffeinate
- label: caffeinate man page
  url: https://ss64.com/osx/caffeinate.html
features:
- network-intensive
- pipes-stdin
- stealth
---

caffeinate creates assertions to alter system sleep behavior.  If no assertion flags are specified, caffeinate creates an assertion to prevent idle sleep.
If a utility is specified, caffeinate creates the assertions on the utility's behalf, and those assertions will persist for the duration of the utility's execution.
Otherwise, caffeinate creates the assertions directly, and those assertions will persist until caffeinate exits.
