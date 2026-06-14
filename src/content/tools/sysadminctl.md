---
trust_level: community
id: macos-execution-sysadminctl
namespace: macos:execution:sysadminctl
name: sysadminctl
description: Create/delete local accounts, guest account, enable SMB/AFP Guest access.
author: Hare Sudhan (@cyb3rbuff)
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.persistence.hook
  - impact.destruction
  - exfiltration.data
platforms:
  - macos
techniques:
  - execution
  - persistence
  - impact
  - exfiltration
execution:
  template: "sysadminctl"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Enable Guest Account: sysadminctl can be used to enable the guest account"
    command: "sudo sysadminctl -guestAccount on\n"
  - description: "Create Local User Account: sysadminctl can be used to create a local user account"
    command: "sudo sysadminctl -addUser randomUser -password \"randomPassword\"\n"
  - description: "Create a Local Admin Account: sysadminctl can be used to create a local admin account"
    command: "sudo sysadminctl -addUser randomUser -password \"randomPassword\" -admin\n"
  - description: "Reset user password: sysadminctl can be used to reset password for a particular user account"
    command: "sudo sysadminctl -resetPasswordFor randomUser -newPassword \"randomPassword\"\n"
  - description: "Delete a local account: sysadminctl can delete the specified user account"
    command: "sudo sysadminctl -deleteUser randomUser\n"
  - description: "Enable SMB Guest Access: sysadminctl can enable SMB Guest Access"
    command: "sudo sysadminctl -smbGuestAccess on\n"
  - description: "Enable AFP Guest Access: sysadminctl can enable AFP Guest Access"
    command: "sudo sysadminctl -afpGuestAccess on\n"
install:
  - method: custom
    commands:
      - "/usr/sbin/sysadminctl"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_create_account.yml"
    description: "Sigma: Creation Of A Local User Account"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_add_user_to_admin_group.yml"
    description: "Sigma: User Added To Admin Group Via Sysadminctl"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_enable_guest_account.yml"
    description: "Sigma: Guest Account Enabled Via Sysadminctl"
references:
  - label: "sysadminctl man page"
    url: "https://ss64.com/mac/sysadminctl.html"
---

sysadminctl can administer system user accounts. sysadminctl can be used to change user passwords, create new 
users (including automatically provisioning the user home folder) or to check the status of a user's SecureToken.
