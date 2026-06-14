---
trust_level: community
id: macos-discovery-notifyutil
namespace: macos:discovery:notifyutil
name: notifyutil
description: Monitor and post Darwin notifications for inter-process communication and system event monitoring.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - discovery.enumerate
  - collection.data
  - network.commandandcontrol
  - security.defenseevasion.bypass
  - security.privilegeescalation.shell
platforms:
  - macos
techniques:
  - discovery
  - collection
  - command-and-control
  - defense-evasion
  - privilege-escalation
execution:
  template: "notifyutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Monitor system events for reconnaissance: An attacker can register for system notification keys to detect when the user locks their screen, changes network state, or other system events without using more easily detected APIs. The following example monitors for screen lock events."
    command: "notifyutil -w com.apple.screenIsLocked"
  - description: "Establish covert inter-process communication channel: Threat actors can use Darwin notifications as a covert IPC mechanism to coordinate between malicious processes. By posting and monitoring custom notification keys with associated state values, malware components can exchange commands and data without using traditional IPC methods that may be monitored."
    command: "# Sender process\nnotifyutil -p com.example.hidden.channel -s com.example.hidden.channel 1337\n\n# Receiver process in another terminal/process\nnotifyutil -1 com.example.hidden.channel -g com.example.hidden.channel\n"
  - description: "Monitor network state changes for data exfiltration timing: An attacker can monitor for network configuration changes to determine optimal timing for data exfiltration. This allows malware to detect when the system connects to networks and adjust behavior accordingly."
    command: "notifyutil -w com.apple.system.config.network_change"
  - description: "Monitor timezone changes for geolocation tracking: Monitoring timezone change notifications can help an attacker track when a target device moves between geographic locations or when users travel, providing intelligence about the target's physical location and movement patterns."
    command: "notifyutil -w com.apple.system.timezone"
  - description: "Monitor login/logout events for privilege escalation timing: By monitoring authentication-related notification keys, an attacker can detect login and logout events to time privilege escalation attempts or other malicious activities when defenses may be weakened during authentication transitions."
    command: "notifyutil -w com.apple.loginwindow.logout -w com.apple.springboard.attemptactivationend"
  - description: "Query system notification state values for reconnaissance: Threat actors can query state values of system notification keys to gather information about the current system configuration without executing more suspicious commands."
    command: "notifyutil -g com.apple.system.timezone\nnotifyutil -g com.apple.loginwindow.logout\nnotifyutil -g com.apple.screenIsLocked\n"
install:
  - method: custom
    commands:
      - "/usr/bin/notifyutil"
detections:
  - type: other
    description: "Monitor notifyutil execution with suspicious notification keys"
  - type: other
    description: "Detect notifyutil monitoring non-standard or custom notification keys (keys not starting with com.apple)"
  - type: other
    description: "Monitor long-running notifyutil processes (using -w flag for sustained monitoring)"
  - type: other
    description: "Detect notifyutil usage in conjunction with known malware indicators or suspicious parent processes"
references:
  - label: "Quick Tip: system-wide notifications with notifyutil"
    url: "https://brettterpstra.com/2012/07/04/quick-tip-system-wide-notifications-with-notifyutil/"
  - label: "Darwin Notification Concepts - Apple Developer Documentation"
    url: "https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/MacOSXNotifcationOv/DarwinNotificationConcepts/DarwinNotificationConcepts.html"
  - label: "notify(3) manual page"
    url: "https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/notify.3.html"
---

The notifyutil binary is a command-line interface to the notify(3) API and notifyd(8) daemon, which manages Darwin notifications on macOS. This utility enables posting notifications, monitoring system-wide notification keys, and manipulating state values associated with notification keys. While designed for legitimate inter-process communication (IPC), notifyutil can be abused by threat actors to monitor system events (like screen lock, network changes, timezone updates), establish covert communication channels between processes, or gather intelligence about system state changes without triggering traditional security monitoring.