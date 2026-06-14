---
trust_level: community
id: wtfbin-sophos-web-protection
namespace: wtf:bin:sophos-web-protection
name: Sophos Web Protection (sophosxl.net)
description: Do you like giant DNS queries? Sophos does
version: 1.0.0
capabilities:
- network.exfiltration.dns
platforms:
- cross-platform
techniques:
- exfiltration
execution:
  template: Sophos Web Protection
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://support.sophos.com/support/s/article/KB-000034570?language=en_US
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/sophos-web-protection/
features:
- network-intensive
---

examples:
  - description: "Run the binary and monitor DNS exfiltration"
    command: "Sophos Web Protection"

# Sophos Web Protection (sophosxl.net)

Do you like giant DNS queries? Sophos does.



Sophos Web Protection, for reasons surpassing understanding, performs DNS lookups using b64-encoded data as subdomains to sophosxl.net. This creates a gigantic amount of DNS queries, all of which look like data exfil, because technically they are.

*Contributed by mttaggart*
