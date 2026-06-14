---
trust_level: community
id: wtfbin-mcafee-antivirus
namespace: wtf:bin:mcafee-antivirus
name: "McAfee Antivirus"
description: "McAfee also loves big DNS queries!"
version: "1.0.0"
capabilities:
  - network.exfiltration.dns
platforms:
  - windows
techniques:
  - exfiltration
execution:
  template: "McAfee Antivirus"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/33"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/mcafee-antivirus/"
---
examples:
  - description: "Run the binary and monitor DNS exfiltration"
    command: "McAfee Antivirus"

# McAfee Antivirus

McAfee also loves big DNS queries!


   
Various McAfee performs odd DNS lookups to subdomains of `avqs.mcafee.com` and `avts.mcafee.com` domains.
Example:

```
A? a-0.19-a3000081.c930082.1838.11b0.2fca.400.0.n7dbrrk87wfrd2gm1699ghv8hi.avqs.mcafee.com.
A? 13-0.19-b3000081.30483.1838.11b4.2fca.210.0.jsdhk1cfzc4r9jrf2j214zd4gi.avqs.mcafee.com.
A? 13-0.19-b3000081.a0082.1838.11b4.2fca.210.0.4fk9i42wg1l1rlfrgvlpsv7a9q.avqs.mcafee.com.
A? 13-0.19-b3000081.60082.1838.11b4.2fca.210.0.uqnk1rubb52k9unam8919hj6wq.avqs.mcafee.com.
A? 13-0.19-b3000081.8a70082.1838.11b4.2fca.210.0.bklpbm2z81gc949wv8qr3spea6.avqs.mcafee.com.
A? 13-0.19-b3000081.60082.1838.11b4.2fca.210.0.nuthnwa7a65azzqaij3t43ts1i.avqs.mcafee.com.
A? 13-0.19-b3000081.60082.1838.11b4.2fca.210.0.lqmag7m5gq7i6h16d6emea6fwv.avqs.mcafee.com.
A? 13-0.19-b3000081.10082.1838.11b4.2fca.210.0.gkmrckah4wcjc96fvbratcmn26.avqs.mcafee.com.
A? 14-0.19-b3000489.2.1644.95b.3ea3.210.0.7ahnlkt1uiliactc2cfvqqnjcv.avts.mcafee.com.
```

*Contributed by Petr Špaček (@pspacek)*
