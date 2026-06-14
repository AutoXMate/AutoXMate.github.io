---
trust_level: community
id: macos-defense-evasion-defaults
namespace: macos:defenseevasion:defaults
name: defaults
description: Read, write, and delete user preference values.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - discovery.enumerate
  - security.persistence.hook
platforms:
  - macos
techniques:
  - defense-evasion
  - discovery
  - persistence
execution:
  template: "defaults"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Disable Gatekeeper's auto rearm functionality: The following command can be used to disable Gatekeepers rearm functionality. This command requires root privileges."
    command: "sudo defaults write /Library/Preferences/com.apple.security GKAutoRearm -bool NO"
  - description: "Show mounted servers: Show all mounted servers on the desktop."
    command: "defaults read com.apple.finder \"ShowMountedServersOnDesktop\""
  - description: "Add a login item to the current user: An attacker can use defaults to add a login hook in attempt to gain persistence. This command requires root privileges."
    command: "sudo defaults write /Library/Preferences/com.apple.loginwindow LoginHook gain_persistence.sh"
  - description: "Get Active Directory user info from Jamf Connect: Retrieve Active Directory user info from Jamf Connect defaults configuration."
    command: "defaults read com.jamf.connect.state"
  - description: "Enable Firewall: Enables macOS' default firewall. This command requires root privileges."
    command: "sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 1"
  - description: "Disable Firewall: Disables macOS' default firewall. This command requires root privileges."
    command: "sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 0"
install:
  - method: custom
    commands:
      - "/usr/bin/defaults"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "macOS defaults list: Uncomplete list of macOS defaults commands with demos"
    url: "https://macos-defaults.com/"
  - label: "Insistence on Persistence"
    url: "https://www.huntress.com/blog/insistence-on-persistence"
---

The defaults binary is normally used to interact with the user defaults system, a database of macOS used to manage system settings much like the Windows Registry. The database can be abused by threat actors to change settings in attempt to evade defenses or to gain persistence.