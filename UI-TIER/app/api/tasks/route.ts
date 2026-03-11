import { NextResponse } from 'next/server'

export async function GET() {
  try {
    const tasks = [
      {
        id: '1',
        title: 'Review Q4 Budget Proposal',
        priority: 'high' as const,
        status: 'in_progress' as const,
        dueDate: '2026-03-12',
        source: 'Email: john.doe@company.com',
      },
      {
        id: '2',
        title: 'Update Project Timeline',
        priority: 'medium' as const,
        status: 'pending' as const,
        dueDate: '2026-03-13',
        source: 'Email: sarah.smith@company.com',
      },
      {
        id: '3',
        title: 'Schedule Team Building Event',
        priority: 'low' as const,
        status: 'completed' as const,
        dueDate: '2026-03-15',
        source: 'Email: hr@company.com',
      },
    ]

    return NextResponse.json(tasks)
  } catch (error) {
    console.error('Error fetching tasks:', error)
    return NextResponse.json([])
  }
}
