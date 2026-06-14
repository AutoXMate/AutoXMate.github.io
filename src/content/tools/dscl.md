---
trust_level: community
id: macos-discovery-dscl
namespace: macos:discovery:dscl
name: dscl
description: Interact with Directory Services.
author: Jonathan Bar Or (@yo_yo_yo_jbo)
version: 1.0.0
capabilities:
- discovery.enumerate
- security.persistence.hook
platforms:
- macos
techniques:
- discovery
- persistence
execution:
  template: dscl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Local user enumeration: Enumerate all local users.'
  command: 'dscl . -list /Users

    dscl . list /Users

    dscl . ls /Users

    '
- description: 'Active Directory user enumeration: Enumerate all Active Directory
    users.'
  command: 'dscl "/Active Directory/TEST/All Domains" -list /Users

    dscl "/Active Directory/TEST/All Domains" list /Users

    dscl "/Active Directory/TEST/All Domains" ls /Users

    '
- description: 'Local user information gathering: Gain useful local user information
    such as when their password was last set, their keyboard layout, their avatar,
    their home directory, UID and default shell.'
  command: 'dscl . -read /Users/$USERNAME

    dscl . read /Users/$USERNAME

    dscl . cat /Users/$USERNAME

    '
- description: 'Active Directory user information gathering: Gain useful Active Directory
    user information such as when their password was last set, their keyboard layout,
    their avatar, their home directory, UID and default shell.'
  command: 'dscl "/Active Directory/TEST/All Domains" -read /Users/$USERNAME

    dscl "/Active Directory/TEST/All Domains" read /Users/$USERNAME

    dscl "/Active Directory/TEST/All Domains" cat /Users/$USERNAME

    '
- description: 'Local group enumeration: Enumerate all local groups.'
  command: 'dscl . -list /Groups

    dscl . list /Groups

    dscl . ls /Groups

    '
- description: 'Active Directory group enumeration: Enumerate all Active Directory
    groups.'
  command: 'dscl "/Active Directory/TEST/All Domains" -list /Groups

    dscl "/Active Directory/TEST/All Domains" list /Groups

    dscl "/Active Directory/TEST/All Domains" ls /Groups

    '
- description: 'Local group information gathering: Gain useful local group information
    such as which users belong to that group, SMB SIDs and group ID. Especially useful
    for the "admin" group.'
  command: 'dscl . -read /Groups/$GROUPNAME

    dscl . read /Groups/$GROUPNAME

    dscl . cat /Groups/$GROUPNAME

    '
- description: 'Active Directory group information gathering: Gain useful Active Directory
    group information such as which users belong to that group, SMB SIDs and group
    ID. Especially useful for the "admin" group.'
  command: 'dscl "/Active Directory/TEST/All Domains" -read /Groups/$GROUPNAME

    dscl "/Active Directory/TEST/All Domains" read /Groups/$GROUPNAME

    dscl "/Active Directory/TEST/All Domains" cat /Groups/$GROUPNAME

    '
- description: 'Computer enumeration: Enumerate all computers in an Active Directory.'
  command: 'dscl  "/Active Directory/TEST/All Domains" -list /Computers

    dscl  "/Active Directory/TEST/All Domains" list /Computers

    dscl  "/Active Directory/TEST/All Domains" ls /Computers

    '
- description: 'Share enumeration: Enumerate all shares.'
  command: 'dscl . -list /SharePoints

    dscl . list /SharePoints

    dscl . ls /SharePoints

    '
- description: 'Password policy discovery: Gain password policy information'
  command: 'dscl . -read /Config/shadowhash

    dscl . read /Config/shadowhash

    dscl . cat /Config/shadowhash

    '
- description: 'Change a user password: Change an existing user''s password.'
  command: dscl . passwd /Users/$USERNAME oldPassword newPassword
- description: 'Local account creation: Create a local account'
  command: dscl -create
install:
- method: custom
  commands:
  - /usr/bin/dscl
detections:
- type: other
  url: https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/user_created_by_dscl
  description: 'Jamf Protect: Detect user account creation with dscl'
references:
- label: MacOS Red Teaming - HackTricks
  url: https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation/macos-red-teaming
- label: 'MITRE ATT&CK T1136.001 Create Account: Local Account'
  url: https://attack.mitre.org/techniques/T1136/001/
features:
- process-manip
---

An extensive tool for communicating with the Directory Services, useful for Discovery.
