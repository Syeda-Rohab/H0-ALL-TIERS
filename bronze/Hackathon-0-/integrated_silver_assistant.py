"""
Integrated Silver Tier AI Assistant
Main workflow orchestrator for multi-source processing
"""

import os
import time
import threading
from datetime import datetime
from queue import Queue
import json

# Import all Silver Tier modules
from silver_assistant import SilverAIAssistant
from claude_reasoning import ClaudeReasoningLoop
from human_approval import HumanApprovalSystem
from task_scheduler import TaskScheduler
from enhanced_agent_skills import EnhancedAgentSkills
from linkedin_automation import LinkedInAutomation
from mcp_server import MCPServer

class IntegratedSilverAssistant:
    def __init__(self):
        self.vault_path = "silver_vault"
        self.setup_vault_structure()
        
        # Initialize all Silver Tier components
        self.ai_assistant = SilverAIAssistant()
        self.reasoning_loop = ClaudeReasoningLoop(self.vault_path)
        self.approval_system = HumanApprovalSystem(self.vault_path)
        self.task_scheduler = TaskScheduler(self.vault_path)
        self.agent_skills = EnhancedAgentSkills(self.vault_path)
        self.linkedin_auto = LinkedInAutomation()
        self.mcp_server = MCPServer()
        
        # Initialize processing queues
        self.inbound_queue = Queue()  # For incoming data from various sources
        self.outbound_queue = Queue()  # For outgoing actions
        self.approval_queue = Queue()  # For items requiring approval
        
        # Setup default tasks
        self.setup_default_workflow()
    
    def setup_vault_structure(self):
        """Setup the complete Silver Tier vault structure"""
        os.makedirs(self.vault_path, exist_ok=True)
        folders = [
            "Inbox", "Needs_Action", "Pending_Approval", "Done", 
            "LinkedIn_Posts", "Thinking_Logs", "Task_Logs", "Skills_Log"
        ]
        
        for folder in folders:
            os.makedirs(os.path.join(self.vault_path, folder), exist_ok=True)
        
        print("Silver Tier vault structure created")
    
    def setup_default_workflow(self):
        """Setup the default workflow tasks"""
        print("Setting up integrated workflow...")
        
        # Setup task scheduler with integrated tasks
        self.task_scheduler.add_task(
            task_id="multi_source_monitor",
            task_func=self.monitor_multi_sources,
            schedule_rule="every 10 minutes",
            description="Monitor all sources (Gmail, LinkedIn, etc.)"
        )
        
        self.task_scheduler.add_task(
            task_id="process_inbound_queue",
            task_func=self.process_inbound_queue,
            schedule_rule="every 5 minutes",
            description="Process items in inbound queue"
        )
        
        self.task_scheduler.add_task(
            task_id="check_approvals",
            task_func=self.check_pending_approvals,
            schedule_rule="every 15 minutes",
            description="Check for pending approvals"
        )
        
        self.task_scheduler.add_task(
            task_id="generate_linkedin_posts",
            task_func=self.generate_linkedin_content,
            schedule_rule="every 2 hours",
            description="Generate and schedule LinkedIn sales posts"
        )
        
        self.task_scheduler.add_task(
            task_id="update_dashboard",
            task_func=self.update_dashboard,
            schedule_rule="every 30 minutes",
            description="Update dashboard with current status"
        )
    
    def monitor_multi_sources(self):
        """Monitor multiple sources for new inputs"""
        print("Monitoring multi-sources...")
        
        # Simulate getting data from different sources
        sources_data = {
            "gmail": self.get_simulated_emails(),
            "linkedin": self.get_simulated_linkedin_activity(),
            "other": []  # Could be WhatsApp, etc.
        }
        
        # Add all data to inbound queue
        for source, items in sources_data.items():
            for item in items:
                item['source'] = source
                self.inbound_queue.put(item)
                print(f"Added to queue from {source}: {item.get('subject', item.get('title', 'Unknown'))[:50]}...")
        
        return sources_data
    
    def get_simulated_emails(self):
        """Simulate getting emails (in real implementation, this would connect to Gmail)"""
        return [
            {
                'type': 'email',
                'subject': 'Q4 Budget Approval Required',
                'body': 'Please review and approve the Q4 marketing budget of $50,000 by end of day.',
                'sender': 'finance@company.com',
                'priority': 'high',
                'sensitivity': 'high'
            },
            {
                'type': 'email',
                'subject': 'Team Meeting Tomorrow',
                'body': 'Reminder about the team meeting tomorrow at 10 AM in conference room A.',
                'sender': 'admin@company.com',
                'priority': 'medium',
                'sensitivity': 'normal'
            }
        ]
    
    def get_simulated_linkedin_activity(self):
        """Simulate getting LinkedIn activity"""
        return [
            {
                'type': 'linkedin_post',
                'title': 'New Product Launch',
                'content': 'Exciting news! Our new product is now available. Check it out!',
                'target_audience': 'customers',
                'post_type': 'sales'
            }
        ]
    
    def process_inbound_queue(self):
        """Process items in the inbound queue"""
        print(f"Processing inbound queue ({self.inbound_queue.qsize()} items)...")
        
        processed_count = 0
        while not self.inbound_queue.empty():
            try:
                item = self.inbound_queue.get_nowait()
                
                # Process the item based on its type and source
                result = self.process_single_item(item)
                
                if result:
                    processed_count += 1
                    print(f"Processed: {item.get('subject', item.get('title', 'Unknown'))[:50]}...")
                
            except:
                # Queue is empty
                break
        
        print(f"Processed {processed_count} items from inbound queue")
        return processed_count
    
    def process_single_item(self, item):
        """Process a single item through the complete workflow"""
        try:
            print(f"Processing item from {item['source']}: {item.get('subject', item.get('title', 'Unknown'))[:50]}...")
            
            # Step 1: Use agent skills to classify and analyze
            if item['type'] == 'email':
                processed_data = self.agent_skills.execute_email_processing_skill(item)
            elif item['type'] == 'linkedin_post':
                processed_data = self.agent_skills.execute_sales_posting_skill(
                    item['content'], item.get('target_audience', 'general')
                )
            else:
                # Generic processing
                processed_data = {
                    "original_item": item,
                    "processed_at": datetime.now().isoformat(),
                    "action_required": True
                }
            
            # Step 2: Apply Claude reasoning loop
            reasoning_result = self.reasoning_loop.run_reasoning_loop(item)
            
            # Step 3: Check if approval is needed
            if self.requires_approval(processed_data):
                # Submit for approval
                approval_id = self.approval_system.submit_for_approval(
                    processed_data,
                    self.determine_approval_type(item)
                )
                print(f"Submitted for approval: {approval_id}")
            else:
                # Skip approval, proceed directly
                self.execute_approved_action(item, processed_data)
            
            # Step 4: Update dashboard
            self.update_dashboard()
            
            return True
            
        except Exception as e:
            print(f"Error processing item: {str(e)}")
            return False
    
    def requires_approval(self, processed_data):
        """Determine if an item requires approval"""
        # Check if the processed data indicates high sensitivity or risk
        if isinstance(processed_data, dict):
            sensitivity = processed_data.get('sensitivity', 'normal')
            priority = processed_data.get('priority', 'medium')
            
            if sensitivity == 'high' or priority == 'high':
                return True
        
        # Check original email content for sensitive keywords
        original = processed_data.get('original_email', {})
        content = original.get('body', '') + ' ' + original.get('subject', '')
        content_lower = content.lower()
        
        sensitive_keywords = [
            'financial', 'payment', 'contract', 'salary', 'confidential', 
            'customer', 'client', 'money', 'budget', 'deal', 'negotiation'
        ]
        
        for keyword in sensitive_keywords:
            if keyword in content_lower:
                return True
        
        return False
    
    def determine_approval_type(self, item):
        """Determine the appropriate approval type"""
        from human_approval import ApprovalType
        
        content = item.get('body', '') + ' ' + item.get('subject', '') + ' ' + item.get('content', '')
        content_lower = content.lower()
        
        if any(word in content_lower for word in ['financial', 'budget', 'payment', 'money']):
            return ApprovalType.FINANCIAL
        elif any(word in content_lower for word in ['contract', 'agreement', 'legal']):
            return ApprovalType.CONTRACT
        elif any(word in content_lower for word in ['personnel', 'hr', 'employee', 'salary']):
            return ApprovalType.PERSONNEL
        elif any(word in content_lower for word in ['confidential', 'private', 'secret']):
            return ApprovalType.CONFIDENTIAL
        elif any(word in content_lower for word in ['customer', 'client', 'account']):
            return ApprovalType.CUSTOMER
        else:
            return ApprovalType.GENERAL
    
    def execute_approved_action(self, item, processed_data):
        """Execute an action that has been approved"""
        print(f"Executing approved action: {item.get('subject', item.get('title', 'Unknown'))[:50]}...")
        
        # Based on the item type, execute the appropriate action
        if item['type'] == 'email':
            # Create action plan and move to Done
            plan_file = self.create_action_plan(item)
            self.move_to_done(item, plan_file)
        elif item['type'] == 'linkedin_post':
            # Handle LinkedIn post
            self.handle_linkedin_post(item)
        
        return True
    
    def create_action_plan(self, item):
        """Create an action plan for the item"""
        # Use Claude reasoning to create a detailed plan
        reasoning_result = self.reasoning_loop.run_reasoning_loop(item)
        return reasoning_result.get('plan_file')
    
    def move_to_done(self, item, plan_file=None):
        """Move processed item to Done folder"""
        # In the full implementation, this would move files appropriately
        print(f"Moved to Done: {item.get('subject', item.get('title', 'Unknown'))}")
    
    def handle_linkedin_post(self, item):
        """Handle LinkedIn post processing"""
        # Create post file in LinkedIn_Posts folder
        post_file = self.linkedin_auto.create_post_file(
            item['content'],
            item.get('post_type', 'general'),
            item.get('target_audience', 'general')
        )
        print(f"LinkedIn post created: {post_file}")
    
    def check_pending_approvals(self):
        """Check for and process pending approvals"""
        print("Checking pending approvals...")
        
        # Run approval system cycle
        self.approval_system.run_approval_cycle()
        
        # In a real system, this would also check for responses to approval requests
        pending = self.approval_system.get_pending_approvals()
        print(f"Currently pending approvals: {len(pending)}")
        
        return pending
    
    def generate_linkedin_content(self):
        """Generate LinkedIn sales content"""
        print("Generating LinkedIn content...")
        
        # Use LinkedIn automation to create posts
        self.linkedin_auto.run_auto_posting_cycle()
        
        return True
    
    def update_dashboard(self):
        """Update the dashboard with current status"""
        print("Updating dashboard...")
        
        # Create/update dashboard file
        dashboard_path = os.path.join(self.vault_path, "Dashboard.md")
        
        # Count items in each folder
        import os
        inbox_count = len([f for f in os.listdir(os.path.join(self.vault_path, "Inbox")) if f.endswith('.md')])
        needs_action_count = len([f for f in os.listdir(os.path.join(self.vault_path, "Needs_Action")) if f.endswith('.md')])
        pending_approval_count = len([f for f in os.listdir(os.path.join(self.vault_path, "Pending_Approval")) if f.endswith('.md')])
        done_count = len([f for f in os.listdir(os.path.join(self.vault_path, "Done")) if f.endswith('.md')])
        linkedin_posts_count = len([f for f in os.listdir(os.path.join(self.vault_path, "LinkedIn_Posts")) if f.endswith('.md')])
        
        dashboard_content = f"""# Silver Tier AI Assistant Dashboard

## System Status
- **Active Tasks**: {needs_action_count}
- **Pending Approval**: {pending_approval_count}
- **Completed Tasks**: {done_count}
- **System Status**: Operational
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Source Monitoring
- **Gmail**: Active
- **LinkedIn**: Active
- **Other Sources**: Configured

## Queue Status
- **Inbound Queue**: {self.inbound_queue.qsize()} items
- **Outbound Queue**: {self.outbound_queue.qsize()} items

## Content Generation
- **LinkedIn Posts**: {linkedin_posts_count} posts managed
- **Auto Posts Scheduled**: Enabled
- **Engagement Tracking**: Active

## Approval System
- **Pending Requests**: {pending_approval_count}
- **Auto-Approval Enabled**: For low-risk items
- **Notification System**: Active

## Task Scheduler
- **Active Tasks**: {len(self.task_scheduler.tasks)} configured
- **Next Runs**: See Task_Logs for details

## Recent Activity
- Multi-source monitoring active
- Claude reasoning loop operational
- Enhanced agent skills engaged
- MCP server ready for notifications

## Generated By
Silver Tier AI Assistant
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)
        
        print("Dashboard updated")
        return True
    
    def start_system(self):
        """Start the complete Silver Tier system"""
        print("Starting Integrated Silver Tier AI Assistant...")
        
        # Start the task scheduler
        self.task_scheduler.start_scheduler()
        
        # Start MCP server in background thread
        def start_mcp():
            from flask import Flask
            app = Flask(__name__)
            
            @app.route('/status')
            def status():
                return {'status': 'silver_tier_operational', 'timestamp': datetime.now().isoformat()}
            
            app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
        
        mcp_thread = threading.Thread(target=start_mcp, daemon=True)
        mcp_thread.start()
        
        print("Silver Tier system operational!")
        print("- Multi-source monitoring active")
        print("- Task scheduler running")
        print("- Approval system ready")
        print("- Dashboard auto-updating")
        print("- MCP server listening on port 5000")
    
    def run_manual_cycle(self):
        """Run one manual cycle of the complete workflow"""
        print("\n=== Running Manual Silver Tier Cycle ===")
        
        # Step 1: Monitor sources
        sources_data = self.monitor_multi_sources()
        
        # Step 2: Process inbound queue
        processed = self.process_inbound_queue()
        
        # Step 3: Check approvals
        pending = self.check_pending_approvals()
        
        # Step 4: Update dashboard
        self.update_dashboard()
        
        print(f"Manual cycle completed:")
        print(f"  - Sources monitored: {len(sources_data)}")
        print(f"  - Items processed: {processed}")
        print(f"  - Pending approvals: {len(pending)}")
        print("=== Cycle Complete ===\n")

def main():
    print("Initializing Integrated Silver Tier AI Assistant...")
    
    # Initialize the integrated system
    integrated_assistant = IntegratedSilverAssistant()
    
    # Run a manual cycle to demonstrate the workflow
    integrated_assistant.run_manual_cycle()
    
    # Start the full system
    integrated_assistant.start_system()
    
    print("\nSilver Tier AI Assistant fully operational!")
    print("All components integrated and working together:")
    print("- Multi-source monitoring (Gmail, LinkedIn)")
    print("- Claude reasoning loop")
    print("- Human approval system")
    print("- Task scheduling")
    print("- Enhanced agent skills")
    print("- MCP server operations")
    print("- Dashboard updates")
    
    # Keep the main thread alive
    try:
        print("\nSystem is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(10)  # Sleep to allow other threads to run
    except KeyboardInterrupt:
        print("\nShutting down Silver Tier system...")
        integrated_assistant.task_scheduler.stop_scheduler()
        print("System shutdown complete.")

if __name__ == "__main__":
    main()