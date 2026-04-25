# Security Tooling

A collection of custom-built security tools developed from scratch in Python. Each tool targets a specific phase of penetration testing or security assessment — from reconnaissance and analysis to exploitation and post-exploitation.

Built as part of a structured learning path to develop hands-on scripting ability for offensive security work. Every tool is written without AI code generation.

## Tools

| # | Tool | Phase | Status |
|---|------|-------|--------|
| 01 | [HTTP Header checker](https://github.com/Certifa/Security-Tooling/tree/main/01%20-%20HTTP%20Header%20Checker) | Recon | ✅ |
| 02 | [Subdomain Enumerator](#02---subdomain-enumerator) | Recon | 🔲 |
| 03 | [Log Analyzer](#03---log-analyzer) | Forensics | 🔲 |
| 04 | [Port Scanner](#04---port-scanner) | Recon | 🔲 |
| 05 | [OSINT Scraper](#05---osint-scraper) | Recon | 🔲 |
| 06 | [Hash Cracker](#06---hash-cracker) | Exploitation | 🔲 |
| 07 | [Vulnerability Scanner](#07---vulnerability-scanner) | Assessment | 🔲 |
| 08 | [Packet Analyzer](#08---packet-analyzer) | Network | 🔲 |
| 09 | [Exploit Framework](#09---exploit-framework) | Exploitation | 🔲 |
| 10 | [C2-Lite](#10---c2-lite) | Post-Exploitation | 🔲 |

> Update status to ✅ when a tool is complete and pushed.

---

### 01 - HTTP Header Checker

**Directory:** `01-header-checker/`

CLI tool that audits HTTP security headers across one or multiple targets. Checks for the presence and configuration of headers like `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Permissions-Policy`, and `Referrer-Policy`. Supports single URL input and bulk scanning from file.

**Core libraries:** `requests`, `argparse`, `sys`

---

### 02 - Subdomain Enumerator

**Directory:** `02-subdomain-enum/`

Enumerates subdomains for a target domain using certificate transparency logs (crt.sh). Resolves discovered subdomains via DNS to identify live hosts. Outputs results as a formatted terminal table or JSON for pipeline integration.

**Core libraries:** `requests`, `json`, `socket`, `argparse`, `re`

---

### 03 - Log Analyzer

**Directory:** `03-log-analyzer/`

Parses Apache and Nginx access logs to identify indicators of attack. Detects brute-force attempts (repeated 401/403 from single IPs), directory traversal patterns, SQL injection signatures in request URIs, and anomalous request rates. Generates a summary report of findings with severity ratings.

**Core libraries:** `re`, `collections`, `csv`, `argparse`, `datetime`

---

### 04 - Port Scanner

**Directory:** `04-port-scanner/`

Multi-threaded TCP port scanner with banner grabbing. Supports scanning custom port ranges, top-N common ports, or specific port lists. Identifies open ports and attempts service fingerprinting through banner analysis.

**Core libraries:** `socket`, `threading`, `argparse`, `struct`

---

### 05 - OSINT Scraper

**Directory:** `05-osint-scraper/`

Automated OSINT collection tool for target domains. Scrapes and enumerates email addresses, social media links, technology stack indicators (response headers, HTML meta tags, known paths), exposed metadata, and `robots.txt` / `sitemap.xml` contents. Compiles findings into a structured recon report.

**Core libraries:** `requests`, `BeautifulSoup`, `re`, `json`, `argparse`

---

### 06 - Hash Cracker

**Directory:** `06-hash-cracker/`

Hash identification and dictionary attack tool. Detects hash type by format and length (MD5, SHA-1, SHA-256, etc.), then attempts to crack using a provided wordlist with configurable mutation rules (case toggling, digit appending, common substitutions).

**Core libraries:** `hashlib`, `argparse`, `sys`, `itertools`

---

### 07 - Vulnerability Scanner

**Directory:** `07-vuln-scanner/`

Template-based web vulnerability scanner inspired by Nuclei's architecture. Detection rules are defined as YAML template files specifying: the HTTP request to send, response matching criteria, and severity classification. Ships with templates for CORS misconfiguration, open redirect, exposed `.git` directories, directory listing, missing security headers, and default credentials on common services.

**Core libraries:** `requests`, `yaml`, `re`, `argparse`, `os`

---

### 08 - Packet Analyzer

**Directory:** `08-packet-analyzer/`

Network traffic capture and analysis tool. Sniffs packets on a specified interface and identifies security-relevant traffic: cleartext credentials, DNS queries, ARP anomalies, and unencrypted HTTP requests. Outputs a real-time summary and post-capture report.

**Core libraries:** `scapy`, `argparse`, `struct`

---

### 09 - Exploit Framework

**Directory:** `09-exploit-framework/`

Modular exploit framework where each module is a self-contained proof-of-concept for a specific CVE. The framework handles target specification, module selection, and execution. Includes PoC modules for vulnerabilities encountered during HackTheBox machines and CTF challenges.

**Core libraries:** `requests`, `socket`, `pwntools`, `argparse`, `importlib`

---

### 10 - C2-Lite

**Directory:** `10-c2-lite/`

Educational command-and-control simulation for red team learning. Implements a basic agent-handler architecture with remote command execution, file transfer (upload/download), and connection management. Built strictly for lab environments and authorized testing.

**Core libraries:** `socket`, `flask`, `subprocess`, `os`, `threading`, `base64`

> ⚠️ **Disclaimer:** This tool is built for educational purposes in authorized lab environments only. Do not deploy against systems you do not own or have explicit written permission to test.

---

## Usage

Each tool directory contains its own `README.md` with installation instructions, usage examples, and sample output. General requirements:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/security-tooling.git
cd security-tooling

# Install dependencies for a specific tool
pip install -r 01-header-checker/requirements.txt

# Run the tool
python 01-header-checker/header_check.py --help
```

## About

These tools are built as part of a structured offensive security learning path. Each project targets specific Python libraries and security concepts, progressing from basic HTTP interaction to network-level analysis and exploit development.

- **HackTheBox:** Pro Hacker
- **Bug Bounty:** Active on HackerOne and Bugcrowd
- **Focus areas:** Web application security, OSINT, forensics
