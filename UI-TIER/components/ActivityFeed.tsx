'use client'

import { useState, useEffect } from 'react'

interface Activity {
  id: string
  type: 'email' | 'task' | 'system'
  action: string
  timestamp: string
  details: string
}

export default function ActivityFeed() {
  const [activities, setActivities] = useState<Activity[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchActivities()
    const interval = setInterval(fetchActivities, 10000)
    return () => clearInterval(interval)
  }, [])

  const fetchActivities = async () => {
    try {
      const response = await fetch('/api/activity')
      const data = await response.json()
      setActivities(data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching activities:', error)
      setLoading(false)
    }
  }

  const mockActivities: Activity[] = [
    {
      id: '1',
      type: 'email',
      action: 'Email Processed',
      timestamp: '2026-03-11 09:30:15',
      details: 'Processed email: Q4 Budget Review Meeting',
    },
    {
      id: '2',
      type: 'task',
      action: 'Task Created',
      timestamp: '2026-03-11 09:30:16',
      details: 'Created task: Review Q4 Budget Proposal',
    },
    {
      id: '3',
      type: 'system',
      action: 'Dashboard Updated',
      timestamp: '2026-03-11 09:30:17',
      details: 'Dashboard statistics refreshed',
    },
    {
      id: '4',
      type: 'task',
      action: 'Task Completed',
      timestamp: '2026-03-11 08:45:22',
      details: 'Completed task: Schedule Team Building Event',
    },
    {
      id: '5',
      type: 'email',
      action: 'Email Received',
      timestamp: '2026-03-11 08:45:10',
      details: 'New email from: sarah.smith@company.com',
    },
    {
      id: '6',
      type: 'system',
      action: 'System Check',
      timestamp: '2026-03-11 08:00:00',
      details: 'All systems operational',
    },
  ]

  const displayActivities = activities.length > 0 ? activities : mockActivities

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'email':
        return '📧'
      case 'task':
        return '✅'
      case 'system':
        return '⚙️'
      default:
        return '📝'
    }
  }

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'email':
        return 'bg-blue-500/20 text-blue-400'
      case 'task':
        return 'bg-purple-500/20 text-purple-400'
      case 'system':
        return 'bg-green-500/20 text-green-400'
      default:
        return 'bg-gray-500/20 text-gray-400'
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-white">Activity Feed</h2>
        <button
          onClick={fetchActivities}
          className="px-4 py-2 bg-primary hover:bg-blue-600 text-white rounded-lg transition-colors duration-200"
        >
          🔄 Refresh
        </button>
      </div>

      <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
        <div className="flow-root">
          <ul className="-mb-8">
            {loading ? (
              <li className="text-center text-gray-400 py-8">Loading activities...</li>
            ) : (
              displayActivities.map((activity, idx) => (
                <li key={activity.id}>
                  <div className="relative pb-8">
                    {idx !== displayActivities.length - 1 && (
                      <span
                        className="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-700"
                        aria-hidden="true"
                      />
                    )}
                    <div className="relative flex space-x-3">
                      <div className={`h-8 w-8 rounded-full flex items-center justify-center ${getTypeColor(activity.type)}`}>
                        <span className="text-sm">{getTypeIcon(activity.type)}</span>
                      </div>
                      <div className="flex min-w-0 flex-1 justify-between space-x-4">
                        <div className="flex-1">
                          <p className="text-sm font-medium text-white">{activity.action}</p>
                          <p className="text-sm text-gray-400">{activity.details}</p>
                        </div>
                        <div className="whitespace-nowrap text-right text-sm text-gray-400">
                          <time dateTime={activity.timestamp}>{activity.timestamp}</time>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              ))
            )}
          </ul>
        </div>
      </div>

      <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
        <h3 className="text-xl font-semibold text-white mb-4">📊 Activity Analytics</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center p-4 bg-white/5 rounded-lg">
            <div className="text-3xl font-bold text-blue-400">24</div>
            <div className="text-sm text-gray-400 mt-1">Emails Today</div>
          </div>
          <div className="text-center p-4 bg-white/5 rounded-lg">
            <div className="text-3xl font-bold text-purple-400">18</div>
            <div className="text-sm text-gray-400 mt-1">Tasks Created</div>
          </div>
          <div className="text-center p-4 bg-white/5 rounded-lg">
            <div className="text-3xl font-bold text-green-400">15</div>
            <div className="text-sm text-gray-400 mt-1">Tasks Completed</div>
          </div>
        </div>
      </div>
    </div>
  )
}
