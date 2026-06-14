---
trust_level: community
id: macos-defense-evasion-pkill
namespace: macos:defenseevasion:pkill
name: pkill
description: Kill processes by name or pattern.
author: Jason Phang Vern - Onn
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - impact.destruction
platforms:
  - macos
techniques:
  - defense-evasion
  - impact
execution:
  template: "pkill"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Kill security tools: Terminate defensive processes like firewalls, AV, or monitoring tools."
    command: "pkill -f \"Little Snitch|ESET|osqueryd|Falcon\""
  - description: "Force kill processes with SIGKILL: Use the -9 signal to forcefully terminate processes that may not respond to normal termination signals. Useful for killing hung security tools."
    command: "pkill -9 osqueryd"
  - description: "Kill all processes for a user: Terminate all processes belonging to a specific user, potentially ending user sessions or disrupting monitoring."
    command: "pkill -u username"
  - description: "Kill logging and monitoring daemons: Terminate system logging and monitoring processes to evade detection."
    command: "pkill -f \"syslog|auditd|osqueryd|esensor|nessusd\""
  - description: "Kill process by exact name match: Use exact matching with -x flag to kill specific process by exact name rather than pattern."
    command: "pkill -x com.apple.Safari"
install:
  - method: custom
    commands:
      - "/usr/bin/pkill"
detections:
  - type: other
    description: "Process execution monitoring for pkill"
  - type: other
    description: "Endpoint Detection - pkill targeting security tools"
references:
  - label: "Fake DeepSeek Site Infects Mac Users with Atomic (AMOS) Stealer"
    url: "https://www.esentire.com/blog/fake-deepseek-site-infects-mac-users-with-atomic-stealer"
  - label: "SS64 pkill man page"
    url: "https://ss64.com/mac/pkill.html"
---

pkill is a Unix utility available on macOS that sends signals to processes matching a given name or pattern. While intended for legitimate process management, threat actors can abuse pkill to terminate security tools, monitoring daemons, or user applications for defense evasion. It's particularly valuable to attackers as a Living Off the Land technique that avoids bringing custom binaries onto the system.