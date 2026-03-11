import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET() {
  try {
    // Define vault paths - adjust based on your actual structure
    const basePaths = [
      path.join(process.cwd(), '..', 'bronze', 'bronze_vault'),
      path.join(process.cwd(), '..', 'PLATINUM-TIER', 'platinum_vault'),
    ]

    let stats = {
      inbox: 0,
      needsAction: 0,
      pendingApproval: 0,
      done: 0,
      totalProcessed: 0,
    }

    for (const basePath of basePaths) {
      if (fs.existsSync(basePath)) {
        const inboxPath = path.join(basePath, 'Inbox')
        const needsActionPath = path.join(basePath, 'Needs_Action')
        const pendingApprovalPath = path.join(basePath, 'Pending_Approval')
        const donePath = path.join(basePath, 'Done')

        if (fs.existsSync(inboxPath)) {
          stats.inbox += fs.readdirSync(inboxPath).filter(f => f.endsWith('.md')).length
        }
        if (fs.existsSync(needsActionPath)) {
          stats.needsAction += fs.readdirSync(needsActionPath).filter(f => f.endsWith('.md')).length
        }
        if (fs.existsSync(pendingApprovalPath)) {
          stats.pendingApproval += fs.readdirSync(pendingApprovalPath).filter(f => f.endsWith('.md')).length
        }
        if (fs.existsSync(donePath)) {
          stats.done += fs.readdirSync(donePath).filter(f => f.endsWith('.md')).length
        }
      }
    }

    stats.totalProcessed = stats.done

    return NextResponse.json(stats)
  } catch (error) {
    console.error('Error fetching stats:', error)
    return NextResponse.json({
      inbox: 0,
      needsAction: 0,
      pendingApproval: 0,
      done: 0,
      totalProcessed: 0,
    })
  }
}
