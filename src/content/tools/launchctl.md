---
trust_level: community
id: macos-execution-launchctl
namespace: macos:execution:launchctl
name: launchctl
description: Interact with LaunchAgents and LaunchDaemons.
author: Josh Carullo
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.persistence.hook
platforms:
  - macos
techniques:
  - execution
  - persistence
execution:
  template: "launchctl"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Use launchctl to execute an application: A oneliner that will load a plist as a LaunchAgent or LaunchDaemon, achieving persistence on a target machine. This command requires root privileges."
    command: "sudo launchctl load /Library/LaunchAgent/com.apple.installer"
  - description: "Persistent launch agent: Creation of a persistent launch agent called with $HOME/Library/LaunchAgents/com.apple.updates.plist"
    command: "launchctl load -w ~/Library/LaunchAgents/com.apple.updates.plist"
install:
  - method: custom
    commands:
      - "/bin/launchctl"
detections:
  - type: other
    description: "LaunchAgents and LaunchDaemons must have a plist file on disk in the root, system, or user Library directory. Monitoring for plist's with executables located in /tmp or /Shared could identify suspicious applications."
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/launchctl_unload_and_bootout_events"
    description: "Jamf Protect: Detect launchctl activity that unloads or bootsout specific service"
references:
  - label: "20 Common Tools & Techniques used by macOS threat Actors & Malware"
    url: "https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/"
  - label: "Mitre Attack Technique: launchctl T1569"
    url: "https://attack.mitre.org/techniques/T1569/001/"
  - label: "MITRE ATT&CK T1543.001  Create or Modify System Process: Launch Agent "
    url: "https://attack.mitre.org/techniques/T1543/001/"
  - label: "Komplex OS X Trojan (Sofacy)"
    url: "https://unit42.paloaltonetworks.com/unit42-sofacys-komplex-os-x-trojan/"
---

launchctl can be used to load, start, stop, and unload macOS services. It is a command-line frontend to launchd.