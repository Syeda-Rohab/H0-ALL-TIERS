"""
AI Employee Backend API Server
This server connects the UI with your existing Python AI Employee functionality
Run this alongside the Next.js frontend
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import sys
from datetime import datetime

# Add parent directory to path to import ai_employee
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'bronze'))

app = Flask(__name__)
CORS(app)

# Define vault paths
BASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'bronze', 'bronze_vault')
PLATINUM_VAULT_PATH = os.path.join(os.path.dirname(__file__), '..', 'PLATINUM-TIER', 'platinum_vault')

def count_md_files(folder_path):
    """Count .md files in a folder"""
    if not os.path.exists(folder_path):
        return 0
    return len([f for f in os.listdir(folder_path) if f.endswith('.md')])

def get_files_from_folder(folder_path, limit=20):
    """Get list of .md files from a folder"""
    if not os.path.exists(folder_path):
        return []
    
    files = []
    for f in os.listdir(folder_path)[:limit]:
        if f.endswith('.md'):
            filepath = os.path.join(folder_path, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    files.append({
                        'filename': f,
                        'content': content[:500],  # First 500 chars
                        'created': datetime.fromtimestamp(os.path.getctime(filepath)).isoformat()
                    })
            except Exception as e:
                files.append({
                    'filename': f,
                    'content': f'Error reading file: {str(e)}',
                    'created': datetime.fromtimestamp(os.path.getctime(filepath)).isoformat()
                })
    return files

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get current statistics from vault"""
    stats = {
        'inbox': 0,
        'needsAction': 0,
        'pendingApproval': 0,
        'done': 0,
        'totalProcessed': 0
    }
    
    for vault_path in [BASE_PATH, PLATINUM_VAULT_PATH]:
        if os.path.exists(vault_path):
            stats['inbox'] += count_md_files(os.path.join(vault_path, 'Inbox'))
            stats['needsAction'] += count_md_files(os.path.join(vault_path, 'Needs_Action'))
            stats['pendingApproval'] += count_md_files(os.path.join(vault_path, 'Pending_Approval'))
            stats['done'] += count_md_files(os.path.join(vault_path, 'Done'))
    
    stats['totalProcessed'] = stats['done']
    
    return jsonify(stats)

@app.route('/api/emails', methods=['GET'])
def get_emails():
    """Get emails from Needs_Action folder"""
    emails = []
    
    for vault_path in [BASE_PATH, PLATINUM_VAULT_PATH]:
        needs_action_path = os.path.join(vault_path, 'Needs_Action')
        if os.path.exists(needs_action_path):
            files = get_files_from_folder(needs_action_path)
            for file in files:
                if 'EMAIL' in file['filename']:
                    # Parse email content
                    content = file['content']
                    subject = 'Unknown'
                    sender = 'Unknown'
                    
                    for line in content.split('\n'):
                        if line.startswith('# Email Note:'):
                            subject = line.replace('# Email Note:', '').strip()
                        elif line.startswith('## Sender'):
                            sender = content.split('## Sender')[1].split('\n')[1].strip()
                    
                    emails.append({
                        'id': file['filename'],
                        'subject': subject,
                        'sender': sender,
                        'timestamp': file['created'],
                        'status': 'processing'
                    })
    
    return jsonify(emails if emails else [])

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get tasks from Needs_Action folder"""
    tasks = []
    
    for vault_path in [BASE_PATH, PLATINUM_VAULT_PATH]:
        needs_action_path = os.path.join(vault_path, 'Needs_Action')
        if os.path.exists(needs_action_path):
            files = get_files_from_folder(needs_action_path)
            for file in files:
                if 'PLAN' in file['filename']:
                    content = file['content']
                    title = content.split('\n')[0].replace('# Action Plan:', '').strip()
                    
                    tasks.append({
                        'id': file['filename'],
                        'title': title,
                        'priority': 'medium',
                        'status': 'in_progress',
                        'dueDate': datetime.now().strftime('%Y-%m-%d'),
                        'source': 'Auto-generated from email'
                    })
    
    return jsonify(tasks if tasks else [])

@app.route('/api/activity', methods=['GET'])
def get_activity():
    """Get recent activity from Done folder"""
    activities = []
    
    for vault_path in [BASE_PATH, PLATINUM_VAULT_PATH]:
        done_path = os.path.join(vault_path, 'Done')
        if os.path.exists(done_path):
            files = get_files_from_folder(done_path, limit=10)
            for file in files:
                activity_type = 'task' if 'PLAN' in file['filename'] else 'email'
                activities.append({
                    'id': file['filename'],
                    'type': activity_type,
                    'action': 'Processed' if 'PLAN' in file['filename'] else 'Email Processed',
                    'timestamp': file['created'],
                    'details': f"File: {file['filename']}"
                })
    
    # Sort by timestamp
    activities.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return jsonify(activities if activities else [])

@app.route('/api/process', methods=['POST'])
def process_emails():
    """Trigger email processing"""
    try:
        # Import and run the AI employee cycle
        from bronze.ai_employee import AIEmployee
        
        ai = AIEmployee()
        ai.setup_directories()
        
        if ai.authenticate():
            ai.run_cycle()
            return jsonify({'success': True, 'message': 'Email processing completed'})
        else:
            return jsonify({'success': False, 'message': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'vault_exists': os.path.exists(BASE_PATH)
    })

if __name__ == '__main__':
    print("🚀 AI Employee Backend Server starting...")
    print(f"📁 Base Vault Path: {BASE_PATH}")
    print(f"📁 Platinum Vault Path: {PLATINUM_VAULT_PATH}")
    app.run(debug=True, port=5001, host='0.0.0.0')
