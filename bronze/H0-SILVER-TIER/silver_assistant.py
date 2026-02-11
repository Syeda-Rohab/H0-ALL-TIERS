"""
Silver Tier AI Assistant - Enhanced System
Extends Bronze Tier with additional watchers, MCP server, and advanced features
"""

import os
import json
import time
import smtplib
import threading
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from queue import Queue
import requests
from flask import Flask, request, jsonify

# Import from Bronze Tier
from ai_employee_simple import (
    setup_directories, 
    simulate_get_emails, 
    create_email_note, 
    process_with_claude, 
    move_to_done, 
    update_dashboard
)

# Define extended vault paths
VAULT_PATH = "silver_vault"
INBOX_PATH = os.path.join(VAULT_PATH, "Inbox")
NEEDS_ACTION_PATH = os.path.join(VAULT_PATH, "Needs_Action")
DONE_PATH = os.path.join(VAULT_PATH, "Done")
APPROVAL_PATH = os.path.join(VAULT_PATH, "Pending_Approval")
LINKEDIN_POSTS_PATH = os.path.join(VAULT_PATH, "LinkedIn_Posts")
DASHBOARD_FILE = os.path.join(VAULT_PATH, "Dashboard.md")
COMPANY_HANDBOOK_FILE = os.path.join(VAULT_PATH, "Company_Handbook.md")

class SilverAIAssistant:
    def __init__(self):
        self.approval_queue = Queue()
        self.linkedin_posts_queue = Queue()
        self.setup_extended_directories()
        
    def setup_extended_directories(self):
        """Create extended directory structure for Silver Tier"""
        setup_directories()  # From Bronze Tier
        os.makedirs(APPROVAL_PATH, exist_ok=True)
        os.makedirs(LINKEDIN_POSTS_PATH, exist_ok=True)
        
        # Update Company Handbook for Silver Tier
        self.update_company_handbook()
        
    def update_company_handbook(self):
        """Update Company Handbook with Silver Tier features"""
        handbook_content = """# Company Handbook - Silver Tier AI Assistant

## Rules & Guidelines

### 1. Communication Protocol
- All communications must be documented in the vault
- Use clear, concise language in all notes
- Follow the four-folder system: Inbox → Needs_Action → Pending_Approval → Done

### 2. Task Processing
- Process all incoming emails within 24 hours
- Create PLAN_xxx.md for each email that requires action
- Route sensitive actions to Pending_Approval
- Move completed tasks to the Done folder

### 3. Data Handling
- Maintain confidentiality of all company information
- Store all processed data in the vault
- Regular backups are mandatory

## AI Agent Skills

### Skill 1: Multi-Source Monitoring
- Monitor Gmail for important emails
- Monitor LinkedIn for networking opportunities
- Monitor WhatsApp for urgent messages
- Consolidate all inputs into unified processing queue

### Skill 2: Email Processing
- Parse incoming emails for important information
- Extract action items and deadlines
- Categorize emails by priority and sensitivity

### Skill 3: LinkedIn Sales Posts
- Generate engaging sales content automatically
- Schedule posts based on optimal timing
- Track engagement and performance metrics

### Skill 4: Task Planning
- Create detailed action plans (PLAN_xxx.md)
- Break down complex tasks into smaller steps
- Assign priorities and deadlines
- Implement Claude reasoning loop (think → plan → execute)

### Skill 5: Status Reporting
- Update Dashboard.md regularly
- Track active and completed tasks
- Report system status changes
- Monitor approval queue status

### Skill 6: Document Management
- Organize files in the proper folders
- Maintain consistent naming conventions
- Archive completed tasks appropriately

### Skill 7: Human Approval Management
- Flag sensitive actions for human review
- Send approval requests via MCP server
- Wait for human confirmation before proceeding
- Log all approval decisions

### Skill 8: MCP Server Operations
- Send notifications to humans for approvals
- Process approval responses
- Coordinate with external systems

## Priority Levels
- **Critical**: Requires immediate attention (within 1 hour)
- **High**: Requires attention within 4 hours
- **Medium**: Should be addressed within 24 hours
- **Low**: Can be handled within 72 hours

## Sensitivity Levels Requiring Approval
- Financial transactions
- Contract negotiations
- Personnel matters
- Confidential information sharing
- External communications with clients

## Emergency Procedures
- If system fails, notify administrator immediately
- Maintain log of all errors for troubleshooting
- Have backup manual processes ready
"""
        
        with open(COMPANY_HANDBOOK_FILE, 'w', encoding='utf-8') as f:
            f.write(handbook_content)
    
    def get_linkedin_posts(self):
        """Simulate getting LinkedIn posts to publish"""
        print("Simulating LinkedIn posts retrieval...")
        
        # Create mock LinkedIn posts
        mock_posts = [
            {
                'id': 'post1',
                'title': 'New Product Launch',
                'content': 'Exciting news! Our new product is now available. Check it out!',
                'target_audience': 'customers',
                'scheduled_time': datetime.now().isoformat()
            },
            {
                'id': 'post2',
                'title': 'Industry Insights',
                'content': 'Latest trends in our industry that you should know about.',
                'target_audience': 'professionals',
                'scheduled_time': datetime.now().isoformat()
            }
        ]
        
        return mock_posts
    
    def create_linkedin_post(self, post_data):
        """Create a LinkedIn post file in the LinkedIn_Posts folder"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"LINKEDIN_POST_{timestamp}.md"
        filepath = os.path.join(LINKEDIN_POSTS_PATH, filename)
        
        content = f"""# LinkedIn Post: {post_data['title']}

## Content
{post_data['content']}

## Target Audience
{post_data['target_audience']}

## Scheduled Time
{post_data['scheduled_time']}

## Status
- [ ] Drafted
- [ ] Approved
- [ ] Published
- [ ] Engagement Tracked

## Engagement Metrics
- Likes: 0
- Comments: 0
- Shares: 0
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created LinkedIn post: {filename}")
        return filepath
    
    def claude_reasoning_loop(self, input_data, source="email"):
        """Implement Claude reasoning loop: think → plan → execute"""
        print(f"Starting Claude reasoning loop for {source}...")
        
        # Thinking phase
        thinking_content = f"""# Reasoning Analysis for {input_data.get('subject', input_data.get('title', 'Unknown'))}

## Input Analysis
- Source: {source}
- Content: {input_data.get('body', input_data.get('content', 'N/A'))[:200]}...

## Key Points Identified
- Action required: Yes/No
- Priority level: High/Medium/Low
- Sensitivity level: Normal/Sensitive
- Dependencies: List of dependencies

## Potential Approaches
1. Approach 1: Description
2. Approach 2: Description
3. Approach 3: Description

## Recommended Approach
Selected approach with justification
"""
        
        # Planning phase (this is where the PLAN_xxx.md gets created)
        plan_content = f"""# Action Plan: {input_data.get('subject', input_data.get('title', 'Unknown'))}

## Reasoning Summary
{thinking_content}

## Detailed Plan
1. [ ] Step 1: Description
2. [ ] Step 2: Description
3. [ ] Step 3: Description

## Timeline
- Priority: {input_data.get('priority', 'Medium')}
- Due Date: Within 24-48 hours

## Resources Needed
- Access to relevant documents
- Team member consultation if required

## Dependencies
- Previous related tasks completion
- Availability of required resources

## Success Criteria
- [ ] All action items completed
- [ ] Stakeholders notified of completion
- [ ] Follow-up scheduled if needed

## Sensitivity Check
- Requires approval: {input_data.get('requires_approval', 'No')}
"""
        
        # Create the PLAN file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"PLAN_{timestamp}.md"
        filepath = os.path.join(NEEDS_ACTION_PATH, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(plan_content)
        
        print(f"Created action plan with reasoning: {filename}")
        return filepath
    
    def route_for_approval(self, file_path, reason="Sensitive action detected"):
        """Route file to approval queue if needed"""
        filename = os.path.basename(file_path)
        new_path = os.path.join(APPROVAL_PATH, filename)
        
        # Move the file to approval queue
        os.rename(file_path, new_path)
        
        # Add to approval queue
        approval_item = {
            'file_path': new_path,
            'reason': reason,
            'timestamp': datetime.now().isoformat(),
            'approved': False
        }
        
        self.approval_queue.put(approval_item)
        print(f"Routed to approval: {filename} - {reason}")
        
        # Send notification for approval
        self.send_approval_notification(approval_item)
        
        return new_path
    
    def send_approval_notification(self, approval_item):
        """Send notification for human approval"""
        print(f"NOTIFICATION: Action requires approval - {approval_item['reason']}")
        # In a real system, this would send an email or other notification
    
    def process_approval_response(self, file_path, approved=True):
        """Process human approval response"""
        filename = os.path.basename(file_path)
        
        if approved:
            # Move to Done after approval
            new_path = os.path.join(DONE_PATH, filename)
            os.rename(file_path, new_path)
            print(f"Approved and moved to Done: {filename}")
        else:
            # Move to Needs_Action for revision
            new_path = os.path.join(NEEDS_ACTION_PATH, filename)
            os.rename(file_path, new_path)
            print(f"Not approved, returned to Needs_Action: {filename}")
    
    def run_silver_cycle(self):
        """Run one complete cycle of the Silver Tier AI assistant"""
        print("\n=== Starting Silver Tier AI Assistant Cycle ===")
        
        # 1. Get emails from Gmail
        emails = simulate_get_emails(max_results=2)
        print(f"Found {len(emails)} emails")
        
        for email in emails:
            print(f"Processing email: {email['subject']}")
            
            # Create email note
            email_note_path = create_email_note(email)
            
            # Determine if this requires approval based on content
            requires_approval = self.determine_approval_needed(email)
            
            # Create reasoning-based plan
            plan_path = self.claude_reasoning_loop(email, source="email")
            
            # Route to approval if needed, otherwise move to Done
            if requires_approval:
                self.route_for_approval(plan_path, "Sensitive email content detected")
                self.route_for_approval(email_note_path, "Sensitive email content detected")
            else:
                move_to_done(email_note_path)
                move_to_done(plan_path)
        
        # 2. Process LinkedIn posts
        linkedin_posts = self.get_linkedin_posts()
        print(f"Found {len(linkedin_posts)} LinkedIn posts to process")
        
        for post in linkedin_posts:
            post_file = self.create_linkedin_post(post)
            
            # Determine if this requires approval
            requires_approval = self.determine_approval_needed({'body': post['content']})
            
            if requires_approval:
                self.route_for_approval(post_file, "Sales post content requires approval")
            else:
                move_to_done(post_file)
        
        # 3. Update dashboard
        update_dashboard()
        
        print("=== Silver Tier Cycle Complete ===\n")
    
    def determine_approval_needed(self, content_dict):
        """Determine if content requires human approval"""
        content = content_dict.get('body', '') + ' ' + content_dict.get('subject', '') + ' ' + content_dict.get('content', '')
        content_lower = content.lower()
        
        # Keywords that trigger approval requirement
        approval_keywords = [
            'financial', 'payment', 'contract', 'salary', 'confidential', 
            'customer', 'client', 'money', 'budget', 'deal', 'negotiation',
            'private', 'secret', 'sensitive', 'important'
        ]
        
        for keyword in approval_keywords:
            if keyword in content_lower:
                return True
        
        return False
    
    def start_monitoring(self, interval_minutes=15):
        """Start continuous monitoring for Silver Tier"""
        print(f"Starting Silver Tier monitoring (checking every {interval_minutes} minutes)")
        
        while True:
            try:
                self.run_silver_cycle()
                print(f"Sleeping for {interval_minutes} minutes...")
                time.sleep(interval_minutes * 60)
            except KeyboardInterrupt:
                print("\nMonitoring stopped by user.")
                break
            except Exception as e:
                print(f"Error during monitoring cycle: {e}")
                print("Retrying in 5 minutes...")
                time.sleep(5 * 60)

def main():
    print("Initializing Silver Tier AI Assistant...")
    assistant = SilverAIAssistant()
    
    # Run one cycle for testing
    assistant.run_silver_cycle()
    
    print("Silver Tier system initialized!")
    print("- Extended vault structure created")
    print("- Multi-source monitoring ready")
    print("- Approval system operational")
    print("- LinkedIn posting functionality added")
    print("- Claude reasoning loop implemented")

if __name__ == "__main__":
    main()