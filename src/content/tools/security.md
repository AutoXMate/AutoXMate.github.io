---
trust_level: community
id: macos-credential-access-security
namespace: macos:credentialaccess:security
name: security
description: Interact with Keychain, macOS's built-in password manager.
author: Pratik Jeware (@Pratik-987), Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - credential.dump
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - credential-access
  - defense-evasion
execution:
  template: "security"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Dump credentials, keys, certificates, and other sensitive information from Keychain: This command will dump keychain passwords from login.keychain"
    command: "sudo security dump-keychain -d login.keychain"
  - description: "Retrieve Chrome's \"Chrome Safe Storage\" password manager secret: This command will retrieve the Chrome Safe Storage password manager secret from the keychain."
    command: "security find-generic-password -w -s \"Chrome Safe Storage\""
  - description: "Add an arbitrary trusted certificate to aid a MITM attack: This command will add a certificate to the keychain."
    command: "security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain bad_cert.crt"
install:
  - method: custom
    commands:
      - "/usr/bin/security"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_creds_from_keychain.yml"
    description: "Sigma: Credentials from Password Stores - Keychain"
  - type: elastic
    url: "https://github.com/elastic/detection-rules/blob/main/rules/macos/credential_access_credentials_keychains.toml"
    description: "Elastic: Access to Keychain Credentials Directories"
  - type: elastic
    url: "https://github.com/elastic/detection-rules/blob/main/rules/macos/credential_access_dumping_keychain_security.toml"
    description: "Elastic: Credential Access Dumping Keychain Security"
  - type: elastic
    url: "https://github.com/elastic/detection-rules/blob/main/rules/macos/credential_access_keychain_pwd_retrieval_security_cmd.toml"
    description: "Elastic: Keychain Password Retrieval via Command Line"
  - type: other
    url: "https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/keychain_dumped"
    description: "Jamf Protect: Detect Keychain dumping using security"
references:
  - label: "Using the OS X Keychain to store and retrieve passwords"
    url: "https://www.netmeister.org/blog/keychain-passwords.html"
  - label: "SS64 security man page"
    url: "https://ss64.com/osx/security.html"
---

security is a command-line utility included in macOS that allows users to interact with the Keychain app. Keychains allow users to manager passwords and credentials for many services and features, including Wi-Fi and website passwords, secure notes, certificates, and Kerberos.