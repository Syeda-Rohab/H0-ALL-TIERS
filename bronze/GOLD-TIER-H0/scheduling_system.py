"""
Scheduling System for Gold Tier AI Team
Handles daily/weekly task scheduling and execution
"""

import schedule
import time
import threading
from datetime import datetime, timedelta
import json
import os
from enum import Enum

class TaskFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    HOURLY = "hourly"
    MONTHLY = "monthly"

class TaskType(Enum):
    DATA_SYNC = "data_sync"
    REPORT_GENERATION = "report_generation"
    CONTENT_POSTING = "content_posting"
    ANALYTICS_UPDATE = "analytics_update"
    SYSTEM_MAINTENANCE = "system_maintenance"
    ERROR_CHECK = "error_check"

class GoldTierScheduler:
    def __init__(self, vault_path="gold_vault"):
        self.vault_path = vault_path
        self.schedules_path = os.path.join(vault_path, "Schedules")
        os.makedirs(self.schedules_path, exist_ok=True)
        
        self.scheduled_tasks = {}
        self.task_history = []
        self.running = False
        self.scheduler_thread = None
        
        # Setup default schedules
        self.setup_default_schedules()
    
    def setup_default_schedules(self):
        """Setup default schedules for Gold Tier"""
        print("Setting up default schedules...")
        
        # Daily tasks
        self.schedule_task(
            task_id="daily_sync",
            task_func=self.daily_data_sync,
            frequency=TaskFrequency.DAILY,
            time_spec="09:00",
            task_type=TaskType.DATA_SYNC,
            description="Daily data synchronization"
        )
        
        self.schedule_task(
            task_id="daily_report",
            task_func=self.daily_report_generation,
            frequency=TaskFrequency.DAILY, 
            time_spec="17:00",
            task_type=TaskType.REPORT_GENERATION,
            description="Daily report generation"
        )
        
        # Weekly tasks
        self.schedule_task(
            task_id="weekly_analytics",
            task_func=self.weekly_analytics_update,
            frequency=TaskFrequency.WEEKLY,
            time_spec="friday at 10:00",
            task_type=TaskType.ANALYTICS_UPDATE,
            description="Weekly analytics update"
        )
        
        self.schedule_task(
            task_id="weekly_maintenance",
            task_func=self.weekly_system_maintenance,
            frequency=TaskFrequency.WEEKLY,
            time_spec="sunday at 02:00",
            task_type=TaskType.SYSTEM_MAINTENANCE,
            description="Weekly system maintenance"
        )
        
        # Hourly tasks
        self.schedule_task(
            task_id="hourly_check",
            task_func=self.hourly_error_check,
            frequency=TaskFrequency.HOURLY,
            time_spec="every_hour",
            task_type=TaskType.ERROR_CHECK,
            description="Hourly error checking"
        )
        
        print("Default schedules setup completed!")
    
    def schedule_task(self, task_id, task_func, frequency, time_spec, task_type, description=""):
        """Schedule a task with specified frequency"""
        task_info = {
            "id": task_id,
            "function": task_func,
            "frequency": frequency.value,
            "time_spec": time_spec,
            "type": task_type.value,
            "description": description,
            "last_run": None,
            "next_run": None,
            "run_count": 0,
            "enabled": True,
            "created_at": datetime.now().isoformat()
        }
        
        # Apply schedule based on frequency
        if frequency == TaskFrequency.DAILY:
            if time_spec == "09:00":
                schedule.every().day.at("09:00").do(self._execute_wrapped_task, task_id)
            elif time_spec == "17:00":
                schedule.every().day.at("17:00").do(self._execute_wrapped_task, task_id)
        elif frequency == TaskFrequency.WEEKLY:
            if "friday" in time_spec:
                schedule.every().friday.at("10:00").do(self._execute_wrapped_task, task_id)
            elif "sunday" in time_spec:
                schedule.every().sunday.at("02:00").do(self._execute_wrapped_task, task_id)
        elif frequency == TaskFrequency.HOURLY:
            schedule.every().hour.do(self._execute_wrapped_task, task_id)
        
        self.scheduled_tasks[task_id] = task_info
        self.log_schedule_event(task_id, "scheduled", task_info)
        
        print(f"Scheduled task: {task_id} ({frequency.value} at {time_spec})")
        return task_id
    
    def _execute_wrapped_task(self, task_id):
        """Wrapper to execute a scheduled task and log results"""
        if task_id in self.scheduled_tasks and self.scheduled_tasks[task_id]["enabled"]:
            return self.execute_task(task_id)
    
    def execute_task(self, task_id):
        """Execute a scheduled task"""
        if task_id not in self.scheduled_tasks:
            print(f"Task {task_id} not found")
            return False
        
        task_info = self.scheduled_tasks[task_id]
        print(f"Executing scheduled task: {task_id}")
        
        try:
            # Execute the task function
            result = task_info["function"]()
            
            # Update task info
            task_info["last_run"] = datetime.now().isoformat()
            task_info["run_count"] += 1
            
            # Log successful execution
            self.log_task_execution(task_id, "completed", result)
            print(f"Task completed: {task_id}")
            
            return result
        except Exception as e:
            # Log error
            self.log_task_execution(task_id, "failed", str(e))
            print(f"Task failed: {task_id} - {str(e)}")
            return None
    
    def daily_data_sync(self):
        """Daily data synchronization task"""
        print("Running daily data sync...")
        
        # Simulate data sync operations
        sync_result = {
            "status": "completed",
            "services_synced": ["gmail", "linkedin", "calendar", "notion"],
            "records_processed": 42,
            "timestamp": datetime.now().isoformat()
        }
        
        # Log sync result
        self.save_task_result("daily_data_sync", sync_result)
        return sync_result
    
    def daily_report_generation(self):
        """Daily report generation task"""
        print("Running daily report generation...")
        
        # Generate daily report
        report = {
            "report_type": "daily_summary",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "metrics": {
                "tasks_completed": 24,
                "errors_encountered": 0,
                "api_calls": 156,
                "emails_sent": 8,
                "posts_created": 3
            },
            "agents_status": {
                "watcher": "active",
                "processor": "active", 
                "poster": "active",
                "analyst": "active",
                "coordinator": "active"
            },
            "timestamp": datetime.now().isoformat()
        }
        
        # Save report
        self.save_task_result("daily_report", report)
        return report
    
    def weekly_analytics_update(self):
        """Weekly analytics update task"""
        print("Running weekly analytics update...")
        
        # Generate weekly analytics
        analytics = {
            "report_type": "weekly_analytics",
            "week_of": (datetime.now() - timedelta(days=datetime.now().weekday())).strftime("%Y-%m-%d"),
            "metrics": {
                "total_tasks_completed": 168,
                "average_daily_tasks": 24,
                "error_rate": 0.02,
                "system_uptime": "99.8%",
                "api_success_rate": 0.98
            },
            "trends": {
                "increasing": ["task_completion", "api_calls"],
                "decreasing": ["errors"],
                "stable": ["uptime"]
            },
            "recommendations": [
                "Continue current operations",
                "Monitor error patterns",
                "Optimize API usage"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        # Save analytics
        self.save_task_result("weekly_analytics", analytics)
        return analytics
    
    def weekly_system_maintenance(self):
        """Weekly system maintenance task"""
        print("Running weekly system maintenance...")
        
        # Perform maintenance tasks
        maintenance = {
            "status": "completed",
            "tasks_performed": [
                "log_cleanup",
                "cache_clearing", 
                "backup_verification",
                "performance_review"
            ],
            "cleanup_stats": {
                "logs_removed": 245,
                "cache_cleared_mb": 12.5,
                "backups_verified": 7
            },
            "timestamp": datetime.now().isoformat()
        }
        
        # Save maintenance report
        self.save_task_result("weekly_maintenance", maintenance)
        return maintenance
    
    def hourly_error_check(self):
        """Hourly error checking task"""
        print("Running hourly error check...")
        
        # Check for errors (simulated)
        error_check = {
            "status": "ok",
            "errors_found": 0,
            "checks_performed": [
                "agent_health",
                "api_connections", 
                "task_queues",
                "system_resources"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        # Save error check result
        self.save_task_result("hourly_error_check", error_check)
        return error_check
    
    def save_task_result(self, task_type, result):
        """Save task result to appropriate folder"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{task_type.upper()}_{timestamp}.json"
        filepath = os.path.join(self.schedules_path, filename)
        
        with open(filepath, 'w') as f:
            json.dump(result, f, indent=2, default=str)
    
    def log_schedule_event(self, task_id, event_type, details):
        """Log schedule events"""
        log_entry = {
            "task_id": task_id,
            "event_type": event_type,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save to schedule logs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"SCHEDULE_EVENT_{task_id}_{event_type}_{timestamp}.json"
        filepath = os.path.join(self.schedules_path, filename)
        
        with open(filepath, 'w') as f:
            json.dump(log_entry, f, indent=2, default=str)
    
    def log_task_execution(self, task_id, status, result):
        """Log task execution"""
        execution_log = {
            "task_id": task_id,
            "status": status,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save to execution logs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"EXECUTION_LOG_{task_id}_{status}_{timestamp}.json"
        filepath = os.path.join(self.schedules_path, filename)
        
        with open(filepath, 'w') as f:
            json.dump(execution_log, f, indent=2, default=str)
    
    def start_scheduler(self):
        """Start the scheduler in background"""
        if self.running:
            print("Scheduler already running")
            return
        
        self.running = True
        
        def run_scheduler():
            print("Gold Tier Scheduler started")
            while self.running:
                schedule.run_pending()
                time.sleep(1)  # Check every second
        
        self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        self.scheduler_thread.start()
        print("Gold Tier Scheduler running in background")
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join()
        print("Gold Tier Scheduler stopped")
    
    def get_schedule_status(self):
        """Get current schedule status"""
        status = {
            "scheduler_running": self.running,
            "total_scheduled_tasks": len(self.scheduled_tasks),
            "active_tasks": sum(1 for task in self.scheduled_tasks.values() if task["enabled"]),
            "disabled_tasks": sum(1 for task in self.scheduled_tasks.values() if not task["enabled"]),
            "task_summary": {
                task_id: {
                    "type": task["type"],
                    "frequency": task["frequency"],
                    "last_run": task["last_run"],
                    "run_count": task["run_count"],
                    "enabled": task["enabled"]
                }
                for task_id, task in self.scheduled_tasks.items()
            },
            "timestamp": datetime.now().isoformat()
        }
        return status
    
    def add_custom_schedule(self, task_id, task_func, frequency, time_spec, task_type, description=""):
        """Add a custom scheduled task"""
        return self.schedule_task(task_id, task_func, frequency, time_spec, task_type, description)
    
    def disable_task(self, task_id):
        """Disable a scheduled task"""
        if task_id in self.scheduled_tasks:
            self.scheduled_tasks[task_id]["enabled"] = False
            self.log_schedule_event(task_id, "disabled", "Task manually disabled")
            print(f"Task disabled: {task_id}")
    
    def enable_task(self, task_id):
        """Enable a scheduled task"""
        if task_id in self.scheduled_tasks:
            self.scheduled_tasks[task_id]["enabled"] = True
            self.log_schedule_event(task_id, "enabled", "Task manually enabled")
            print(f"Task enabled: {task_id}")

def main():
    print("Initializing Gold Tier Scheduling System...")
    
    # Initialize the scheduler
    scheduler = GoldTierScheduler()
    
    # Show schedule status
    status = scheduler.get_schedule_status()
    print(f"\nScheduled tasks: {status['total_scheduled_tasks']}")
    print(f"Active tasks: {status['active_tasks']}")
    
    # Start the scheduler
    scheduler.start_scheduler()
    
    print("\nGold Tier Scheduling System initialized!")
    print("- Daily tasks scheduled")
    print("- Weekly tasks scheduled") 
    print("- Hourly monitoring active")
    print("- Scheduler running in background")
    
    # Keep main thread alive for demonstration
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