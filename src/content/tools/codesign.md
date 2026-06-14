---
trust_level: community
id: macos-defense-evasion-codesign
namespace: macos:defenseevasion:codesign
name: codesign
description: Create, manipulate and verify code signatures.
author: Thijs Xhaflaire
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - defense-evasion
execution:
  template: "codesign"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Ad-hoc codesigning an app bundle: This command forcefully re-signs the MyApp.app application with an ad-hoc signature, applying the signature deeply to all nested code within the app"
    command: "codesign --force --deep -s - MyApp.app"
install:
  - method: custom
    commands:
      - "/usr/bin/codesign"
detections:
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/adhoc_codesigning.yaml"
    description: "Jamf Protect: Detect ad-hoc codesigning activity"
references:
  - label: "When Apple Admits macOS Malware Is A Problem – It’s Time To Take Notice"
    url: "https://www.sentinelone.com/blog/when-apple-admits-macos-malware-is-a-problem-its-time-to-take-notice/"
  - label: "codesign man page"
    url: "https://ss64.com/mac/codesign.html"
---

The codesign command is used to create, check, and display code signatures, as well as inquire into the dynamic status of signed code in the system.