# 📚 AI Employee Pro - Documentation

## 🎯 Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [API Reference](#api-reference)
- [Troubleshooting](#troubleshooting)

---

## Introduction

AI Employee Pro is a complete autonomous AI employee management system with 4 tiers.

### Tiers Overview

| Tier | Purpose | Features |
|------|---------|----------|
| 🥉 Bronze | Email Processing | Gmail integration, Action plans |
| 🥈 Silver | Automation | Calendar, Reminders, Auto-reply |
| 🥇 Gold | Content | AI Content, Social Media |
| 💎 Platinum | Multi-Agent | 7 Agents, Analytics |

---

## Installation

### Prerequisites

- Python 3.9+ (for console tiers)
- Node.js 18+ (for dashboard)
- Gmail API credentials (optional)

### Setup

```bash
# Clone repository
git clone https://github.com/Syeda-Rohab/H0-ALL-TIERS.git
cd H0-ALL-TIERS

# Install dashboard dependencies
cd ai-employee-pro
npm install
```

---

## Usage

### Run Dashboard

```bash
cd ai-employee-pro
npm run dev
```

**Open:** http://localhost:3000

### Run Console Tiers

```bash
# Bronze Tier
cd bronze
python ai_employee_simple.py

# Platinum Tier
cd PLATINUM-TIER
python platinum_tier_console_simple.py
```

---

## Deployment

### Vercel (Recommended)

```bash
cd ai-employee-pro
vercel --prod
```

### Manual Deploy

1. Go to [vercel.com](https://vercel.com)
2. Import repository
3. Root: `./ai-employee-pro`
4. Deploy

---

## API Reference

### Dashboard Endpoints

The dashboard is static and doesn't require a backend. All data is simulated.

### Console Tier APIs

**Bronze Tier:**
- `gmail_auth.py` - Gmail authentication
- `ai_employee.py` - Main processing logic

**Platinum Tier:**
- `platinum_tier_console.py` - Multi-agent system

---

## Troubleshooting

### Dashboard not loading?

```bash
# Clear cache
rm -rf .next
npm run build
npm run dev
```

### Console tier errors?

```bash
# Install dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.9+
```

### Vercel deployment fails?

1. Check `vercel.json` configuration
2. Verify Root Directory: `./ai-employee-pro`
3. Check build logs in Vercel dashboard

---

## FAQ

**Q: Do I need Gmail API credentials?**  
A: Only for real email processing. Dashboard works without them.

**Q: Can I customize the UI?**  
A: Yes! Edit `ai-employee-pro/index.html`

**Q: Is it mobile responsive?**  
A: Yes! Works perfectly on all devices.

---

## Support

- **Issues:** [GitHub Issues](https://github.com/Syeda-Rohab/H0-ALL-TIERS/issues)
- **Demo:** [Live Dashboard](https://h0-all-tiers.vercel.app)

---

<div align="center">

**Made with ❤️ for Hackathon 0**

</div>
