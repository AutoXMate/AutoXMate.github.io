---
trust_level: community
id: macos-discovery-getfileinfo
namespace: macos:discovery:getfileinfo
name: GetFileInfo
description: Get attributes of files and directories.
author: Chris Campbell (@texasbe2trill)
version: 1.0.0
capabilities:
- discovery.enumerate
platforms:
- macos
techniques:
- discovery
execution:
  template: GetFileInfo
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Iterate through a directory to GetFileInfo: A bash or zsh oneliner
    can provide an attacker with information about specific files of interest.'
  command: for FILE in ~/Downloads/*; do echo $(GetFileInfo $FILE) >> fileinfo.txt;
    sleep 2; done
install:
- method: custom
  commands:
  - /usr/bin/GetFileInfo
detections:
- type: other
  description: No detections at time of publishing
references:
- label: macOS/binaries/GetFileInfo
  url: https://macosbin.com/bin/getfileinfo
features:
- file-system
- local
---

Uses the CommandLine/Terminal to return type, creator, attributes, created, and modified file information of a file or directory.
