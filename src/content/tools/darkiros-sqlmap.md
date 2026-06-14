---
trust_level: community
id: darkiros-sqlmap
namespace: darkiros:tool:sqlmap
name: sqlmap
description: SQLMap - classic with tamper
version: 1.0.0
capabilities:
- security.execution.injection
platforms:
- cross-platform
techniques:
- execution
execution:
  template: sqlmap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: SQLMap - classic with tamper
  command: sqlmap -u '[url]' tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
- description: SQLMap - mysql tamper list
  command: sqlmap -u '[url]' --dbms=MYSQL tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
- description: SQLMap - mssql tamper list
  command: sqlmap -u '[url]' --dbms=MSSQL tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
items:
- Hash
- Password
services:
- HTTP
- HTTPS
- MSSQL
- MySQL
- PostgreSQL
features:
- pipes-stdin
- stealth
mitre_ids:
- T1190
---

# sqlmap

Darkiros cheat sheet commands:

**SQLMap - classic with tamper**
```
sqlmap -u '[url]' tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

**SQLMap - mysql tamper list**
```
sqlmap -u '[url]' --dbms=MYSQL tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

**SQLMap - mssql tamper list**
```
sqlmap -u '[url]' --dbms=MSSQL tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```
