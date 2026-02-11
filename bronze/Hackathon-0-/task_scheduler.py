"""
Task Scheduler for Silver Tier AI Assistant
Manages automated tasks and cron-like scheduling
"""

import os
import time
import threading
from datetime import datetime, timedelta
from enum import Enum
import schedule
import atexit

class TaskType(Enum):
    EMAIL_MONITOR = "email_monitor"
    LINKEDIN_POST = "linkedin_post"
    DASHBOARD_UPDATE = "dashboard_update"
    APPROVAL_CHECK = "approval_check"
    REPORT_GENERATION = "report_generation"
    SYSTEM_MAINTENANCE = "system_maintenance"

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TaskScheduler:
    def __init__(self, vault_path="silver_vault"):
        self.vault_path = vault_path
        self.tasks = {}
        self.task_logs_path = os.path.join(vault_path, "Task_Logs")
        os.makedirs(self.task_logs_path, exist_ok=True)
        
        self.scheduler_thread = None
        self.running = False
        
    def add_task(self, task_id, task_func, schedule_rule, task_type=TaskType.SYSTEM_MAINTENANCE, 
                 priority=TaskPriority.MEDIUM, description=""):
        """Add a task to the scheduler"""
        task_info = {
            "id": task_id,
            "function": task_func,
            "schedule_rule": schedule_rule,
            "type": task_type,
            "priority": priority,
            "description": description,
            "last_run": None,
            "next_run": None,
            "enabled": True,
            "run_count": 0
        }
        
        self.tasks[task_id] = task_info
        self._apply_schedule(task_id, schedule_rule)
        
        print(f"Task added: {task_id} ({task_type.value}) - {schedule_rule}")
        return task_id
    
    def _apply_schedule(self, task_id, schedule_rule):
        """Apply the schedule rule to the task"""
        task_info = self.tasks[task_id]
        
        # Parse the schedule rule and apply to schedule library
        if "every" in schedule_rule.lower():
            if "minute" in schedule_rule:
                schedule.every(int(schedule_rule.split()[1])).minutes.do(
                    self._execute_task_wrapper, task_id
                ).tag(task_id)
            elif "hour" in schedule_rule:
                schedule.every(int(schedule_rule.split()[1])).hours.do(
                    self._execute_task_wrapper, task_id
                ).tag(task_id)
            elif "day" in schedule_rule:
                schedule.every(int(schedule_rule.split()[1])).days.do(
                    self._execute_task_wrapper, task_id
                ).tag(task_id)
            elif "second" in schedule_rule:
                schedule.every(int(schedule_rule.split()[1])).seconds.do(
                    self._execute_task_wrapper, task_id
                ).tag(task_id)
        else:
            # Handle specific time schedules
            if schedule_rule.startswith("at "):
                time_part = schedule_rule[3:]  # Remove "at "
                if ":" in time_part:
                    hour, minute = map(int, time_part.split(":"))
                    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(
                        self._execute_task_wrapper, task_id
                    ).tag(task_id)
    
    def _execute_task_wrapper(self, task_id):
        """Wrapper to execute a task and log the results"""
        if task_id in self.tasks and self.tasks[task_id]["enabled"]:
            return self._execute_task(task_id)
    
    def _execute_task(self, task_id):
        """Execute a scheduled task"""
        task_info = self.tasks[task_id]
        
        print(f"Executing task: {task_id}")
        
        # Log task execution
        self.log_task_execution(task_id, "started")
        
        try:
            # Execute the task function
            result = task_info["function"]()
            
            # Update task info
            task_info["last_run"] = datetime.now().isoformat()
            task_info["run_count"] += 1
            
            # Calculate next run time based on schedule
            # This is a simplified calculation
            if "minute" in task_info["schedule_rule"]:
                mins = int(task_info["schedule_rule"].split()[1])
                next_run = datetime.now() + timedelta(minutes=mins)
                task_info["next_run"] = next_run.isoformat()
            
            self.log_task_execution(task_id, "completed", result)
            print(f"Task completed: {task_id}")
            
            return result
        except Exception as e:
            self.log_task_execution(task_id, "failed", str(e))
            print(f"Task failed: {task_id} - {str(e)}")
            return None
    
    def log_task_execution(self, task_id, status, result=None):
        """Log task execution to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"TASK_LOG_{task_id}_{timestamp}.txt"
        filepath = os.path.join(self.task_logs_path, filename)
        
        log_entry = f"""Task Execution Log
=================
Task ID: {task_id}
Status: {status}
Timestamp: {datetime.now().isoformat()}
Result: {str(result)[:500] if result else 'None'}

Task Info:
{self.tasks.get(task_id, {})}
"""
        
        with open(filepath, 'w') as f:
            f.write(log_entry)
    
    def remove_task(self, task_id):
        """Remove a task from the scheduler"""
        if task_id in self.tasks:
            # Cancel the scheduled job
            schedule.clear(task_id)
            del self.tasks[task_id]
            print(f"Task removed: {task_id}")
    
    def enable_task(self, task_id):
        """Enable a task"""
        if task_id in self.tasks:
            self.tasks[task_id]["enabled"] = True
            print(f"Task enabled: {task_id}")
    
    def disable_task(self, task_id):
        """Disable a task"""
        if task_id in self.tasks:
            self.tasks[task_id]["enabled"] = False
            print(f"Task disabled: {task_id}")
    
    def start_scheduler(self):
        """Start the task scheduler in a background thread"""
        if self.running:
            print("Scheduler already running")
            return
        
        self.running = True
        
        def run_scheduler():
            print("Task scheduler started")
            while self.running:
                schedule.run_pending()
                time.sleep(1)  # Check every second
        
        self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        self.scheduler_thread.start()
        
        print("Task scheduler running in background")
    
    def stop_scheduler(self):
        """Stop the task scheduler"""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join()
        print("Task scheduler stopped")
    
    def get_task_status(self):
        """Get status of all tasks"""
        status = {}
        for task_id, task_info in self.tasks.items():
            status[task_id] = {
                "type": task_info["type"].value,
                "priority": task_info["priority"].value,
                "enabled": task_info["enabled"],
                "last_run": task_info["last_run"],
                "run_count": task_info["run_count"],
                "description": task_info["description"]
            }
        return status
    
    def setup_default_tasks(self):
        """Setup default tasks for Silver Tier system"""
        print("Setting up default tasks...")
        
        # Email monitoring task (runs every 15 minutes)
        self.add_task(
            task_id="email_monitor",
            task_func=lambda: print("Monitoring emails..."),
            schedule_rule="every 15 minutes",
            task_type=TaskType.EMAIL_MONITOR,
            priority=TaskPriority.HIGH,
            description="Monitor Gmail for new important emails"
        )
        
        # LinkedIn posting task (runs every 2 hours)
        self.add_task(
            task_id="linkedin_poster",
            task_func=lambda: print("Checking LinkedIn posts..."),
            schedule_rule="every 2 hours",
            task_type=TaskType.LINKEDIN_POST,
            priority=TaskPriority.MEDIUM,
            description="Generate and post LinkedIn sales content"
        )
        
        # Dashboard update task (runs every 30 minutes)
        self.add_task(
            task_id="dashboard_update",
            task_func=lambda: print("Updating dashboard..."),
            schedule_rule="every 30 minutes",
            task_type=TaskType.DASHBOARD_UPDATE,
            priority=TaskPriority.MEDIUM,
            description="Update dashboard with current status"
        )
        
        # Approval check task (runs every 10 minutes)
        self.add_task(
            task_id="approval_checker",
            task_func=lambda: print("Checking pending approvals..."),
            schedule_rule="every 10 minutes",
            task_type=TaskType.APPROVAL_CHECK,
            priority=TaskPriority.HIGH,
            description="Check for pending approvals and expired requests"
        )
        
        # System maintenance task (runs daily at 2 AM)
        self.add_task(
            task_id="system_maintenance",
            task_func=lambda: print("Running system maintenance..."),
            schedule_rule="at 2:00",
            task_type=TaskType.SYSTEM_MAINTENANCE,
            priority=TaskPriority.LOW,
            description="Perform routine system maintenance"
        )

def main():
    print("Initializing Task Scheduler...")
    
    # Initialize the scheduler
    scheduler = TaskScheduler()
    
    # Setup default tasks
    scheduler.setup_default_tasks()
    
    # Show task status
    status = scheduler.get_task_status()
    print(f"\nConfigured tasks: {len(status)}")
    for task_id, info in status.items():
        print(f"  - {task_id}: {info['description']} (Priority: {info['priority']})")
    
    # Start the scheduler
    scheduler.start_scheduler()
    
    print("\nTask Scheduler initialized!")
    print("- Default tasks configured")
    print("- Scheduler running in background")
    print("- Logging to Task_Logs folder")
    
    # Keep the main thread alive for demonstration
    try:
        print("\nScheduler is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(10)  # Sleep to allow other threads to run
    except KeyboardInterrupt:
        print("\nStopping scheduler...")
        scheduler.stop_scheduler()
        print("Scheduler stopped.")

if __name__ == "__main__":
    main()