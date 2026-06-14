---
trust_level: community
id: macos-recon-dsexport
namespace: macos:recon:dsexport
name: dsexport
description: Export data from an Open Directory directory services server.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - reconnaissance.enumerate
  - discovery.enumerate
platforms:
  - macos
techniques:
  - recon
  - discovery
execution:
  template: "dsexport"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Export local host users: Export the local host user information to a file"
    command: "dsexport local_users.txt /Local/Default dsRecTypeStandard:Users"
  - description: "Export local host groups: Export the local host group information to a file"
    command: "dsexport local_groups.txt /Local/Default dsRecTypeStandard:Groups"
install:
  - method: custom
    commands:
      - "/usr/bin/dsexport"
detections:
  - type: other
    description: "No detections at time of publishing"
---

dsexport is a command-line utility designed to export records from the directory services database on a local host or from a connected LDAP service. The tool can be used to gather information about users, groups, and computers. The tool can also be used to export the directory services database to a file for offline analysis.