# Gold Tier AI Team - Deployment Guide

## Overview
This guide explains how to deploy and run the Gold Tier Orchestrated AI Team system.

## System Requirements
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Syeda-Rohab/GOLD-TIER-H0.git
cd GOLD-TIER-H0
```

### 2. Install Dependencies
```bash
pip install flask schedule requests
```

### 3. Set Up Environment Variables (Optional)
```bash
export NOTION_API_KEY="your_notion_api_key"
export CALENDAR_API_KEY="your_calendar_api_key"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT=587
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your_app_password"
```

## Running the System

### 1. Quick Start (Demo Mode)
```bash
python gold_tier_orchestrator.py
```

### 2. Individual Components
You can also run individual components:

#### Run the main orchestrator:
```bash
python gold_tier_orchestrator.py
```

#### Run the MCP server independently:
```bash
python advanced_mcp_server.py
```

#### Run the scheduling system:
```bash
python scheduling_system.py
```

#### Test the agent skills:
```bash
python agent_skills_system.py
```

## Configuration

### API Keys
To use real API integrations, configure these environment variables:

- `NOTION_API_KEY`: Your Notion integration token
- `CALENDAR_API_KEY`: Your Google Calendar API key
- `SMTP_SERVER`: Your SMTP server (default: smtp.gmail.com)
- `SMTP_PORT`: SMTP port (default: 587)
- `SENDER_EMAIL`: Email address for sending
- `SENDER_PASSWORD`: App password for email

### Scheduling Configuration
The system comes with default schedules:
- Daily data sync at 9:00 AM
- Daily report generation at 5:00 PM
- Weekly analytics update on Friday at 10:00 AM
- Weekly maintenance on Sunday at 2:00 AM
- Hourly error checking

You can customize these in `scheduling_system.py`.

## System Architecture

### Components
1. **Multi-Agent System**:
   - Watcher Agent: Monitors sources (Gmail, LinkedIn, Calendar)
   - Processor Agent: Analyzes and processes data
   - Poster Agent: Handles content posting
   - Analyst Agent: Manages analytics and reporting
   - Coordinator Agent: Orchestrates workflows

2. **Advanced MCP Server**:
   - API integration for Notion, Calendar, Email
   - Proxy endpoints for external services
   - Analytics and monitoring

3. **Scheduling System**:
   - Daily/weekly task scheduling
   - Automated execution
   - Task history and logging

4. **Agent Skills System**:
   - 5+ specialized skills
   - Email analysis
   - Content creation
   - Calendar management
   - Notion integration
   - Social media posting
   - Data analytics
   - Task coordination
   - Error handling

## Usage Examples

### 1. Trigger a Manual Orchestration Cycle
```python
from gold_tier_orchestrator import GoldTierOrchestrator

orchestrator = GoldTierOrchestrator()
orchestrator.run_full_orchestration_cycle()
```

### 2. Execute Specific Skills
```python
from agent_skills_system import AgentSkillsSystem

skills = AgentSkillsSystem()
result = skills.execute_skill(
    "email_analysis", 
    {
        "subject": "Meeting Request", 
        "body": "Can we schedule a meeting for tomorrow?"
    }
)
```

### 3. Schedule Custom Tasks
```python
from scheduling_system import GoldTierScheduler, TaskFrequency, TaskType

scheduler = GoldTierScheduler()
scheduler.add_custom_schedule(
    task_id="custom_task",
    task_func=lambda: print("Custom task executed!"),
    frequency=TaskFrequency.DAILY,
    time_spec="09:00",
    task_type=TaskType.DATA_SYNC,
    description="Custom daily task"
)
```

## Monitoring and Analytics

### Dashboard
The system generates analytics dashboards in the `gold_vault/Dashboard/` folder in Obsidian-compatible format.

### Logs
- Agent logs: `gold_vault/Agent_Logs/`
- API logs: `gold_vault/API_Logs/`
- Error logs: `gold_vault/Error_Logs/`
- Reports: `gold_vault/Reports/`
- Skills logs: `gold_vault/Skills/`

## Troubleshooting

### Common Issues
1. **API Connection Errors**: Check your API keys and network connectivity
2. **Permission Errors**: Ensure the system has write access to the vault directory
3. **Scheduling Issues**: Verify system clock is accurate

### Error Handling
The system includes robust error handling with:
- Automatic retries for transient failures
- Detailed error logging
- Graceful degradation when services are unavailable

## Production Deployment

### 1. Using a WSGI Server
For production, run the MCP server using Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5001 advanced_mcp_server:app
```

### 2. Systemd Service (Linux)
Create a systemd service file to run the orchestrator as a system service.

### 3. Docker Containerization
The system can be containerized using Docker for easy deployment.

## Security Considerations
- Store API keys securely using environment variables
- Use app-specific passwords for email services
- Regularly rotate API keys
- Monitor API usage and set quotas

## Maintenance
- Regularly check error logs
- Monitor system performance
- Update dependencies periodically
- Backup the vault directory regularly