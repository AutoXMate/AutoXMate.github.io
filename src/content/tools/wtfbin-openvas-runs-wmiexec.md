---
trust_level: community
id: wtfbin-openvas-runs-wmiexec
namespace: wtf:bin:openvas-runs-wmiexec
name: OpenVAS runs WMIExec
description: TFW the vuln scanner runs offensive tools
version: 1.0.0
capabilities:
- security.execution.impacket
platforms:
- windows
techniques:
- execution
execution:
  template: OpenVAS runs WMIExec
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/greenbone/openvas-scanner/blob/308cefe338df888814b735d11302f4b7e258bdc3/nasl/nasl_smb.c#L367
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/openvas-runs-wmiexec/
features:
- network-intensive
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute OpenVAS runs WMIExec and observe the unusual behavior"
    command: "OpenVAS runs WMIExec"

# OpenVAS runs WMIExec

TFW the vuln scanner runs offensive tools.


   
When connecting to Windows hosts, OpenVAS will run impacket-wmiexec against the host. The resulting events look identical to a secretsdump run that you'd [hunt for](https://riccardoancarani.github.io/2020-05-10-hunting-for-impacket).

*Contributed by mttaggart*
