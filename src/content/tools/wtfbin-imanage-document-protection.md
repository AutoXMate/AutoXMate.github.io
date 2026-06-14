---
trust_level: community
id: wtfbin-imanage-document-protection
namespace: wtf:bin:imanage-document-protection
name: iManage Document Protection
description: Random file extensions from iManage
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: iManage Document Protection
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/39
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/imanage-document-protection/
features:
- file-system
- local
- pipes-stdin
---

examples:
  - description: "Execute iManage Document Protection and observe the unusual behavior"
    command: "iManage Document Protection"

# iManage Document Protection

Random file extensions from iManage


   
When Office documents are protected by iManage, upon opening them they create script files in `%TEMP%` with a randomly generated file extension (such as `.hta`, `.sct`, `.inf`, `.cpl`, `.wsf`, etc.). This happens because iManage implements the `Path.GetRandomFileName` Method to handle this behavior. So while most instances result in files that look like `x191krbu.idj`, sometimes they end up being written like `x191krbu.hta` which likely will wreak havoc on a good defender's SIEM rules.

*Contributed by Chris Beckett (@cbecks_2)*
