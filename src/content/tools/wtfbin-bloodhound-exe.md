---
trust_level: community
id: wtfbin-bloodhound-exe
namespace: wtf:bin:bloodhound-exe
name: "Bloodhound.exe"
description: "Not the Bloodhound you're thinking of"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - windows
techniques:
  - execution
execution:
  template: "Bloodhound.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/14"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/bloodhound-exe/"
---
examples:
  - description: "Execute Bloodhound.exe and observe the unusual behavior"
    command: "Bloodhound.exe"

# Bloodhound.exe

Not the Bloodhound you're thinking of.


   
Silver Bullet Technology's Ranger runs an executable called Bloodhound.exe (`C:\Program Files (x86)\Silver Bullet Technology\Ranger\Logging\Bloodhound.exe`). It doesn't appear to be SpecterOps's Bloodhound tool for Active Directory mapping, it merely shares a namesake.

*Contributed by Dray Agha (@purp1ew0lf)*
