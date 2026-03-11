'use client'

import { useState, useEffect } from 'react'

interface Email {
  id: string
  subject: string
  sender: string
  timestamp: string
  status: 'unread' | 'processing' | 'completed'
}

export default function EmailList() {
  const [emails, setEmails] = useState<Email[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchEmails()
  }, [])

  const fetchEmails = async () => {
    try {
      const response = await fetch('/api/emails')
      const data = await response.json()
      setEmails(data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching emails:', error)
      setLoading(false)
    }
  }

  const mockEmails: Email[] = [
    {
      id: '1',
      subject: 'Q4 Budget Review Meeting',
      sender: 'john.doe@company.com',
      timestamp: '2026-03-11 09:30 AM',
      status: 'unread',
    },
    {
      id: '2',
      subject: 'Project Deadline Update',
      sender: 'sarah.smith@company.com',
      timestamp: '2026-03-11 08:45 AM',
      status: 'processing',
    },
    {
      id: '3',
      subject: 'Team Building Event',
      sender: 'hr@company.com',
      timestamp: '2026-03-10 04:20 PM',
      status: 'completed',
    },
    {
      id: '4',
      subject: 'Client Feedback - Website Redesign',
      sender: 'client@external.com',
      timestamp: '2026-03-10 02:15 PM',
      status: 'completed',
    },
  ]

  const displayEmails = emails.length > 0 ? emails : mockEmails

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'unread':
        return 'bg-blue-500/20 text-blue-400 border-blue-500/30'
      case 'processing':
        return 'bg-warning/20 text-warning border-warning/30'
      case 'completed':
        return 'bg-success/20 text-success border-success/30'
      default:
        return 'bg-gray-500/20 text-gray-400 border-gray-500/30'
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-white">Email Management</h2>
        <button
          onClick={fetchEmails}
          className="px-4 py-2 bg-primary hover:bg-blue-600 text-white rounded-lg transition-colors duration-200"
        >
          🔄 Refresh
        </button>
      </div>

      <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-white/5">
              <tr>
                <th className="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                  Status
                </th>
                <th className="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                  Subject
                </th>
                <th className="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                  Sender
                </th>
                <th className="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                  Timestamp
                </th>
                <th className="px-6 py-4 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/10">
              {loading ? (
                <tr>
                  <td colSpan={5} className="px-6 py-8 text-center text-gray-400">
                    Loading emails...
                  </td>
                </tr>
              ) : (
                displayEmails.map((email) => (
                  <tr key={email.id} className="hover:bg-white/5 transition-colors duration-200">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`px-3 py-1 rounded-full text-xs font-medium border ${getStatusColor(email.status)}`}>
                        {email.status.charAt(0).toUpperCase() + email.status.slice(1)}
                      </span>
                    </td>
                    <td className="px-6 py-4">
                      <div className="text-sm font-medium text-white">{email.subject}</div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="text-sm text-gray-300">{email.sender}</div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="text-sm text-gray-400">{email.timestamp}</div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <button className="text-primary hover:text-blue-400 transition-colors duration-200">
                        View
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      <div className="rounded-2xl bg-white/5 backdrop-blur-lg border border-white/10 p-6">
        <h3 className="text-xl font-semibold text-white mb-4">📧 Email Processing Settings</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">
              Auto-Check Interval (minutes)
            </label>
            <input
              type="number"
              defaultValue={30}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">
              Max Emails per Cycle
            </label>
            <input
              type="number"
              defaultValue={10}
              className="w-full px-4 py-2 bg-white/10 border border-white/20 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>
        </div>
      </div>
    </div>
  )
}
