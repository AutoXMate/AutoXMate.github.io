---
trust_level: community
id: macos-execution-hdiutil
namespace: macos:execution:hdiutil
name: hdiutil
description: Manipulate disk images using the DiskImages framework.
author: Mark Morowczynsk (@markmorow)
version: 1.0.0
capabilities:
- security.execution.command
- collection.data
platforms:
- macos
techniques:
- execution
- collection
execution:
  template: hdiutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Mount a malicious dmg file: Uses hdiutil to mount a malicious dmg
    file to the system.'
  command: hdiutil mount malicious.dmg
- description: 'Mount a malicious dmg file: Uses hdiutil to mount a malicious dmg
    file to the system.'
  command: hdiutil attach malicious.dmg
- description: 'Mount a malicious iso file: Uses hdiutil to mount a malicious iso
    file to the system.'
  command: hdiutil mount malicious.iso
- description: 'Mount a malicious iso file: Uses hdiutil to mount a malicious iso
    file to the system.'
  command: hdiutil attach malicious.iso
- description: 'Exfiltrate data in dmg file: Uses hdiutil to create a dmg file to
    store exfiltrate data'
  command: hdiutil create -volname "Volume Name" -srcfolder /path/to/folder -ov diskimage.dmg
- description: 'Exfiltrate data in encrypted dmg file: Uses hdiutil to create a dmg
    file to store exfiltrate data'
  command: hdiutil create -encryption -stdinpass -volname "Volume Name" -srcfolder
    /path/to/folder -ov encrypteddiskimage.dmg
install:
- method: custom
  commands:
  - /usr/bin/hdiutil
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_mount.yml
  description: 'Sigma: Disk Image Mounting Via Hdiutil'
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_hdiutil_create.yml
  description: 'Sigma: Disk Image Creation Via Hdiutil'
references:
- label: Microsoft finds new macOS vulnerability, Shrootless, that could bypass System
    Integrity Protection
  url: https://www.microsoft.com/en-us/security/blog/2021/10/28/microsoft-finds-new-macos-vulnerability-shrootless-that-could-bypass-system-integrity-protection/
features:
- local
- pipes-stdin
---

hdiutil manipulates disk images such as DMG and ISO files. You can mount, unmount, create, resize and verify disk images. Including encrypted images.
