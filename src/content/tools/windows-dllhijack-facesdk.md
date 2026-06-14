---
trust_level: community
id: windows-dllhijack-facesdk
namespace: windows:dllhijack:facesdk
name: facesdk.dll
description: "facesdk.dll — Sideloading hijacking (Luxand)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "facesdk.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/facesdk.html"
---
examples:
  - description: "Place malicious facesdk.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\luxand\\facesdk\\bin\\win64\\facesdk.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\luxand\\facesdk\\bin\\win64\\FacialFeatureDemo.exe\""

# facesdk.dll

**Vendor:** Luxand

**Expected Location:** %PROGRAMFILES%\luxand\facesdk\bin\win64

**Vulnerable Executables:**
- %PROGRAMFILES%\luxand\facesdk\bin\win64\FacialFeatureDemo.exe (Sideloading)
