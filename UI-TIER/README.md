# UI-TIER: AI Employee Web Dashboard

A beautiful, modern web-based UI for your AI Employee that can be deployed on Vercel.

## 🎯 Features

- **Real-time Dashboard**: View email processing stats, tasks, and system status
- **Email Management**: Track and manage emails from Gmail
- **Task Tracking**: Monitor auto-generated tasks from emails
- **Activity Feed**: Live activity log of all AI Employee actions
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Theme**: Beautiful gradient dark mode UI

## 🚀 Quick Start

### Option 1: Local Development

1. **Install Node.js dependencies**:
```bash
cd UI-TIER
npm install
```

2. **Start the Backend Server** (optional, for real data):
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run backend server
python backend_server.py
```

3. **Start the Frontend**:
```bash
npm run dev
```

4. **Open in browser**: http://localhost:3000

### Option 2: Deploy to Vercel

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Deploy**:
```bash
vercel --prod
```

3. **Follow the prompts** to complete deployment

## 📁 Project Structure

```
UI-TIER/
├── app/
│   ├── api/              # API routes
│   │   ├── stats/        # Statistics endpoint
│   │   ├── emails/       # Emails endpoint
│   │   ├── tasks/        # Tasks endpoint
│   │   └── activity/     # Activity feed endpoint
│   ├── globals.css       # Global styles
│   ├── layout.tsx        # Root layout
│   └── page.tsx          # Main page
├── components/
│   ├── Dashboard.tsx     # Dashboard component
│   ├── EmailList.tsx     # Email list component
│   ├── TaskList.tsx      # Task list component
│   └── ActivityFeed.tsx  # Activity feed component
├── public/               # Static assets
├── backend_server.py     # Python backend server
├── package.json          # Node.js dependencies
├── tsconfig.json         # TypeScript config
├── tailwind.config.js    # Tailwind CSS config
└── vercel.json           # Vercel deployment config
```

## 🔧 Configuration

### Connect to Your Existing AI Employee

The UI is designed to work with your existing Bronze and Platinum tier code:

- **Bronze Vault**: `../bronze/bronze_vault`
- **Platinum Vault**: `../PLATINUM-TIER/platinum_vault`

The backend server (`backend_server.py`) reads data from these vaults and serves it to the UI.

### Environment Variables

For Vercel deployment, you may need to set these environment variables:

```
NODE_VERSION=18
NEXT_PUBLIC_API_URL=your-backend-url
```

## 🎨 UI Components

### Dashboard
- Overview statistics (Inbox, Needs Action, Pending, Done)
- Processing statistics
- Quick action buttons
- System status indicators

### Emails
- List of all processed emails
- Status indicators (unread, processing, completed)
- Email processing settings

### Tasks
- Task management with priority levels
- Filter by status (all, pending, in_progress, completed)
- Task details and actions

### Activity
- Real-time activity feed
- Activity analytics
- Color-coded activity types

## 🔄 How It Works

1. **Frontend (Next.js)**: React-based UI that runs on Vercel
2. **Backend (Flask)**: Python server that connects to your AI Employee code
3. **Data Flow**: 
   - AI Employee processes emails → Creates .md files in vault
   - Backend reads vault folders → Serves data via API
   - Frontend calls APIs → Displays data in beautiful UI

## 📝 Important Notes

- **Your existing console code remains unchanged** - this is a separate UI layer
- The UI reads from the same vault folders your console app uses
- You can run both console and UI versions simultaneously
- All data is stored in your existing vault structure

## 🐛 Troubleshooting

### Backend not connecting?
- Make sure Flask is installed: `pip install flask flask-cors`
- Check vault paths in `backend_server.py`
- Run backend with: `python backend_server.py`

### UI not showing data?
- Ensure backend server is running on port 5001
- Check browser console for errors
- Verify vault folders exist and contain .md files

### Deployment issues?
- Run `vercel --prod` from the UI-TIER folder
- Check vercel.json configuration
- Ensure all dependencies are in package.json

## 🎯 Next Steps

1. **Customize**: Modify colors, layouts, and features in the components
2. **Deploy**: Push to Vercel for production hosting
3. **Integrate**: Connect to your actual Gmail and Claude APIs
4. **Enhance**: Add more features like notifications, settings, etc.

## 📄 License

Part of your Hackathon 0 project - All rights reserved.

---

**Made with ❤️ for your AI Employee**
