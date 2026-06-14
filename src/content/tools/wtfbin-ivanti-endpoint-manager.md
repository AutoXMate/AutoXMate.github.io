---
trust_level: community
id: wtfbin-ivanti-endpoint-manager
namespace: wtf:bin:ivanti-endpoint-manager
name: "Ivanti Endpoint Manager"
description: "Ivanti does some weird stuff"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - windows
techniques:
  - execution
execution:
  template: "Ivanti Endpoint Manager"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/22"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/ivanti-endpoint-manager/"
---
examples:
  - description: "Execute Ivanti Endpoint Manager and observe the unusual behavior"
    command: "Ivanti Endpoint Manager"

# Ivanti Endpoint Manager

Ivanti does some weird stuff


   
The command-line arguments for the exes listed below occasionally contain fragmented, seemingly-random strings containing special unicode characters, what looks like bits of HTML or XML tags, and/or URL-enocoded strings. For example:
* LDdrives.exe -p 51205 -c -s -b5D€Cv
* LDdrives.exe -p 51205 -c -s -b8µq
* LDdrives.exe -p 51205 -c -s "-b8</timer>¶(+N& "
* LDmemory.exe -p 51207 -c -s "-b32164/><key nam=ÂgËo�"
* LDnetwork.exe -p 51214 -c -s -b10</timer>žÊ/€/�

These processes all spawn instances of Console Host (conhost.exe) with the 0x4 flag, like `C:\Windows\system32\conhost.exe 0x4`.

*Contributed by Micah Babinski (mbabinski)*
