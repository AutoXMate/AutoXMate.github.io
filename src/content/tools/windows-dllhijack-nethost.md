---
trust_level: community
id: windows-dllhijack-nethost
namespace: windows:dllhijack:nethost
name: nethost.dll
description: "nethost.dll — Sideloading hijacking (Microsoft)"
author: "Josh Allman"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "nethost.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://ctrlaltintel.com/research/FudCrypt-analysis-1/"
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/dotnet/core/tutorials/netcore-hosting"
  - label: "Reference"
    url: "https://protonvpn.com/support/install-windows-vpn"
  - label: "Reference"
    url: "https://protonvpn.com/support/protonvpn-windows-vpn-application/"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/nethost.html"
---
examples:
  - description: "Place malicious nethost.dll in the search order location"
    command: "copy malicious.dll \"%PROGRAMFILES%\\dotnet\\packs\\Microsoft.NETCore.App.Host.win-x64\\%VERSION%\\runtimes\\win-x64\\native\\nethost.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%PROGRAMFILES%\\Proton\\VPN\\ProtonVPN.exe\""

# nethost.dll

**Vendor:** Microsoft

**Expected Location:** %PROGRAMFILES%\dotnet\packs\Microsoft.NETCore.App.Host.win-x64\%VERSION%\runtimes\win-x64\native

**Vulnerable Executables:**
- %PROGRAMFILES%\Proton\VPN\ProtonVPN.exe (Sideloading)

**Acknowledgement:** Josh Allman
