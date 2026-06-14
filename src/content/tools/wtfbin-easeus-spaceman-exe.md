---
trust_level: community
id: wtfbin-easeus-spaceman-exe
namespace: wtf:bin:easeus-spaceman-exe
name: "EaseUS spaceman.exe"
description: "EaseUS and bizarre Scheduled Tasks"
version: "1.0.0"
capabilities:
  - security.persistence.scheduled-task
platforms:
  - windows
techniques:
  - persistence
execution:
  template: "EaseUS spaceman.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://answers.microsoft.com/en-us/windows/forum/all/windows-10-spacemanexe/c60c4d6b-0bca-49e3-8054-68213efbd67a"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/easeus-spaceman-exe/"
---
examples:
  - description: "Execute EaseUS spaceman.exe and observe the unusual behavior"
    command: "EaseUS spaceman.exe"

# EaseUS spaceman.exe

EaseUS and bizarre Scheduled Tasks.



The file is associated with EaseUS Partition Manager or Hard Drive Tools 2003 by TradeTouch.com. Aside from the odd name of the binary, other WTF behaviors include installing to system32 and creating scheduled tasks. These stand out when triaging in PowerShell using `Get-ScheduledTask | Select -Property Author`

*Contributed by Michael Weber "mthrfcknruckus" (@mjweber915)*
