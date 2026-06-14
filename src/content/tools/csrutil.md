---
trust_level: community
id: macos-defense-evasion-csrutil
namespace: macos:defenseevasion:csrutil
name: csrutil
description: Configure or view system security policies.
author: Megan Carney (https://infosec.exchange/@PwnieFan)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - reconnaissance.enumerate
  - discovery.enumerate
platforms:
  - macos
techniques:
  - defense-evasion
  - recon
  - discovery
execution:
  template: "csrutil"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Disable SIP: disable SIP (System Integrity Protection) - requires booting into recovery mode"
    command: "csrutil disable"
  - description: "Disable authenticated-root: When authenticated-root is disabled, booting is allowed from non-sealed system snapshots - requires booting into recovery mode"
    command: "csrutil authenticated-root disable"
  - description: "Add a netboot server: Insert a new IPv4 address in the list of allowed NetBoot sources"
    command: "csrutil netboot add <address>"
  - description: "Map infrastructure: List allowed NetBoot sources"
    command: "csrutil netboot list"
  - description: "Determine if SIP is enabled: Determine if System Integrity Protection is enabled"
    command: "csrutil status"
install:
  - method: custom
    commands:
      - "/usr/bin/csrutil"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_disable.yml"
    description: "Sigma: System Integrity Protection (SIP) Disabled"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_csrutil_status.yml"
    description: "Sigma: System Integrity Protection (SIP) Enumeration"
references:
  - label: "Discussion on how SIP interacts with bless and netboot"
    url: "https://developer.apple.com/forums/thread/4002"
  - label: "MITRE ATT&CK T1518.001 Software Discovery: Security Software Discovery"
    url: "https://attack.mitre.org/techniques/T1518/001/"
  - label: "The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSSBackdoor Planting in Safari, and LeveragesTwo Zero-day Exploits"
    url: "https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf"
---

Used to enable/disable SIP, configure netboot and authenticated-root settings