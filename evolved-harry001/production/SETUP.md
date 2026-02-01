# harry-clawd Production Setup

**Goal:** Real production system, not just experiments.

## 🎯 Production Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRODUCTION STACK                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│  │   Codespace │───▶│   Deploy    │───▶│   Server    │    │
│  │  (Dev Env)  │    │   Pipeline  │    │  (Production│    │
│  └─────────────┘    └─────────────┘    └─────────────┘    │
│        │                                     │            │
│        ▼                                     ▼            │
│  ┌─────────────┐                      ┌─────────────┐    │
│  │   GitHub    │                      │   Monitor   │    │
│  │   Actions   │                      │   (24/7)    │    │
│  └─────────────┘                      └─────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📋 Production Components

### 1. CI/CD Pipeline
```yaml
# .github/workflows/production.yml
name: Production Deploy
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 9 * * *'  # Daily 9AM

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'
      - name: Install Dependencies
        run: npm ci
      - name: Run Tests
        run: npm test
      - name: Deploy to Server
        run: |
          # Deploy to production server
          ssh user@server "cd /opt/harry-clawd && git pull && npm ci && pm2 restart all"
```

### 2. Server Setup (Production)
```bash
# On production server (Ubuntu/Debian)
# 1. Install Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. Install PM2 (process manager)
sudo npm install -g pm2

# 3. Create directory
sudo mkdir -p /opt/harry-clawd
sudo chown $USER /opt/harry-clawd

# 4. Setup Nginx (reverse proxy)
sudo apt install nginx
sudo systemctl enable nginx

# 5. SSL with Let's Encrypt
sudo certbot --nginx -d harry-clawd.example.com
```

### 3. Monitoring (24/7)
```bash
# PM2 Dashboard
pm2 install pm2-logrotate
pm2 install pm2-server-monit
pm2 install pm2-http

# Uptime monitoring
pm2 start uptime-monitor.js
```

### 4. Backup Strategy
```bash
# Daily backup cron
0 2 * * * tar -czf /backup/harry-clawd-$(date +\%Y\%m\%d).tar.gz /opt/harry-clawd

# Weekly to cloud
0 3 * * 0 rclone sync /backup/ gdrive:harry-clawd-backup
```

## 🔧 harry-clawd Repo Structure (Production)

```
harry-clawd/
├── src/
│   ├── index.js           # Main entry
│   ├── services/          # Business logic
│   ├── utils/             # Helpers
│   └── config/            # Environment
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/
│   ├── deploy.sh          # Deploy script
│   ├── backup.sh          # Backup script
│   └── monitor.sh         # Health check
├── .env.example           # Environment template
├── Dockerfile             # Container
├── docker-compose.yml     # Local dev
├── ecosystem.config.js    # PM2 config
└── README.md
```

## 🚀 Quick Deploy Commands

```bash
# From codespace
cd /workspaces/harry-clawd

# Build
npm run build

# Test
npm test

# Deploy
npm run deploy

# Or manual
git push origin main
# GitHub Actions auto-deploys
```

## 📊 Production Checklist

- [ ] Server provisioned (VPS/Cloud)
- [ ] Domain configured (DNS A record)
- [ ] SSL certificate (Let's Encrypt)
- [ ] PM2 process manager setup
- [ ] Nginx reverse proxy
- [ ] Firewall configured (ufw)
- [ ] SSH keys setup
- [ ] GitHub Actions secrets configured
- [ ] Monitoring (Uptime Robot/Pingdom)
- [ ] Backups (daily + offsite)
- [ ] Logs (centralized)
- [ ] Alerts (error notifications)

## 🎯 First Production Deploy

**Step 1: Create new codespace**
```bash
gh codespace create --repo Harry-00101/harry-clawd
```

**Step 2: Setup production branch**
```bash
git checkout -b production
git push -u origin production
```

**Step 3: Provision server**
- Rent VPS (DigitalOcean/AWS/DO/Hetzner)
- Run setup script

**Step 4: Configure GitHub Actions**
- Add secrets (SSH key, server IP, etc.)

**Step 5: First deploy**
```bash
git checkout production
# Make changes
git add .
git commit -m "Production setup"
git push
```

**Step 6: Verify**
- Check https://harry-clawd.example.com
- Check server logs
- Check monitoring

## 💰 Cost Estimate

| Item | Monthly Cost |
|------|--------------|
| VPS (2GB RAM, 1 CPU) | $5-10 |
| Domain | $1-2 |
| SSL | Free (Let's Encrypt) |
| Monitoring | Free (Uptime Robot) |
| **Total** | **$6-12/month** |

## 🛠️ Tools Required

- [ ] VPS Provider (DigitalOcean, Hetzner, Linode)
- [ ] Domain registrar (Namecheap, Cloudflare)
- [ ] GitHub account
- [ ] PM2 (process manager)
- [ ] Nginx (web server)
- [ ] Let's Encrypt (SSL)

---

**Goal: harry-clawd running 24/7 in production! 🚀**
