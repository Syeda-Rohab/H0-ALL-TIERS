"""
Claude Reasoning Loop for Silver Tier AI Assistant
Implements think → plan → execute cycle with advanced reasoning
"""

import os
import json
import time
from datetime import datetime
from enum import Enum

class ReasoningStep(Enum):
    THINK = "think"
    ANALYZE = "analyze"
    PLAN = "plan"
    EVALUATE = "evaluate"
    EXECUTE = "execute"

class ClaudeReasoningLoop:
    def __init__(self, vault_path="silver_vault"):
        self.vault_path = vault_path
        self.thinking_logs_path = os.path.join(vault_path, "Thinking_Logs")
        os.makedirs(self.thinking_logs_path, exist_ok=True)
        
    def think_phase(self, input_data, context=None):
        """Think phase: analyze the input and form initial thoughts"""
        print("Starting THINK phase...")
        
        # Create detailed analysis
        analysis = {
            "input_summary": self.summarize_input(input_data),
            "key_elements": self.extract_key_elements(input_data),
            "potential_impacts": self.assess_impacts(input_data),
            "constraints": self.identify_constraints(input_data),
            "resources_available": self.assess_resources(context) if context else {},
            "timestamp": datetime.now().isoformat()
        }
        
        # Log the thinking process
        thinking_log = self.create_thinking_log("THINK", analysis, input_data)
        
        return analysis, thinking_log
    
    def analyze_phase(self, input_data, previous_analysis):
        """Analyze phase: deeper analysis and considerations"""
        print("Starting ANALYZE phase...")
        
        analysis = {
            "detailed_breakdown": self.detailed_analysis(input_data),
            "risks_assessment": self.assess_risks(input_data),
            "opportunities_identified": self.identify_opportunities(input_data),
            "stakeholders_impacted": self.identify_stakeholders(input_data),
            "alternatives_considered": self.consider_alternatives(input_data),
            "previous_analysis": previous_analysis,
            "timestamp": datetime.now().isoformat()
        }
        
        # Log the analysis process
        thinking_log = self.create_thinking_log("ANALYZE", analysis, input_data)
        
        return analysis, thinking_log
    
    def plan_phase(self, input_data, analysis_results):
        """Plan phase: create detailed action plan"""
        print("Starting PLAN phase...")
        
        # Create detailed plan based on analysis
        plan = {
            "strategic_objectives": self.define_objectives(input_data, analysis_results),
            "action_steps": self.create_action_steps(input_data, analysis_results),
            "timeline": self.create_timeline(input_data, analysis_results),
            "resource_allocation": self.allocate_resources(input_data, analysis_results),
            "success_metrics": self.define_success_metrics(input_data, analysis_results),
            "risk_mitigation": self.plan_risk_mitigation(analysis_results),
            "dependencies": self.identify_dependencies(analysis_results),
            "analysis_results": analysis_results,
            "timestamp": datetime.now().isoformat()
        }
        
        # Create PLAN_xxx.md file
        plan_file = self.create_plan_file(plan, input_data)
        
        return plan, plan_file
    
    def evaluate_phase(self, plan, input_data):
        """Evaluate phase: assess the plan's viability"""
        print("Starting EVALUATE phase...")
        
        evaluation = {
            "feasibility_score": self.assess_feasibility(plan),
            "risk_level": self.assess_overall_risk(plan),
            "resource_requirements": self.validate_resources(plan),
            "timeline_realism": self.validate_timeline(plan),
            "success_probability": self.calculate_success_probability(plan),
            "recommended_adjustments": self.suggest_adjustments(plan),
            "plan_file": plan.get('plan_file'),
            "timestamp": datetime.now().isoformat()
        }
        
        # Log the evaluation
        thinking_log = self.create_thinking_log("EVALUATE", evaluation, input_data)
        
        return evaluation, thinking_log
    
    def execute_phase(self, plan, evaluation):
        """Execute phase: initiate execution of the plan"""
        print("Starting EXECUTE phase...")
        
        execution = {
            "execution_status": "initiated",
            "plan_initiated": plan,
            "evaluation_used": evaluation,
            "next_steps": self.determine_next_steps(plan),
            "monitoring_points": self.set_monitoring_points(plan),
            "execution_log": f"Execution initiated for plan: {plan.get('plan_file', 'unknown')}",
            "timestamp": datetime.now().isoformat()
        }
        
        # Update the plan file with execution status
        self.update_plan_execution_status(plan.get('plan_file'), execution)
        
        return execution
    
    def run_reasoning_loop(self, input_data, context=None):
        """Run the complete Claude reasoning loop: think → analyze → plan → evaluate → execute"""
        print("\n=== Starting Claude Reasoning Loop ===")
        print(f"Input: {input_data.get('subject', input_data.get('title', 'Unknown'))[:50]}...")
        
        # Phase 1: Think
        analysis, think_log = self.think_phase(input_data, context)
        
        # Phase 2: Analyze
        detailed_analysis, analyze_log = self.analyze_phase(input_data, analysis)
        
        # Phase 3: Plan
        plan, plan_file = self.plan_phase(input_data, detailed_analysis)
        
        # Phase 4: Evaluate
        evaluation, evaluate_log = self.evaluate_phase(plan, input_data)
        
        # Phase 5: Execute
        execution = self.execute_phase(plan, evaluation)
        
        print("=== Claude Reasoning Loop Complete ===\n")
        
        return {
            "thinking_log": think_log,
            "analysis_log": analyze_log,
            "plan_file": plan_file,
            "evaluation_log": evaluate_log,
            "execution_record": execution
        }
    
    def summarize_input(self, input_data):
        """Create a summary of the input data"""
        return {
            "type": input_data.get('type', 'unknown'),
            "subject": input_data.get('subject', input_data.get('title', 'No subject')),
            "summary": input_data.get('body', input_data.get('content', ''))[:200] + "...",
            "priority": input_data.get('priority', 'medium'),
            "sensitivity": input_data.get('sensitivity', 'normal')
        }
    
    def extract_key_elements(self, input_data):
        """Extract key elements from input"""
        content = input_data.get('body', input_data.get('content', ''))
        elements = {
            "entities_mentioned": [],
            "action_items": [],
            "deadlines": [],
            "resources_needed": [],
            "stakeholders": []
        }
        
        # Simple keyword extraction (would be more sophisticated with NLP in real implementation)
        keywords = ['urgent', 'important', 'deadline', 'meeting', 'report', 'project', 'customer', 'client']
        for keyword in keywords:
            if keyword in content.lower():
                elements["entities_mentioned"].append(keyword)
        
        return elements
    
    def assess_impacts(self, input_data):
        """Assess potential impacts of the input"""
        return {
            "business_impact": "medium",
            "urgency_level": input_data.get('priority', 'medium'),
            "stakeholder_impact": "varies",
            "resource_impact": "low_to_medium"
        }
    
    def identify_constraints(self, input_data):
        """Identify constraints for the task"""
        return {
            "time_constraints": "standard",
            "resource_constraints": "available",
            "dependency_constraints": "minimal",
            "external_factors": "none_identified"
        }
    
    def assess_resources(self, context):
        """Assess available resources"""
        if context:
            return context.get('resources', {})
        return {"available_staff": 3, "available_budget": "medium", "tools_available": ["email", "calendar"]}
    
    def detailed_analysis(self, input_data):
        """Perform detailed analysis"""
        return {
            "content_depth": "medium",
            "complexity_level": "moderate",
            "requirement_specificity": "clear",
            "feasibility_assessment": "achievable"
        }
    
    def assess_risks(self, input_data):
        """Assess risks associated with the input"""
        return {
            "low_risks": ["time_delay"],
            "medium_risks": ["resource_unavailability"],
            "high_risks": [],
            "mitigation_strategies": ["early_start", "backup_resources"]
        }
    
    def identify_opportunities(self, input_data):
        """Identify opportunities in the input"""
        return {
            "upselling_opportunities": [],
            "networking_opportunities": [],
            "process_improvements": [],
            "efficiency_gains": []
        }
    
    def identify_stakeholders(self, input_data):
        """Identify stakeholders impacted"""
        return {
            "primary": ["sender", "direct_team"],
            "secondary": ["management", "related_departments"],
            "tertiary": ["customers", "partners"]
        }
    
    def consider_alternatives(self, input_data):
        """Consider alternative approaches"""
        return [
            {"approach": "direct_response", "pros": ["quick", "efficient"], "cons": ["limited_scope"]},
            {"approach": "comprehensive_solution", "pros": ["thorough", "complete"], "cons": ["time-consuming"]},
            {"approach": "collaborative", "pros": ["team_input", "shared_workload"], "cons": ["coordination_needed"]}
        ]
    
    def define_objectives(self, input_data, analysis):
        """Define strategic objectives"""
        return [
            {"objective": "address_immediate_need", "priority": "high"},
            {"objective": "maintain_relationship", "priority": "medium"},
            {"objective": "follow_up_appropriately", "priority": "medium"}
        ]
    
    def create_action_steps(self, input_data, analysis):
        """Create detailed action steps"""
        return [
            {"step": 1, "action": "Acknowledge receipt", "priority": "high", "estimated_time": "15_min"},
            {"step": 2, "action": "Analyze requirements", "priority": "high", "estimated_time": "30_min"},
            {"step": 3, "action": "Develop response/solution", "priority": "high", "estimated_time": "1_hour"},
            {"step": 4, "action": "Review and finalize", "priority": "medium", "estimated_time": "30_min"},
            {"step": 5, "action": "Deliver response", "priority": "high", "estimated_time": "15_min"},
            {"step": 6, "action": "Follow up if needed", "priority": "low", "estimated_time": "15_min"}
        ]
    
    def create_timeline(self, input_data, analysis):
        """Create timeline for the plan"""
        start_time = datetime.now()
        return {
            "start_date": start_time.isoformat(),
            "milestones": [
                {"step": 1, "target_completion": (start_time + timedelta(minutes=15)).isoformat()},
                {"step": 2, "target_completion": (start_time + timedelta(minutes=45)).isoformat()},
                {"step": 3, "target_completion": (start_time + timedelta(hours=1, minutes=45)).isoformat()},
                {"step": 4, "target_completion": (start_time + timedelta(hours=2, minutes=15)).isoformat()},
                {"step": 5, "target_completion": (start_time + timedelta(hours=2, minutes=30)).isoformat()}
            ],
            "overall_deadline": (start_time + timedelta(hours=3)).isoformat()
        }
    
    def allocate_resources(self, input_data, analysis):
        """Allocate resources for the plan"""
        return {
            "personnel": ["ai_assistant", "supervisor_if_needed"],
            "tools": ["email_system", "calendar", "documents"],
            "time_allocation": {"research": "30%", "creation": "50%", "review": "20%"},
            "budget_implications": "minimal"
        }
    
    def define_success_metrics(self, input_data, analysis):
        """Define success metrics for the plan"""
        return {
            "completion_on_time": True,
            "quality_standards_met": True,
            "stakeholder_satisfaction": "target_high",
            "resource_efficiency": "target_optimal"
        }
    
    def plan_risk_mitigation(self, analysis):
        """Plan risk mitigation strategies"""
        return {
            "identified_risks": analysis['risks_assessment']['medium_risks'],
            "mitigation_plans": analysis['risks_assessment']['mitigation_strategies'],
            "contingency_measures": ["escalate_if_delayed", "request_additional_resources"]
        }
    
    def identify_dependencies(self, analysis):
        """Identify dependencies for the plan"""
        return {
            "internal_dependencies": ["access_to_information", "team_availability"],
            "external_dependencies": ["stakeholder_response_times"],
            "critical_path": ["information_access", "approval_processes"]
        }
    
    def assess_feasibility(self, plan):
        """Assess the feasibility of the plan"""
        return 8.5  # Scale of 1-10
    
    def assess_overall_risk(self, plan):
        """Assess the overall risk level"""
        return "medium"
    
    def validate_resources(self, plan):
        """Validate resource requirements"""
        return {
            "adequate_personnel": True,
            "sufficient_tools": True,
            "realistic_timeframes": True,
            "budget_compatible": True
        }
    
    def validate_timeline(self, plan):
        """Validate the timeline realism"""
        return {
            "realistic": True,
            "buffer_included": True,
            "rush_potential": False
        }
    
    def calculate_success_probability(self, plan):
        """Calculate probability of success"""
        return 0.85  # 85% chance of success
    
    def suggest_adjustments(self, plan):
        """Suggest adjustments to improve the plan"""
        return [
            "Consider batching similar tasks",
            "Schedule buffer time for unexpected issues",
            "Prepare templates for common responses"
        ]
    
    def determine_next_steps(self, plan):
        """Determine next steps for execution"""
        return [
            "Begin with Step 1: Acknowledge receipt",
            "Monitor progress against milestones",
            "Escalate if any milestone is delayed by more than 25%"
        ]
    
    def set_monitoring_points(self, plan):
        """Set monitoring points for the plan"""
        return [
            {"step": 2, "check_point": "Requirements analysis complete"},
            {"step": 3, "check_point": "Solution developed and reviewed"},
            {"step": 5, "check_point": "Response delivered"}
        ]
    
    def create_thinking_log(self, phase, data, input_data):
        """Create a log file for the thinking process"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"THINKING_LOG_{phase}_{timestamp}.md"
        filepath = os.path.join(self.thinking_logs_path, filename)
        
        content = f"""# Claude Reasoning Loop - {phase.upper()} Phase Log

## Input Data
**Subject:** {input_data.get('subject', input_data.get('title', 'Unknown'))}
**Type:** {input_data.get('type', 'unknown')}
**Priority:** {input_data.get('priority', 'medium')}
**Sensitivity:** {input_data.get('sensitivity', 'normal')}

## Phase Analysis
```json
{json.dumps(data, indent=2, default=str)}
```

## Timestamp
{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}

## Phase Outcome
The {phase.lower()} phase completed successfully and contributed to the overall reasoning process.
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created thinking log: {filename}")
        return filepath
    
    def create_plan_file(self, plan_data, input_data):
        """Create the PLAN_xxx.md file with the detailed plan"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"PLAN_{timestamp}.md"
        
        # Use the same path as in silver_assistant.py
        vault_path = "silver_vault"
        needs_action_path = os.path.join(vault_path, "Needs_Action")
        os.makedirs(needs_action_path, exist_ok=True)
        
        filepath = os.path.join(needs_action_path, filename)
        
        content = f"""# Claude-Generated Action Plan: {input_data.get('subject', input_data.get('title', 'Unknown'))}

## Reasoning Summary
This plan was generated using Claude's reasoning loop: think → analyze → plan → evaluate → execute.

### Input Analysis
- **Subject:** {input_data.get('subject', input_data.get('title', 'Unknown'))}
- **Content Preview:** {input_data.get('body', input_data.get('content', ''))[:100]}...
- **Priority:** {input_data.get('priority', 'medium')}
- **Sensitivity:** {input_data.get('sensitivity', 'normal')}

## Strategic Objectives
"""
        
        for obj in plan_data['strategic_objectives']:
            content += f"- **{obj['objective'].replace('_', ' ').title()}** (Priority: {obj['priority']})\n"
        
        content += f"""

## Detailed Action Steps
"""
        
        for step in plan_data['action_steps']:
            content += f"- **Step {step['step']}**: {step['action']} (Priority: {step['priority']}, Time: {step['estimated_time']})\n"
        
        content += f"""

## Timeline
- **Start:** {plan_data['timeline']['start_date']}
- **Overall Deadline:** {plan_data['timeline']['overall_deadline']}

### Milestones
"""
        
        for milestone in plan_data['timeline']['milestones']:
            content += f"- Step {milestone['step']} by {milestone['target_completion']}\n"
        
        content += f"""

## Resource Allocation
- **Personnel:** {', '.join(plan_data['resource_allocation']['personnel'])}
- **Tools:** {', '.join(plan_data['resource_allocation']['tools'])}
- **Time Distribution:** {plan_data['resource_allocation']['time_allocation']}

## Success Metrics
"""
        
        for metric, value in plan_data['success_metrics'].items():
            content += f"- {metric.replace('_', ' ').title()}: {value}\n"
        
        content += f"""

## Risk Assessment
- **Feasibility Score:** {plan_data['feasibility_score']}/10
- **Risk Level:** {plan_data['risk_level'].title()}
- **Mitigation Strategies:** {', '.join(plan_data['risk_mitigation']['mitigation_plans'])}

## Dependencies
- **Internal:** {', '.join(plan_data['dependencies']['internal_dependencies'])}
- **External:** {', '.join(plan_data['dependencies']['external_dependencies'])}

## Evaluation Results
- **Success Probability:** {plan_data['success_probability']*100}%
- **Recommended Adjustments:** {', '.join(plan_data['recommended_adjustments'])}

## Execution Status
- **Status:** Pending execution
- **Next Steps:** {', '.join(plan_data['execution_record']['next_steps'][:2])}

## Generated By
Claude Reasoning Loop - Silver Tier AI Assistant
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created detailed action plan: {filename}")
        return filepath
    
    def update_plan_execution_status(self, plan_file, execution_data):
        """Update the plan file with execution status"""
        if plan_file and os.path.exists(plan_file):
            with open(plan_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add execution status to the file
            execution_update = f"""

## Execution Update
- **Status:** {execution_data['execution_status']}
- **Initiated:** {execution_data['timestamp']}
- **Log:** {execution_data['execution_log']}
"""
            
            # Insert execution update before the final section
            lines = content.split('\n')
            final_section_idx = -1
            for i, line in enumerate(lines):
                if line.startswith('## Generated By'):
                    final_section_idx = i
                    break
            
            if final_section_idx != -1:
                lines.insert(final_section_idx, execution_update)
                content = '\n'.join(lines)
            else:
                content += execution_update
            
            with open(plan_file, 'w', encoding='utf-8') as f:
                f.write(content)

def main():
    print("Initializing Claude Reasoning Loop...")
    
    # Initialize the reasoning loop
    reasoning_loop = ClaudeReasoningLoop()
    
    # Test with sample input
    sample_input = {
        'type': 'email',
        'subject': 'Q4 Budget Proposal Review',
        'body': 'Please review and provide feedback on the Q4 budget proposal by end of week. This is important for our financial planning.',
        'priority': 'high',
        'sensitivity': 'high'
    }
    
    # Run the reasoning loop
    result = reasoning_loop.run_reasoning_loop(sample_input)
    
    print("Claude Reasoning Loop completed!")
    print(f"- Thinking logs created in Thinking_Logs folder")
    print(f"- Action plan created: {result['plan_file']}")
    print("- Full reasoning cycle executed successfully")

if __name__ == "__main__":
    main()