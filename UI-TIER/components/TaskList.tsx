'use client'

import { useState, useEffect } from 'react'

interface Task {
  id: string
  title: string
  priority: 'low' | 'medium' | 'high' | 'critical'
  status: 'pending' | 'in_progress' | 'completed'
  dueDate: string
  source: string
}

export default function TaskList() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [filter, setFilter] = useState('all')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    try {
      const response = await fetch('/api/tasks')
      const data = await response.json()
      setTasks(data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching tasks:', error)
      setLoading(false)
    }
  }

  const mockTasks: Task[] = [
    {
      id: '1',
      title: 'Review Q4 Budget Proposal',
      priority: 'high',
      status: 'in_progress',
      dueDate: '2026-03-12',
      source: 'Email: john.doe@company.com',
    },
    {
      id: '2',
      title: 'Update Project Timeline',
      priority: 'medium',
      status: 'pending',
      dueDate: '2026-03-13',
      source: 'Email: sarah.smith@company.com',
    },
    {
      id: '3',
      title: 'Schedule Team Building Event',
      priority: 'low',
      status: 'completed',
      dueDate: '2026-03-15',
      source: 'Email: hr@company.com',
    },
    {
      id: '4',
      title: 'Client Website Revisions',
      priority: 'critical',
      status: 'in_progress',
      dueDate: '2026-03-11',
      source: 'Email: client@external.com',
    },
  ]

  const displayTasks = tasks.length > 0 ? tasks : mockTasks

  const filteredTasks = displayTasks.filter((task) => {
    if (filter === 'all') return true
    if (filter === 'pending') return task.status === 'pending'
    if (filter === 'in_progress') return task.status === 'in_progress'
    if (filter === 'completed') return task.status === 'completed'
    return true
  })

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'critical':
        return 'bg-danger/20 text-danger border-danger/30'
      case 'high':
        return 'bg-orange-500/20 text-orange-400 border-orange-500/30'
      case 'medium':
        return 'bg-warning/20 text-warning border-warning/30'
      case 'low':
        return 'bg-blue-500/20 text-blue-400 border-blue-500/30'
      default:
        return 'bg-gray-500/20 text-gray-400 border-gray-500/30'
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'pending':
        return 'bg-gray-500/20 text-gray-400 border-gray-500/30'
      case 'in_progress':
        return 'bg-primary/20 text-primary border-primary/30'
      case 'completed':
        return 'bg-success/20 text-success border-success/30'
      default:
        return 'bg-gray-500/20 text-gray-400 border-gray-500/30'
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-white">Task Management</h2>
        <div className="flex space-x-2">
          {['all', 'pending', 'in_progress', 'completed'].map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-3 py-1 rounded-lg text-sm font-medium transition-colors duration-200 ${
                filter === f
                  ? 'bg-primary text-white'
                  : 'bg-white/10 text-gray-400 hover:text-white'
              }`}
            >
              {f.replace('_', ' ').charAt(0).toUpperCase() + f.replace('_', ' ').slice(1)}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {loading ? (
          <div className="text-center text-gray-400 py-8">Loading tasks...</div>
        ) : (
          filteredTasks.map((task) => (
            <div
              key={task.id}
              className="rounded-xl bg-white/5 backdrop-blur-lg border border-white/10 p-6 hover:bg-white/10 transition-all duration-200"
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center space-x-3 mb-2">
                    <span className={`px-2 py-1 rounded text-xs font-medium border ${getPriorityColor(task.priority)}`}>
                      {task.priority.toUpperCase()}
                    </span>
                    <span className={`px-2 py-1 rounded text-xs font-medium border ${getStatusColor(task.status)}`}>
                      {task.status.replace('_', ' ').toUpperCase()}
                    </span>
                  </div>
                  <h3 className="text-lg font-semibold text-white mb-2">{task.title}</h3>
                  <div className="flex items-center space-x-4 text-sm text-gray-400">
                    <span>📅 Due: {task.dueDate}</span>
                    <span>📧 {task.source}</span>
                  </div>
                </div>
                <div className="flex space-x-2">
                  <button className="px-3 py-2 bg-primary/20 hover:bg-primary/30 text-primary rounded-lg transition-colors duration-200">
                    View
                  </button>
                  {task.status !== 'completed' && (
                    <button className="px-3 py-2 bg-success/20 hover:bg-success/30 text-success rounded-lg transition-colors duration-200">
                      Complete
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}
