---
id: windows-kernel-procexp
namespace: windows:kernel:procexp
name: procexp.Sys
description: Elevate privileges
author: Nasreddine Bencherchali
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create procexp.sys binPath=C:\windows\temp\procexp.Sys type=kernel
    && sc.exe start procexp.Sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load procexp.Sys kernel driver
  commands:
  - sc.exe create procexp.sys binPath=C:\windows\temp\procexp.Sys type=kernel && sc.exe
    start procexp.Sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/075de997497262a9d105afeadaaefc6348b25ce0e0126505c24aa9396c251e85.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/16a2e578bc8683f17a175480fea4f53c838cfae965f1d4caa47eaf9e0b3415c1.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/1b00d6e5d40b1b84ca63da0e99246574cdd2a533122bc83746f06c0d66e63a6e.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/30abc0cc700fdebc74e62d574addc08f6227f9c7177d9eaa8cbc37d5c017c9bb.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3503ea284b6819f9cb43b3e94c0bb1bf5945ccb37be6a898387e215197a4792a.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3c7e5b25a33a7805c999d318a9523fcae46695a89f55bbdb8bb9087360323dfc.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3ff39728f1c11d1108f65ec5eb3d722fd1a1279c530d79712e0d32b34880baaa.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/46621554728bc55438c7c241137af401250f062edef6e7efecf1a6f0f6d0c1f7.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/51e91dd108d974ae809e5fc23f6fbd16e13f672f86aa594dae4a5c4bc629b0b5.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/59b09bd69923c0b3de3239e73205b1846a5f69043546d471b259887bb141d879.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6bfc0f425de9f4e7480aa2d1f2e08892d0553ed0df1c31e9bf3d8d702f38fa2e.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6e944ae1bfe43a8a7cd2ea65e518a30172ce8f31223bdfd39701b2cb41d8a9e7.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/77950e2a40ac0447ae7ee1ee3ef1242ce22796a157074e6f04e345b1956e143c.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/7a48f92a9c2d95a72e18055cac28c1e7e6cad5f47aa735cbea5c3b82813ccfaf.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/86721ee8161096348ed3dbe1ccbf933ae004c315b1691745a8af4a0df9fed675.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/88e2e6a705d3fb71b966d9fb46dc5a4b015548daf585fb54dfcd81dc0bd3ebdc.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/89b9823ed974a5b71de8468324d45b7e9d6dc914f93615ba86c6209b25b3cbf7.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/98a123b314cba2de65f899cdbfa386532f178333389e0f0fbd544aff85be02eb.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/9d5ebd0f4585ec20a5fe3c5276df13ece5a2645d3d6f70cedcda979bd1248fc2.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/bced04bdefad6a08c763265d6993f07aa2feb57d33ed057f162a947cf0e6668f.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/bdbceca41e576841cad2f2b38ee6dbf92fd77fbbfdfe6ecf99f0623d44ef182c.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c089a31ac95d41ed02d1e4574962f53376b36a9e60ff87769d221dc7d1a3ecfa.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/cdfbe62ef515546f1728189260d0bdf77167063b6dbb77f1db6ed8b61145a2bc.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/d6827cd3a8f273a66ecc33bb915df6c7dea5cc1b8134b0c348303ef50db33476.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/e07211224b02aaf68a5e4b73fc1049376623793509d9581cdaee9e601020af06.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/e3f2ee22dec15061919583e4beb8abb3b29b283e2bcb46badf2bfde65f5ea8dd.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/f29073dc99cb52fa890aae80037b48a172138f112474a1aecddae21179c93478.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/59b09bd69923c0b3de3239e73205b1846a5f69043546d471b259887bb141d879.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/440883cd9d6a76db5e53517d0ec7fe13d5a50d2f6a7f91ecfc863bc3490e4f5c.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/cdfbe62ef515546f1728189260d0bdf77167063b6dbb77f1db6ed8b61145a2bc.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/9b6a84f7c40ea51c38cc4d2e93efb3375e9d98d4894a85941190d94fbe73a4e4.yara
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
references:
- label: Reference
  url: https://malware.news/t/lazarus-group-attack-case-using-vulnerability-of-certificate-software-commonly-used-by-public-institutions-and-universities/67715
- label: Reference
  url: https://waawaa.github.io/en/Bypass-PPL-Using-Process-Explorer/
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/57
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
- label: Reference
  url: https://github.com/Yaxser/Backstab/blob/master/resources/PROCEXP.sys
- label: Reference
  url: https://news.sophos.com/en-us/2023/04/19/aukill-edr-killer-malware-abuses-process-explorer-driver/
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/55#issuecomment-1537161951
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create procexp.sys binPath=C:\\\\windows\\\\temp\\\\procexp.Sys type=kernel && sc.exe start procexp.Sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver procexp.Sys"

# procexp.Sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
