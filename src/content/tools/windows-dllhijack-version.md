---
trust_level: community
id: windows-dllhijack-version
namespace: windows:dllhijack:version
name: version.dll
description: "version.dll — Sideloading hijacking (Microsoft)"
author: "Chris Spehn"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "version.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://securityintelligence.com/posts/windows-features-dll-sideloading/"
  - label: "Reference"
    url: "https://github.com/xforcered/WFH"
  - label: "Reference"
    url: "https://twitter.com/an0n_r0/status/1544472352657915904"
  - label: "Reference"
    url: "https://www.cyjax.com/resources/blog/a-sting-on-bing-bumblebee-delivered-through-bing-seo-poisoning-campaign/"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/96480ef5ccfa8fcb0646538c440103d97ab741ed83f4c2bcb7b4717569f88770/community"
  - label: "Reference"
    url: "https://ctrlaltintel.com/research/FudCrypt-analysis-1/"
  - label: "Reference"
    url: "https://www.iobit.com/en/iobit-unlocker"
  - label: "Reference"
    url: "https://www.iobit.com/product-manuals/unlocker-help"
  - label: "Reference"
    url: "https://community.ccleaner.com/t/c-program-files-ccleaner-ccleanerbugreport-exe-as-part-of-v6-04-pro/77580"
  - label: "Reference"
    url: "https://help.webex.com/article/dluqwo/Executable-files-used-by-Webex-App-on-Windows"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/version.html"
---
examples:
  - description: "Place malicious version.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\version.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\agentservice.exe\""

# version.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\agentservice.exe (Sideloading)
- %SYSTEM32%\certutil.exe (Sideloading)
- %SYSTEM32%\choice.exe (Sideloading)
- %SYSTEM32%\clip.exe (Sideloading)
- %SYSTEM32%\cmstp.exe (Sideloading)
- %SYSTEM32%\cofire.exe (Sideloading)
- %SYSTEM32%\cscript.exe (Sideloading)
- %SYSTEM32%\diskpart.exe (Sideloading)
- %SYSTEM32%\diskraid.exe (Sideloading)
- %SYSTEM32%\dism.exe (Sideloading)
- %SYSTEM32%\driverquery.exe (Sideloading)
- %SYSTEM32%\forfiles.exe (Sideloading)
- %SYSTEM32%\fxssvc.exe (Sideloading)
- %SYSTEM32%\ie4ushowie.exe (Sideloading)
- %SYSTEM32%\iexpress.exe (Sideloading)
- %SYSTEM32%\msconfig.exe (Sideloading)
- %SYSTEM32%\mstsc.exe (Sideloading)
- %SYSTEM32%\openfiles.exe (Sideloading)
- %SYSTEM32%\presentationhost.exe (Sideloading)
- %SYSTEM32%\psr.exe (Sideloading)
- %SYSTEM32%\RelPost.exe (Sideloading)
- %SYSTEM32%\sfc.exe (Sideloading)
- %SYSTEM32%\sigverif.exe (Sideloading)
- %SYSTEM32%\systeminfo.exe (Sideloading)
- %SYSTEM32%\taskkill.exe (Sideloading)
- %SYSTEM32%\tasklist.exe (Sideloading)
- %SYSTEM32%\timeout.exe (Sideloading)
- %SYSTEM32%\unregmp2.exe (Sideloading)
- %SYSTEM32%\verifiergui.exe (Sideloading)
- %SYSTEM32%\vsgraphicsdesktopengine.exe (Sideloading)
- %SYSTEM32%\waitfor.exe (Sideloading)
- %SYSTEM32%\wextract.exe (Sideloading)
- %SYSTEM32%\where.exe (Sideloading)
- %SYSTEM32%\whoami.exe (Sideloading)
- %SYSTEM32%\winsat.exe (Sideloading)
- %SYSTEM32%\wscript.exe (Sideloading)
- %APPDATA%\Zoom\bin\Zoom.exe (Sideloading)
- %SYSTEM32%\icardagt.exe (Sideloading)
- %LOCALAPPDATA%\Microsoft\OneDrive\%VERSION%\Microsoft.SharePoint.exe (Sideloading)
- %PROGRAMFILES%\IObit\IObit Unlocker\IObitUnlocker.exe (Sideloading)
- %PROGRAMFILES%\CCleaner\CCleanerBugReport.exe (Sideloading)
- %PROGRAMFILES%\Cisco Spark\CiscoCollabHost.exe (Sideloading)

**Acknowledgement:** Chris Spehn

**Acknowledgement:** an0n

**Acknowledgement:** Josh Allman
