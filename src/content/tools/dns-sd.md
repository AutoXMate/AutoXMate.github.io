---
trust_level: community
id: macos-discovery-dns-sd
namespace: macos:discovery:dns-sd
name: dns-sd
description: Discover local network services using the DNS-Based Service Discovery (SD) protocol.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - discovery.enumerate
platforms:
  - macos
techniques:
  - discovery
execution:
  template: "dns-sd"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Discover SSH hosts: Hosts serving SSH can be discovered using the _ssh._tcp service string."
    command: "dns-sd -B _ssh._tcp"
  - description: "Discover web hosts: Hosts serving web services can be discovered using the _http._tcp service string."
    command: "dns-sd -B _http._tcp"
  - description: "Discover hosts serving remote screen sharing: Hosts serving remote screen sharing can be discovered using the _rfb._tcp service string."
    command: "dns-sd -B _rfb._tcp"
  - description: "Discover hosts serving SMB: Hosts serving SMB can be discovered using the _smb._tcp service string."
    command: "dns-sd -B _smb._tcp"
install:
  - method: custom
    commands:
      - "/usr/bin/dns-sd"
detections:
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/dns_service_discovery"
    description: "Jamf Protect: Detect dns-sd discovery activity"
references:
  - label: "What does APT Activity Look Like on macOS?"
    url: "https://themittenmac.com/what-does-apt-activity-look-like-on-macos"
  - label: "mDNS / Bonjour Bible - List of Common Service Strings for various vendors"
    url: "https://jonathanmumm.com/tech-it/mdns-bonjour-bible-common-service-strings-for-various-vendors/"
---

dns-sd can be used to interact with the Multicast DNS (mDNS) and DNS Service Discovery (DNS-SD) protocols. The tool is useful for administrators but can also be abused by malicious actors to discover local network services.