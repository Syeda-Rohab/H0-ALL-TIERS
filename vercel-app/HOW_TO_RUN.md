# ✅ How to Run Your AI Employee Dashboard

## ⚠️ IMPORTANT: Run These Steps Manually

The automated scripts aren't working reliably. Please follow these steps:

---

## 📝 Step-by-Step Instructions

### Step 1: Open PowerShell
Press `Windows + R`, type `powershell`, press Enter

### Step 2: Navigate to vercel-app folder
```powershell
cd "C:\Users\Dell\Desktop\H0 Q4\vercel-app"
```

### Step 3: Install dependencies (first time only)
```powershell
npm install
```

Wait 2-3 minutes for installation to complete.

### Step 4: Run the development server
```powershell
npm run dev
```

### Step 5: Open browser
Go to: **http://localhost:3000**

---

## 🎯 Or Use the Batch File

1. Open folder: `C:\Users\Dell\Desktop\H0 Q4\vercel-app`
2. Double-click: **`START_HERE.bat`**
3. Wait for installation
4. Browser will open automatically

---

## 🐛 If It Still Doesn't Work

### Check Node.js is installed:
```powershell
node --version
npm --version
```

If you get "command not found":
- Install Node.js from: https://nodejs.org
- Download the LTS version (Long Term Support)
- Install and restart your computer
- Try again

### Clear cache and reinstall:
```powershell
cd "C:\Users\Dell\Desktop\H0 Q4\vercel-app"
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item package-lock.json -ErrorAction SilentlyContinue
npm install
npm run dev
```

---

## ✅ What You Should See

When it's working, you'll see:

```
> ai-employee-ui@1.0.0 dev
> next dev

  ▲ Next.js 14.2.3
  - Local:        http://localhost:3000

 ✓ Ready in 1234ms
```

Then open http://localhost:3000 in your browser.

---

## 🎨 Your Dashboard

Once running, you'll see:
- 📊 Overview tab with stats
- 🥉 Bronze Tier information
- 💎 Platinum Tier information
- 📁 Files browser
- 🚀 Deploy instructions

---

**Please try the manual steps above!** 🙏
