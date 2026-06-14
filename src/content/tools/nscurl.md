---
trust_level: community
id: macos-defense-evasion-nscurl
namespace: macos:defenseevasion:nscurl
name: nscurl
description: Download, upload, and read files.
author: Leo Pitt (@_D00mfist)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - network.commandandcontrol
platforms:
  - macos
techniques:
  - defense-evasion
  - command-and-control
execution:
  template: "nscurl"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Download file: Download file and ignore cert checking"
    command: "nscurl -k https://google.com -o /private/tmp/google"
  - description: "Download file: Download file to the Downloads directory using -dl"
    command: "nscurl https://google.com -dl"
  - description: "Download file: Download file to a designated directory using -dir"
    command: "nscurl https://google.com -dir /private/tmp/google"
install:
  - method: custom
    commands:
      - "/usr/bin/nscurl"
detections:
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/all_curl_activity"
    description: "Jamf Protect: Detect all curl and nscurl activity"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/file_download_curl_insecure"
    description: "Jamf Protect: Detect file downloads using the insecure argument for curl and nscurl"
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_nscurl_usage.yml"
    description: "Sigma: File Download Via Nscurl - MacOS"
references:
  - label: "How to Diagnose App Transport Security Issues using nscurl and OpenSSL"
    url: "https://www.agnosticdev.com/content/how-diagnose-app-transport-security-issues-using-nscurl-and-openssl"
  - label: "Living-off-the-Land: Exploring macOS LOOBins and Crafting Detection Rules - nscurl"
    url: "https://danielcortez.substack.com/p/living-off-the-land-exploring-macos"
---

macOS version of curl that is used to download files to a target without applying the quarantine extended attribute