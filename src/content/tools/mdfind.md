---
trust_level: community
id: macos-recon-mdfind
namespace: macos:recon:mdfind
name: mdfind
description: Locate files using the Spotlight database.
author: Chris Campbell (@texasbe2trill)
version: 1.0.0
capabilities:
- reconnaissance.enumerate
- discovery.enumerate
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- recon
- discovery
- defense-evasion
execution:
  template: mdfind
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Use mdfind to provide live updates to the number of files matching
    the query: A bash or zsh oneliner can cause mdfind to provide an attacker with
    live updates to the number of files on a system.'
  command: mdfind -live passw
- description: 'Use mdfind to search for AWS Keys: Allows an attacker to query the
    filesystem via the CommandLine/Terminal to search for AWS keys.'
  command: mdfind 'kMDItemTextContext == AKIA || kMDItemDisplayName = *AKIA* -onlyin
    ~'
- description: 'Use mdfind to search for apps to infect: Allows an attacker to determine
    if specific applications are installed and can be leveraged'
  command: set appId to do shell script "mdfind kMDItemCFBundleIdentifier = '" & bundleId
    & "'"
install:
- method: custom
  commands:
  - /usr/bin/mdfind
detections:
- type: other
  url: https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/mdfind_search_aws_keys
  description: 'Jamf Protect: Detect activity related to mdfind used to search for
    stored AWS keys'
references:
- label: '''Farming The Apple Orchards: Living off the Land Techniques'' - Chris Ross
    & Cedric Owens'
  url: https://youtu.be/Snwh4mMe-Cg?t=45
- label: '''Zero-Day TCC bypass discovered in XCSSET malware'' - Jaron Bradley, Ferdous
    Saljooki, Stuart Ashenbrenner'
  url: https://www.jamf.com/blog/zero-day-tcc-bypass-discovered-in-xcsset-malware/
features:
- file-system
- local
- pipes-stdout
- stealth
---

mdfind to locate files on MacOS by searching a pre-built database. It is a command-line alternative to Spotlight in MacOS
