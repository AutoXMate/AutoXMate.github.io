---
trust_level: community
id: wtfbin-windows-tcp-connections-on-high-ports
namespace: wtf:bin:windows-tcp-connections-on-high-ports
name: "Windows TCP Connections on High Ports"
description: "Windows uses random high service ports for a variety of functions"
version: "1.0.0"
capabilities:
  - network.transfer.generic
platforms:
  - windows
techniques:
  - exfiltration
execution:
  template: "Windows TCP Connections on High Ports"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/windows-tcp-connections-on-high-ports/"
---
examples:
  - description: "Execute Windows TCP Connections on High Ports and observe the unusual behavior"
    command: "Windows TCP Connections on High Ports"

# Windows TCP Connections on High Ports

Windows uses random high service ports for a variety of functions. 



Without knowing this, these connections seem malicious but should be considered benign without a second source of suspicion.

*Contributed by Ductape and Dreams*
