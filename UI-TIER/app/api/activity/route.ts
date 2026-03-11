import { NextResponse } from 'next/server'

export async function GET() {
  try {
    const activities = [
      {
        id: '1',
        type: 'email' as const,
        action: 'Email Processed',
        timestamp: '2026-03-11 09:30:15',
        details: 'Processed email: Q4 Budget Review Meeting',
      },
      {
        id: '2',
        type: 'task' as const,
        action: 'Task Created',
        timestamp: '2026-03-11 09:30:16',
        details: 'Created task: Review Q4 Budget Proposal',
      },
      {
        id: '3',
        type: 'system' as const,
        action: 'Dashboard Updated',
        timestamp: '2026-03-11 09:30:17',
        details: 'Dashboard statistics refreshed',
      },
    ]

    return NextResponse.json(activities)
  } catch (error) {
    console.error('Error fetching activities:', error)
    return NextResponse.json([])
  }
}
