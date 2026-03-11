import { NextResponse } from 'next/server'

export async function GET() {
  try {
    // This would normally fetch from your Python backend
    // For now, returning mock data - you can connect to your actual backend
    const emails = [
      {
        id: '1',
        subject: 'Q4 Budget Review Meeting',
        sender: 'john.doe@company.com',
        timestamp: '2026-03-11 09:30 AM',
        status: 'unread' as const,
      },
      {
        id: '2',
        subject: 'Project Deadline Update',
        sender: 'sarah.smith@company.com',
        timestamp: '2026-03-11 08:45 AM',
        status: 'processing' as const,
      },
      {
        id: '3',
        subject: 'Team Building Event',
        sender: 'hr@company.com',
        timestamp: '2026-03-10 04:20 PM',
        status: 'completed' as const,
      },
    ]

    return NextResponse.json(emails)
  } catch (error) {
    console.error('Error fetching emails:', error)
    return NextResponse.json([])
  }
}
