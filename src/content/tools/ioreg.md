---
trust_level: community
id: macos-discovery-ioreg
namespace: macos:discovery:ioreg
name: ioreg
description: Displays a hierarchial view of the I/O Kit registry.
author: Cedric Owens (@cedowens)
version: 1.0.0
capabilities:
- discovery.enumerate
- collection.data
platforms:
- macos
techniques:
- discovery
- collection
execution:
  template: ioreg
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Use ioreg to check whether the remote macOS screen is locked.: The
    following command will display a list of keys that contain "CGSSession". If the
    key "CGSSessionScreenIsLocked" is present, the screen is actively locked.'
  command: ioreg -n Root -d1 -a | grep CGSSession
- description: 'Use ioreg to check whether the host is on a physical machine or a
    VM: Check the output of this command (specifically the IOPlatformSerialNumber,
    board-id, and manufacturer fields) to check whether or not this host is in a virtual
    machine.'
  command: ioreg -rd1 -c IOPlatformExpertDevice
- description: 'Use ioreg to check USB device vendor names: Grep for "USB Vendor Name"
    values to view USB vendor names. On virtualized hardware these values may contain
    the hypervisor name such as "VirtualBox". This is an additional way to check for
    virtualization.'
  command: ioreg -rd1 -c IOUSBHostDevice
- description: 'Check all ioreg properties for hypervisor names.: Grep for "virtual
    box", "oracle", and "vmware" from the output of the ioreg -l command. This is
    an additional way to check for virtualization.'
  command: ioreg -l
install:
- method: custom
  commands:
  - /usr/sbin/ioreg
detections:
- type: other
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_ioreg_discovery.yml
  description: System Information Discovery Using Ioreg
- type: other
  url: https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/lockscreen_check
  description: 'Jamf Protect: Ioreg used to detect if the screen is locked'
references:
- label: 'Evasions: macOS'
  url: https://evasions.checkpoint.com/src/MacOS/macos.html
- label: SwiftBelt-JXA Situational Awareness Tool
  url: https://github.com/cedowens/SwiftBelt-JXA/blob/main/SwiftBelt-JXA.js#520
features:
- pipes-stdout
---

The I/O Kit registry (ioreg) is a useful binary that can be used to gather data such as detecting if a VM is used, getting USB device vendor names, checking if a screen is locked, etc.
