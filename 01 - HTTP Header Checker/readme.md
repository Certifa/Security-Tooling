# HTTP Security Header Scanner

A lightweight command-line tool for auditing HTTP security headers on one or multiple targets. Quickly identify missing or misconfigured headers that could expose a web application to common attacks.

## Checks

The tool checks for the following security headers:

| Header                      | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| `Content-Security-Policy`   | Mitigates XSS and data injection attacks |
| `Strict-Transport-Security` | Enforces HTTPS connections               |
| `X-Frame-Options`           | Prevents clickjacking                    |
| `X-Content-Type-Options`    | Stops MIME-type sniffing                 |
| `Permissions-Policy`        | Controls browser feature access          |
| `Referrer-Policy`           | Limits referrer information leakage      |

## Installation

```bash
git clone https://github.com/youruser/http-header-scanner
cd http-header-scanner
pip install requests
```

## Usage

**Scan a single URL:**
```bash
python scanner.py -u https://example.com
```

**Scan multiple URLs from a file:**
```bash
python scanner.py -f urls.txt
```

**Save output to a file:**
```bash
python scanner.py -u https://example.com -o results.txt
python scanner.py -f urls.txt -o results.txt
```

### Arguments

| Flag             | Description                                       |
| ---------------- | ------------------------------------------------- |
| `-u`, `--url`    | Single target URL                                 |
| `-f`, `--file`   | Path to a `.txt` file containing one URL per line |
| `-o`, `--output` | Save results to a file (appends)                  |

## Example Output

```
===============
https://example.com
===============
Status code  200

Content-Security-Policy MISSING
Strict-Transport-Security max-age=31536000; includeSubDomains
X-Frame-Options DENY
X-Content-Type-Options nosniff
Permissions-Policy MISSING
Referrer-Policy no-referrer
```
