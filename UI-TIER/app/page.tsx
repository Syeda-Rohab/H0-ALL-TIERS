'use client'

import { useState, useEffect } from 'react'
import Dashboard from '@/components/Dashboard'
import EmailList from '@/components/EmailList'
import TaskList from '@/components/TaskList'
import ActivityFeed from '@/components/ActivityFeed'

export default function Home() {
  const [activeTab, setActiveTab] = useState('dashboard')
  const [stats, setStats] = useState({
    inbox: 0,
    needsAction: 0,
    pendingApproval: 0,
    done: 0,
    totalProcessed: 0,
  })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchStats()
    const interval = setInterval(fetchStats, 30000) // Refresh every 30 seconds
    return () => clearInterval(interval)
  }, [])

  const fetchStats = async () => {
    try {
      const response = await fetch('/api/stats')
      const data = await response.json()
      setStats(data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching stats:', error)
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900">
      <header className="border-b border-white/10 backdrop-blur-sm bg-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-primary to-secondary rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-xl">AI</span>
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">AI Employee</h1>
                <p className="text-sm text-gray-400">Autonomous FTE Management</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                loading ? 'bg-warning/20 text-warning' : 'bg-success/20 text-success'
              }`}>
                {loading ? 'Loading...' : 'System Active'}
              </span>
            </div>
          </div>
        </div>
      </header>

      <nav className="border-b border-white/10 backdrop-blur-sm bg-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-4">
            {[
              { id: 'dashboard', label: 'Dashboard', icon: '📊' },
              { id: 'emails', label: 'Emails', icon: '📧' },
              { id: 'tasks', label: 'Tasks', icon: '✅' },
              { id: 'activity', label: 'Activity', icon: '📈' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-4 py-3 text-sm font-medium transition-all duration-200 border-b-2 ${
                  activeTab === tab.id
                    ? 'border-primary text-white bg-white/10'
                    : 'border-transparent text-gray-400 hover:text-white hover:bg-white/5'
                }`}
              >
                <span className="mr-2">{tab.icon}</span>
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'dashboard' && (
          <Dashboard stats={stats} loading={loading} onRefresh={fetchStats} />
        )}
        {activeTab === 'emails' && <EmailList />}
        {activeTab === 'tasks' && <TaskList />}
        {activeTab === 'activity' && <ActivityFeed />}
      </main>

      <footer className="border-t border-white/10 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <p className="text-center text-sm text-gray-400">
            AI Employee Dashboard © 2026 | Powered by Platinum Tier Autonomous FTE
          </p>
        </div>
      </footer>
    </div>
  )
}
