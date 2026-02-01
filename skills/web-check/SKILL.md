# Web-Check Integration

All-in-one OSINT tool for analyzing any website.

## What it Does

🕵️‍♂️ Website analysis including:
- **IP Info** - Server IP, location, hosting
- **SSL Chain** - Certificate details, validity
- **DNS Records** - A, MX, NS, TXT records
- **Headers** - Server tech, security headers
- **Open Ports** - Running services
- **Traceroute** - Network path
- **Trackers** - Analytics, advertising
- **Performance** - Load times, carbon footprint

## Installation

```bash
# Via Docker
docker run -p 3000:3000 lissy93/web-check

# Or via NPM
git clone https://github.com/Lissy93/web-check.git
cd web-check
npm install && npm start
```

## For Harry-001

Web-Check可以:
1. **Analyze stock websites** - Check SEC filings, Yahoo Finance
2. **Verify news sources** - Check site authenticity
3. **Security analysis** - Find vulnerabilities
4. **Competitor research** - Tech stack analysis

## Usage

```bash
# Check a website
curl -s https://api.web-check.xyz/api/<check>?url=<target>

# Checks available:
# ip, ssl, dns, cookies, headers, domain, 
# tech, page-speed, carbon, trace, ports
```

## Example: Check Yahoo Finance

```bash
curl -s https://api.web-check.xyz/api/ip?url=finance.yahoo.com
curl -s https://api.web-check.xyz/api/ssl?url=finance.yahoo.com
curl -s https://api.web-check.xyz/api/dns?url=finance.yahoo.com
```

## References

- https://github.com/Lissy93/web-check
- https://web-check.xyz (demo)
- https://api.web-check.xyz (free API)
