---
trust_level: community
id: wtfbin-eset-protection-suite
namespace: wtf:bin:eset-protection-suite
name: ESET Protection Suite
description: Everybody loves a big DNS query!
version: 1.0.0
capabilities:
- network.exfiltration.dns
platforms:
- windows
techniques:
- exfiltration
execution:
  template: ESET Protection Suite
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://support.eset.com/en/kb332-ports-and-addresses-required-to-use-your-eset-product-with-a-third-party-firewall
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/eset-protection-suite/
features:
- network-intensive
---

examples:
  - description: "Run the binary and monitor DNS exfiltration"
    command: "ESET Protection Suite"

# ESET Protection Suite

Everybody loves a big DNS query!



Various modules of ESET protection suite (Antispam, Parental Controls, LiveGrid) perform odd DNS lookups to subdomains of `e5.sk domain.`

Example:

```
TXT? oa5jhh3yxkgu5kpwgnjmgk54pubqeaqbaeaq.a.e.e5.sk.
TXT? wzxh7gqaszmunhqg3g5ouiiuwebqeaqbaeaq.a.e.e5.sk.
TXT? xegjkvpuklfebhejqeve4mltsmbqeaqbaeaq.a.e.e5.sk.
TXT? vscxkxbn55aelaru6a6y3dxznebqeaqbaeaq.a.e.e5.sk.
TXT? dc5wtaihc6luvphgub6laccokebqeaqbaeaq.a.e.e5.sk.
```

*Contributed by Petr Špaček (@pspacek)*
