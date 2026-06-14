---
trust_level: community
id: wtfbin-samsung-mobilewips
namespace: wtf:bin:samsung-mobilewips
name: Samsung MobileWips
description: Bizarre DNS requests on Samsung phones
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- cross-platform
techniques:
- execution
execution:
  template: Samsung MobileWips
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/27
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/samsung-mobilewips/
features:
- pipes-stdin
- process-manip
---

examples:
  - description: "Run the binary and monitor DNS exfiltration"
    command: "Samsung MobileWips"

# Samsung MobileWips

Bizarre DNS requests on Samsung phones.


   
Samsung MobileWips (presumably a Wireless Intrusion Prevention System) is a default system app on certain Android OS versions. It has been observed making DNS requests to google.com.onion, which will trigger network/DNS-related alerts, such as the Sigma rule [Query Tor Onion Address](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_tor_onion.yml). This domain does not resolve to an IP address, and is not accessible via Tor. It appears to have been added as some sort of DNS check by an Android developer with poor taste!

*Contributed by Micah Babinski (@mbabinski)*
