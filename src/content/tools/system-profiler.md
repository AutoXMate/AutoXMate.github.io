---
trust_level: community
id: macos-discovery-system-profiler
namespace: macos:discovery:system-profiler
name: system_profiler
description: Reports system hardware and software configuration.
author: Ethan Nay
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "system_profiler"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Listing the available datatypes: List all available sub-systems to get information from."
    command: "system_profiler -listDataTypes"
  - description: "Print hardware information: Prints an overview of the hardware of the current machine, including its model name and serial number."
    command: "system_profiler SPHardwareDataType"
  - description: "Print software information: Prints an overview of the software of the current machine, including the exact macOS version number."
    command: "system_profiler SPSoftwareDataType"
  - description: "Print the information of developer tools: Prints the currently active version of the Xcode developer tools and SDK."
    command: "system_profiler SPDeveloperToolsDataType"
  - description: "Print power and battery information: Prints power and battery information, including the current AC wattage and battery cycle count."
    command: "system_profiler SPPowerDataType"
install:
  - method: custom
    commands:
      - "/usr/sbin/system_profiler"
detections:
  - type: other
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_profiler_discovery.yml"
    description: "System Information Discovery Using System_Profiler"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/system_profiler_activity"
    description: "Jamf Protect: Detect system_profiler activity that gathers system information"
references:
  - label: "macOS/binaries/system_profiler"
    url: "https://macosbin.com/bin/system_profiler"
  - label: "system_profiler man page"
    url: "https://ss64.com/osx/system_profiler.html"
---

system_profiler reports on the hardware and software configuration of the system. It can generate plain text reports or XML reports which can be opened with System Information.app