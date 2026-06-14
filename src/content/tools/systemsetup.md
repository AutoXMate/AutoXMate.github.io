---
trust_level: community
id: macos-lateral-movement-systemsetup
namespace: macos:lateralmovement:systemsetup
name: systemsetup
description: Enable remote login, remote apple events for the machine
author: Hare Sudhan (@cyb3rbuff)
version: 1.0.0
capabilities:
- network.lateralmovement
platforms:
- macos
techniques:
- lateral-movement
execution:
  template: systemsetup
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Enable Remote Login: systemsetup can be used to enable SSH for remote
    login'
  command: 'sudo systemsetup -setremotelogin on

    '
- description: "Enable Remote Apple Events: systemsetup can be used to enable Remote\
    \ Apple Events. \nSet whether the system responds to events sent by other computers\
    \ (such as AppleScripts).\n"
  command: 'sudo systemsetup -setremoteappleevents on

    '
install:
- method: custom
  commands:
  - /usr/sbin/systemsetup
detections:
- type: other
  url: https://www.elastic.co/guide/en/security/current/remote-ssh-login-enabled-via-systemsetup-command.html
  description: Command line argument detection containing (args contain systemsetup
    AND (-setremoteappleevents OR -setremotelogin) AND on)
- type: other
  url: https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/systemsetup_activity
  description: 'Jamf Protect: Detect systemsetup activity that enables remotelogin
    or appleremoteevents'
references:
- label: systemsetup man page
  url: https://ss64.com/osx/systemsetup.html
features:
- network-intensive
- remote
---

systemsetup configures certain per-machine settings typically configured in the System Preferences application.
The systemsetup command requires at least "admin" privileges to run.
