---
trust_level: community
id: macos-discovery-networksetup
namespace: macos:discovery:networksetup
name: networksetup
description: Configure network settings in System Preferences.
author: Jason Trost (@jason_trost)
version: "1.0.0"
capabilities:
  - discovery.enumerate
  - network.commandandcontrol
platforms:
  - macos
techniques:
  - discovery
  - command-and-control
execution:
  template: "networksetup"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "network device enumeration: Use networksetup to display services with corresponding port and device in order they are tried for connecting to a network."
    command: "networksetup -listnetworkserviceorder"
  - description: "Detect connected network hardware: Use networksetup to detect new network hardware and create a default network service on the hardware."
    command: "networksetup -detectnewhardware"
  - description: "network device enumeration: Use networksetup to list all network interfaces, providing name, device name, MAC address."
    command: "networksetup -listallhardwareports"
  - description: "network device enumeration: Use networksetup to list all network interface names."
    command: "networksetup -listallnetworkservices"
  - description: "DNS server enumeration: Use networksetup to get configured DNS servers for a specific interface."
    command: "networksetup -getdnsservers Wi-Fi"
  - description: "Enumerate configured web proxy URL for an interface: Displays web proxy auto-configuration information for the specified interface."
    command: "networksetup -getautoproxyurl \"Thunderbolt Ethernet\""
  - description: "Enumerate configured web proxy for an interface: Displays standard web proxy information for the specified interface."
    command: "networksetup -getwebproxy \"Wi-Fi\""
  - description: "Set the https web proxy for an interface: Use networksetup to set the https web proxy for an interface."
    command: "networksetup -setsecurewebproxy \"Wi-Fi\" 46.226.108.171"
  - description: "Set the http web proxy for an interface: Use networksetup to set the http web proxy for an interface."
    command: "networksetup -setwebproxy \"Wi-Fi\" 46.226.108.171"
  - description: "Set auto proxy URL for an interface: Use networksetup to set the proxy URL for an interface."
    command: "networksetup -setautoproxyurl \"Wi-Fi\" $autoProxyURL"
  - description: "Enable auto proxy state: Use networksetup to enable the proxy auto-config"
    command: "networksetup -setautoproxystate \"Wi-Fi\" on"
install:
  - method: custom
    commands:
      - "/usr/sbin/networksetup"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "Threat Hunting the macOS edition Megan Carney (Report)"
    url: "https://megancarney.com/presentations/ExternalReport_ThreatHuntingMacOS.pdf"
  - label: "GrrCon 2018: Threat Hunting the macOS edition Megan Carney"
    url: "https://www.youtube.com/watch?v=_K4gnSuDkRM&feature=youtu.be"
  - label: "Mac Malware of 2017 - a comprehensive analysis of the new mac malware of 17"
    url: "https://objective-see.org/blog/blog_0x25.html"
  - label: "Ay MaMi - Analyzing a New macOS DNS Hijacker: OSX/MaMi"
    url: "https://objective-see.org/blog/blog_0x26.html"
  - label: "Analyzing OSX.DazzleSpy - A fully-featured cyber-espionage macOS implant"
    url: "https://objective-see.org/blog/blog_0x6D.html"
  - label: "The Mac Malware of 2018 - a comprehensive analysis of the new mac malware of - 18"
    url: "https://objective-see.org/blog/blog_0x3C.html"
  - label: "From The DPRK With Love - analyzing a recent north korean macOS backdoor"
    url: "https://objective-see.org/blog/blog_0x6E.html"
---

networksetup is an extensive tool for reading and setting various network configuration details useful for Discovery and Command and Control.