'use client'

interface DashboardProps {
  stats: {
    inbox: number
    needsAction: number
    pendingApproval: number
    done: number
    totalProcessed: number
  }
  loading: boolean
  onRefresh: () => void
}

export default function Dashboard({ stats, loading, onRefresh }: DashboardProps) {
  const statCards = [
    {
      title: 'Inbox',
      value: stats.inbox,
      icon: '📥',
      color: 'from-blue-500 to-blue-600',
      description: 'New emails received',
    },
    {
      title: 'Needs Action',
      value: stats.needsAction,
      icon: '⚡',
      color: 'from-warning to-orange-600',
      description: 'Pending tasks',
    },
    {
      title: 'Pending Approval',
      value: stats.pendingApproval,
      icon: '⏳',
      color: 'from-purple-500 to-purple-600',
      description: 'Awaiting review',
    },
    {
      title: 'Completed',
      value: stats.done,
      icon: '✅',
      color: 'from-success to-green-600',
      description: 'Tasks completed',
    },
  ]

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-white">Overview</h2>
        <button
          onClick={onRefresh}
          disabled={loading}
          className="px-4 py-2 bg-primary hover:bg-blue-600 disabled:bg-gray-600 text-white rounded-lg transition-colors duration-200 flex items-center space-x-2"
        >
          <span>🔄</span>
          <span>{loading ? 'Refreshing...' : 'Refresh'}</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {statCards.map((card) => (
          <div
            key={card.title}
            className="relative overflow-hidden rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6 hover:bg-white/10 transition-all duration-300 hover:scale-105"
          >
            <div className={`absolute top-0 right-0 w-24 h-24 bg-gradient-to-br ${card.color} opacity-20 rounded-full -mr-8 -mt-8`}></div>
            <div className="relative">
              <div className="flex items-center justify-between mb-4">
                <span className="text-4xl">{card.icon}</span>
                <div className={`w-12 h-12 bg-gradient-to-br ${card.color} rounded-lg flex items-center justify-center`}>
                  <span className="text-white font-bold text-lg">{card.value}</span>
                </div>
              </div>
              <h3 className="text-lg font-semibold text-white mb-1">{card.title}</h3>
              <p className="text-sm text-gray-400">{card.description}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
          <h3 className="text-xl font-semibold text-white mb-4">📊 Processing Statistics</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-400">Total Processed Today</span>
              <span className="text-white font-semibold">{stats.totalProcessed}</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-400">Success Rate</span>
              <span className="text-success font-semibold">98.5%</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-400">Average Response Time</span>
              <span className="text-white font-semibold">~2.3s</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-400">System Uptime</span>
              <span className="text-success font-semibold">99.9%</span>
            </div>
          </div>
        </div>

        <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
          <h3 className="text-xl font-semibold text-white mb-4">🚀 Quick Actions</h3>
          <div className="space-y-3">
            <button className="w-full px-4 py-3 bg-gradient-to-r from-primary to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white rounded-lg transition-all duration-200 flex items-center justify-center space-x-2">
              <span>📧</span>
              <span>Process Emails Now</span>
            </button>
            <button className="w-full px-4 py-3 bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700 text-white rounded-lg transition-all duration-200 flex items-center justify-center space-x-2">
              <span>📋</span>
              <span>Generate Report</span>
            </button>
            <button className="w-full px-4 py-3 bg-gradient-to-r from-success to-green-600 hover:from-green-600 hover:to-green-700 text-white rounded-lg transition-all duration-200 flex items-center justify-center space-x-2">
              <span>🔧</span>
              <span>System Settings</span>
            </button>
          </div>
        </div>
      </div>

      <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
        <h3 className="text-xl font-semibold text-white mb-4">📈 System Status</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Gmail Integration</span>
          </div>
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Task Processor</span>
          </div>
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Dashboard API</span>
          </div>
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Analytics Engine</span>
          </div>
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Auto-Scheduler</span>
          </div>
          <div className="flex items-center space-x-3">
            <div className="w-3 h-3 bg-success rounded-full animate-pulse"></div>
            <span className="text-gray-300">Data Vault</span>
          </div>
        </div>
      </div>
    </div>
  )
}
