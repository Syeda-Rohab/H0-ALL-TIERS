'use client'

import { useState, useEffect } from 'react'

// Sample data (in production, this would come from API or be embedded at build time)
const INITIAL_STATS = {
  bronzeEmails: 68,
  bronzePlans: 68,
  bronzeDone: 68,
  platinumTasks: 0,
  totalEmails: 68,
  totalDone: 68,
  activeTasks: 0,
}

export default function Home() {
  const [activeTab, setActiveTab] = useState('overview')
  const [stats, setStats] = useState(INITIAL_STATS)
  const [isClient, setIsClient] = useState(false)

  useEffect(() => {
    setIsClient(true)
  }, [])

  if (!isClient) {
    return (
      <div className="min-h-screen gradient-bg flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-400">Loading Dashboard...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen gradient-bg">
      {/* Header */}
      <header className="glass border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-3">
              <div className="w-12 h-12 gradient-card rounded-xl flex items-center justify-center border border-primary/30">
                <span className="text-2xl">🤖</span>
              </div>
              <div>
                <h1 className="text-2xl font-bold gradient-text">AI Employee</h1>
                <p className="text-sm text-gray-400">Hackathon 0 - Unified Dashboard</p>
              </div>
            </div>
            <div className="flex items-center space-x-2 px-4 py-2 glass rounded-full">
              <div className="w-2 h-2 bg-secondary rounded-full animate-pulse"></div>
              <span className="text-sm text-secondary">System Active</span>
            </div>
          </div>
        </div>
      </header>

      {/* Navigation */}
      <nav className="glass border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-2 overflow-x-auto">
            {[
              { id: 'overview', label: '📊 Overview', icon: '📊' },
              { id: 'bronze', label: '🥉 Bronze', icon: '🥉' },
              { id: 'platinum', label: '💎 Platinum', icon: '💎' },
              { id: 'files', label: '📁 Files', icon: '📁' },
              { id: 'deploy', label: '🚀 Deploy', icon: '🚀' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-4 py-3 rounded-lg font-medium transition-all whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'gradient-card text-white border border-primary/50'
                    : 'text-gray-400 hover:text-white hover:bg-white/5'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'overview' && <OverviewTab stats={stats} />}
        {activeTab === 'bronze' && <BronzeTab stats={stats} />}
        {activeTab === 'platinum' && <PlatinumTab stats={stats} />}
        {activeTab === 'files' && <FilesTab />}
        {activeTab === 'deploy' && <DeployTab />}
      </main>

      {/* Footer */}
      <footer className="glass border-t border-white/10 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <p className="text-center text-sm text-gray-400">
            AI Employee Dashboard © 2026 | Hackathon 0 | Built with Next.js & Tailwind CSS
          </p>
        </div>
      </footer>
    </div>
  )
}

// Overview Tab Component
function OverviewTab({ stats }: { stats: typeof INITIAL_STATS }) {
  const statCards = [
    { title: 'Emails Processed', value: stats.totalEmails, icon: '📧', color: 'from-blue-500 to-cyan-500' },
    { title: 'Tasks Completed', value: stats.totalDone, icon: '✅', color: 'from-green-500 to-emerald-500' },
    { title: 'Active Tasks', value: stats.activeTasks, icon: '⚡', color: 'from-orange-500 to-red-500' },
    { title: 'Efficiency', value: '98.5%', icon: '🎯', color: 'from-purple-500 to-pink-500' },
  ]

  return (
    <div className="space-y-6">
      <div className="gradient-card rounded-2xl p-6 border border-primary/30">
        <h2 className="text-2xl font-bold mb-2 gradient-text">Welcome to AI Employee Dashboard</h2>
        <p className="text-gray-400">
          Your unified AI employee management system. Monitor all tiers, track progress, and deploy to Vercel.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {statCards.map((card) => (
          <div
            key={card.title}
            className="glass rounded-2xl p-6 glass-hover transition-all hover:scale-105"
          >
            <div className="flex items-center justify-between mb-4">
              <span className="text-4xl">{card.icon}</span>
              <div className={`w-16 h-16 bg-gradient-to-br ${card.color} rounded-xl flex items-center justify-center shadow-lg`}>
                <span className="text-2xl font-bold">{card.value}</span>
              </div>
            </div>
            <h3 className="text-lg font-semibold mb-1">{card.title}</h3>
            <p className="text-sm text-gray-400">Real-time statistics</p>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="glass rounded-2xl p-6">
          <h3 className="text-xl font-semibold mb-4">🚀 Quick Actions</h3>
          <div className="space-y-3">
            <a
              href="#bronze"
              onClick={(e) => { e.preventDefault(); document.querySelector('button[onclick*="bronze"]')?.click() }}
              className="block w-full p-4 gradient-card rounded-xl border border-primary/30 hover:border-primary/50 transition-all"
            >
              <div className="flex items-center space-x-3">
                <span className="text-2xl">🥉</span>
                <div>
                  <h4 className="font-semibold">Run Bronze Tier</h4>
                  <p className="text-sm text-gray-400">Process emails and create action plans</p>
                </div>
              </div>
            </a>
            <a
              href="#platinum"
              onClick={(e) => { e.preventDefault(); document.querySelector('button[onclick*="platinum"]')?.click() }}
              className="block w-full p-4 gradient-card rounded-xl border border-accent/30 hover:border-accent/50 transition-all"
            >
              <div className="flex items-center space-x-3">
                <span className="text-2xl">💎</span>
                <div>
                  <h4 className="font-semibold">Run Platinum Tier</h4>
                  <p className="text-sm text-gray-400">Advanced autonomous FTE with multi-agents</p>
                </div>
              </div>
            </a>
          </div>
        </div>

        <div className="glass rounded-2xl p-6">
          <h3 className="text-xl font-semibold mb-4">📈 System Status</h3>
          <div className="space-y-3">
            {[
              { name: 'Bronze Tier', status: 'Active', color: 'bg-secondary' },
              { name: 'Platinum Tier', status: 'Active', color: 'bg-secondary' },
              { name: 'Dashboard', status: 'Online', color: 'bg-primary' },
              { name: 'Vercel Ready', status: 'Yes', color: 'bg-accent' },
            ].map((item) => (
              <div key={item.name} className="flex items-center justify-between">
                <span className="text-gray-300">{item.name}</span>
                <div className="flex items-center space-x-2">
                  <div className={`w-2 h-2 ${item.color} rounded-full animate-pulse`}></div>
                  <span className="text-sm text-gray-400">{item.status}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

// Bronze Tier Tab Component
function BronzeTab({ stats }: { stats: typeof INITIAL_STATS }) {
  return (
    <div className="space-y-6">
      <div className="gradient-card rounded-2xl p-6 border border-orange-500/30">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold mb-2">🥉 Bronze Tier</h2>
            <p className="text-gray-400">Email processing, task creation, and basic automation</p>
          </div>
          <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full text-sm font-medium border border-orange-500/30">
            BRONZE
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">📧</div>
          <div className="text-3xl font-bold gradient-text">{stats.bronzeEmails}</div>
          <div className="text-sm text-gray-400 mt-1">Emails Processed</div>
        </div>
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">📋</div>
          <div className="text-3xl font-bold gradient-text">{stats.bronzePlans}</div>
          <div className="text-sm text-gray-400 mt-1">Plans Created</div>
        </div>
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">✅</div>
          <div className="text-3xl font-bold gradient-text">{stats.bronzeDone}</div>
          <div className="text-sm text-gray-400 mt-1">Completed Tasks</div>
        </div>
      </div>

      <div className="glass rounded-2xl p-6">
        <h3 className="text-xl font-semibold mb-4">How to Run Bronze Tier</h3>
        <div className="space-y-3 text-gray-300">
          <p>1. Navigate to the <code className="px-2 py-1 bg-white/10 rounded">bronze</code> folder</p>
          <p>2. Run: <code className="px-2 py-1 bg-white/10 rounded">python ai_employee_simple.py</code></p>
          <p>3. Check results in <code className="px-2 py-1 bg-white/10 rounded">bronze_vault/Done</code></p>
        </div>
      </div>
    </div>
  )
}

// Platinum Tier Tab Component
function PlatinumTab({ stats }: { stats: typeof INITIAL_STATS }) {
  return (
    <div className="space-y-6">
      <div className="gradient-card rounded-2xl p-6 border border-cyan-500/30">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold mb-2">💎 Platinum Tier</h2>
            <p className="text-gray-400">Advanced autonomous FTE with multi-agent system</p>
          </div>
          <span className="px-4 py-2 bg-cyan-500/20 text-cyan-400 rounded-full text-sm font-medium border border-cyan-500/30">
            PLATINUM
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">🤖</div>
          <div className="text-3xl font-bold gradient-text">7</div>
          <div className="text-sm text-gray-400 mt-1">Active Agents</div>
        </div>
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">📊</div>
          <div className="text-3xl font-bold gradient-text">{stats.platinumTasks}</div>
          <div className="text-sm text-gray-400 mt-1">Tasks Processed</div>
        </div>
        <div className="glass rounded-2xl p-6">
          <div className="text-4xl mb-2">📈</div>
          <div className="text-3xl font-bold gradient-text">Active</div>
          <div className="text-sm text-gray-400 mt-1">Analytics Engine</div>
        </div>
      </div>

      <div className="glass rounded-2xl p-6">
        <h3 className="text-xl font-semibold mb-4">Platinum Tier Agents</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {['Watcher', 'Processor', 'Poster', 'Analyst', 'Coordinator', 'Business', 'Self-Improvement'].map((agent) => (
            <div key={agent} className="p-3 bg-white/5 rounded-lg border border-white/10 text-center">
              <div className="text-sm font-medium">{agent}</div>
              <div className="text-xs text-secondary mt-1">Active</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

// Files Tab Component
function FilesTab() {
  const sampleFiles = [
    { name: 'EMAIL_20260311_093015.md', type: 'Email', date: '2026-03-11 09:30' },
    { name: 'PLAN_20260311_093016.md', type: 'Plan', date: '2026-03-11 09:30' },
    { name: 'EMAIL_20260311_084522.md', type: 'Email', date: '2026-03-11 08:45' },
    { name: 'PLAN_20260311_084523.md', type: 'Plan', date: '2026-03-11 08:45' },
    { name: 'EMAIL_20260310_162015.md', type: 'Email', date: '2026-03-10 16:20' },
    { name: 'PLAN_20260310_162016.md', type: 'Plan', date: '2026-03-10 16:20' },
  ]

  return (
    <div className="space-y-6">
      <div className="glass rounded-2xl p-6">
        <h2 className="text-2xl font-bold mb-4">📁 Processed Files</h2>
        <p className="text-gray-400 mb-6">Files generated by your AI Employee (stored locally in vault folders)</p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {sampleFiles.map((file) => (
            <div key={file.name} className="glass p-4 rounded-xl glass-hover cursor-pointer transition-all">
              <div className="flex items-start justify-between mb-2">
                <div className="font-mono text-sm text-primary truncate flex-1">{file.name}</div>
                <span className={`px-2 py-1 rounded text-xs ${
                  file.type === 'Email' ? 'bg-blue-500/20 text-blue-400' : 'bg-purple-500/20 text-purple-400'
                }`}>
                  {file.type}
                </span>
              </div>
              <div className="text-xs text-gray-500">{file.date}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="glass rounded-2xl p-6">
        <h3 className="text-xl font-semibold mb-4">Vault Locations</h3>
        <div className="space-y-3">
          <div className="p-4 bg-white/5 rounded-lg">
            <div className="font-medium mb-1">🥉 Bronze Vault</div>
            <code className="text-sm text-gray-400">bronze/bronze_vault/Done/</code>
          </div>
          <div className="p-4 bg-white/5 rounded-lg">
            <div className="font-medium mb-1">💎 Platinum Vault</div>
            <code className="text-sm text-gray-400">PLATINUM-TIER/platinum_vault/Done/</code>
          </div>
        </div>
      </div>
    </div>
  )
}

// Deploy Tab Component
function DeployTab() {
  return (
    <div className="space-y-6">
      <div className="gradient-card rounded-2xl p-6 border border-vercel/30" style={{ borderColor: '#0070f333' }}>
        <h2 className="text-2xl font-bold mb-2">🚀 Deploy to Vercel</h2>
        <p className="text-gray-400">Deploy this dashboard to Vercel in seconds - completely free!</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="glass rounded-2xl p-6">
          <h3 className="text-xl font-semibold mb-4">Quick Deploy Steps</h3>
          <div className="space-y-4">
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-primary/20 rounded-full flex items-center justify-center flex-shrink-0">
                <span className="text-primary font-bold">1</span>
              </div>
              <div>
                <h4 className="font-medium mb-1">Install Vercel CLI</h4>
                <code className="text-sm text-gray-400 bg-white/5 px-2 py-1 rounded">npm install -g vercel</code>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-primary/20 rounded-full flex items-center justify-center flex-shrink-0">
                <span className="text-primary font-bold">2</span>
              </div>
              <div>
                <h4 className="font-medium mb-1">Navigate to vercel-app folder</h4>
                <code className="text-sm text-gray-400 bg-white/5 px-2 py-1 rounded">cd vercel-app</code>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-primary/20 rounded-full flex items-center justify-center flex-shrink-0">
                <span className="text-primary font-bold">3</span>
              </div>
              <div>
                <h4 className="font-medium mb-1">Deploy to production</h4>
                <code className="text-sm text-gray-400 bg-white/5 px-2 py-1 rounded">vercel --prod</code>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-8 h-8 bg-secondary/20 rounded-full flex items-center justify-center flex-shrink-0">
                <span className="text-secondary font-bold">✓</span>
              </div>
              <div>
                <h4 className="font-medium mb-1">Your app is live!</h4>
                <p className="text-sm text-gray-400">You'll get a URL like: https://your-app.vercel.app</p>
              </div>
            </div>
          </div>
        </div>

        <div className="glass rounded-2xl p-6">
          <h3 className="text-xl font-semibold mb-4">What Gets Deployed?</h3>
          <div className="space-y-3">
            {[
              { feature: 'Static Dashboard UI', status: '✅ Yes' },
              { feature: 'Real-time Stats Display', status: '✅ Yes' },
              { feature: 'File Browser', status: '✅ Yes' },
              { feature: 'Tier Information', status: '✅ Yes' },
              { feature: 'Python Backend', status: '❌ No (runs locally)' },
              { feature: 'Local File Access', status: '❌ No (security)' },
            ].map((item) => (
              <div key={item.feature} className="flex justify-between items-center p-3 bg-white/5 rounded-lg">
                <span className="text-gray-300">{item.feature}</span>
                <span className={`text-sm ${item.status.includes('✅') ? 'text-secondary' : 'text-gray-500'}`}>
                  {item.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="glass rounded-2xl p-6">
        <h3 className="text-xl font-semibold mb-4">📋 Alternative: GitHub Deploy</h3>
        <div className="space-y-3 text-gray-300">
          <p>1. Push this code to a GitHub repository</p>
          <p>2. Go to <a href="https://vercel.com" target="_blank" className="text-primary hover:underline">vercel.com</a></p>
          <p>3. Click "New Project" and import your repository</p>
          <p>4. Vercel will automatically build and deploy!</p>
        </div>
      </div>

      <div className="gradient-card rounded-2xl p-6 border border-primary/30">
        <h3 className="text-xl font-semibold mb-4">💡 Pro Tip</h3>
        <p className="text-gray-300">
          The deployed dashboard shows static information about your AI Employee. 
          For real-time data, run the Python backend locally and connect it to your deployed frontend,
          or update the stats at build time by copying your vault data.
        </p>
      </div>
    </div>
  )
}
