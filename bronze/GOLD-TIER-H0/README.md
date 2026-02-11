# Gold Tier AI Team - Orchestrated AI System

## Overview
The Gold Tier AI Team is an advanced orchestrated system featuring multiple AI agents working together to monitor, process, analyze, and act on various data sources. This system builds upon the Silver Tier with enhanced capabilities including multi-agent orchestration, advanced MCP integration, comprehensive analytics, and specialized agent skills.

## Features

### Multi-Agent Orchestration
- **Watcher Agent**: Monitors Gmail, LinkedIn, and Calendar
- **Processor Agent**: Analyzes data using Claude reasoning engine
- **Poster Agent**: Handles content posting and communications
- **Analyst Agent**: Generates analytics and reports
- **Coordinator Agent**: Manages workflow orchestration

### Advanced MCP Integration
- API calls to Notion, Google Calendar, and Email services
- Proxy endpoints for external service integration
- Comprehensive API call logging and monitoring

### Analytics Dashboard
- Real-time system status monitoring
- Performance metrics tracking
- Obsidian-compatible dashboard format
- Historical analytics and trend analysis

### Error Handling & Retry Logic
- Automatic error detection and recovery
- Configurable retry mechanisms
- Detailed error logging and reporting
- Graceful degradation capabilities

### Scheduling System
- Daily and weekly task scheduling
- Automated task execution
- Flexible scheduling configurations
- Task history and monitoring

### Specialized Agent Skills
- Email Analysis: Content, sentiment, and urgency analysis
- Content Creation: Post and reply generation
- Calendar Management: Event scheduling and management
- Notion Integration: Page and database management
- Social Media Posting: LinkedIn and Twitter integration
- Data Analytics: Dataset analysis and insights
- Task Coordination: Multi-task workflow management
- Error Handling: Error recovery and escalation

## Architecture

### System Components
```
Gold Tier Orchestrator
├── Multi-Agent System
│   ├── Watcher Agent
│   ├── Processor Agent
│   ├── Poster Agent
│   ├── Analyst Agent
│   └── Coordinator Agent
├── Advanced MCP Server
├── Scheduling System
├── Agent Skills System
└── Analytics Dashboard
```

### Workflow
1. **Watch**: Monitor multiple data sources
2. **Delegate**: Assign tasks to appropriate agents
3. **Execute**: Process and act on data
4. **Report**: Generate analytics and reports
5. **Dashboard**: Update analytics dashboard

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/Syeda-Rohab/GOLD-TIER-H0.git
cd GOLD-TIER-H0

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (optional)
export NOTION_API_KEY="your_notion_api_key"
export CALENDAR_API_KEY="your_calendar_api_key"
```

## Usage

### Quick Start
```bash
# Run the complete orchestrator
python gold_tier_orchestrator.py

# Run individual components
python advanced_mcp_server.py    # MCP server
python scheduling_system.py      # Scheduling system
python agent_skills_system.py    # Agent skills
python demo_script.py            # Run the demo
```

### Environment Variables
- `NOTION_API_KEY`: Notion integration token
- `CALENDAR_API_KEY`: Google Calendar API key
- `SMTP_SERVER`: SMTP server (default: smtp.gmail.com)
- `SMTP_PORT`: SMTP port (default: 587)
- `SENDER_EMAIL`: Email address for sending
- `SENDER_PASSWORD`: App password for email

## File Structure
```
gold_vault/
├── Inbox/                 # Incoming data
├── Needs_Action/          # Items requiring processing
├── Pending_Approval/      # Items awaiting approval
├── Done/                  # Completed tasks
├── Agent_Logs/            # Agent execution logs
├── Analytics/             # Analytics data
├── Schedules/             # Scheduled task logs
├── API_Logs/              # API call logs
├── Watched_Data/          # Monitored data
├── Processed_Data/        # Processed information
├── Posted_Content/        # Published content
├── Error_Logs/            # Error records
├── Reports/               # Generated reports
├── Skills/                # Skill execution logs
└── Dashboard/             # Analytics dashboards
```

## API Endpoints (MCP Server)
- `GET/POST/PATCH/DELETE /notion/*` - Notion API proxy
- `GET/POST/PUT/DELETE /calendar/*` - Calendar API proxy
- `POST /email/send` - Send email
- `GET /status` - Server status
- `GET /analytics` - Detailed analytics
- `GET /health` - Health check

## Configuration
The system comes with default configurations for:
- Daily data sync at 9:00 AM
- Daily report generation at 5:00 PM
- Weekly analytics update on Friday at 10:00 AM
- Weekly maintenance on Sunday at 2:00 AM
- Hourly error checking

## Monitoring
- System status: `/status` endpoint
- Analytics: `/analytics` endpoint
- Health check: `/health` endpoint
- Dashboard files in `gold_vault/Dashboard/`

## Security
- Store API keys securely using environment variables
- Use app-specific passwords for email services
- Regularly rotate API keys
- Monitor API usage and set quotas

## License
MIT License - See LICENSE file for details.