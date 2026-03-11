# 🚀 AI Employee UI - Quick Start Guide

## Option 1: Automatic Setup (Recommended for Windows)

1. **Double-click** `setup-and-run.bat` in the `UI-TIER` folder
2. Wait for installation to complete
3. Browser will automatically open to http://localhost:3000

## Option 2: Manual Setup

### Step 1: Install Node.js Dependencies

Open Command Prompt or PowerShell in the `UI-TIER` folder and run:

```bash
npm install
```

### Step 2: Install Python Dependencies (Optional - for backend)

```bash
pip install -r requirements.txt
```

### Step 3: Start the Development Server

```bash
npm run dev
```

### Step 4: Open in Browser

Navigate to: **http://localhost:3000**

## Option 3: Deploy to Vercel

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Deploy

```bash
vercel --prod
```

### Step 3: Get Your Live URL

Vercel will provide a URL like: `https://your-project.vercel.app`

## 📋 Prerequisites

- **Node.js 18+**: [Download here](https://nodejs.org/)
- **npm**: Comes with Node.js
- **Python 3.9+** (optional, for backend): [Download here](https://python.org)

## 🎯 What You Get

✅ Beautiful dark-themed dashboard UI
✅ Real-time statistics from your AI Employee
✅ Email management interface
✅ Task tracking with priorities
✅ Activity feed with live updates
✅ Ready for Vercel deployment
✅ **Your existing console code remains untouched!**

## 🔧 Troubleshooting

### npm install fails
- Make sure you have Node.js installed
- Try deleting `node_modules` folder and running `npm install` again

### Port 3000 already in use
- Run `npm run dev -- -p 3001` for a different port

### Backend not connecting
- Run `python backend_server.py` in a separate terminal
- Make sure Flask is installed: `pip install flask flask-cors`

## 📞 Need Help?

Check the full README.md for detailed documentation.

---

**Happy Coding! 🎉**
