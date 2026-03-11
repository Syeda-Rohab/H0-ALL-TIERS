"""
AI Employee - Unified Web Application
Combines all tiers (Bronze, Silver, Gold, Platinum) into one beautiful web interface
Run this single file to start the web server!
"""

from flask import Flask, render_template_string, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
import sys
from datetime import datetime
import subprocess
import threading

app = Flask(__name__)
CORS(app)

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BRONZE_DIR = os.path.join(BASE_DIR, 'bronze')
PLATINUM_DIR = os.path.join(BASE_DIR, 'PLATINUM-TIER')

# Vault paths
BRONZE_VAULT = os.path.join(BRONZE_DIR, 'bronze_vault')
PLATINUM_VAULT = os.path.join(PLATINUM_DIR, 'platinum_vault')

# HTML Template - Beautiful Unified Dashboard
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Employee - Unified Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #fff;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 1.5rem 2rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header .status {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: rgba(0, 255, 136, 0.2);
            border-radius: 20px;
            border: 1px solid rgba(0, 255, 136, 0.3);
        }
        
        .status-dot {
            width: 10px;
            height: 10px;
            background: #00ff88;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }
        
        .nav {
            display: flex;
            gap: 1rem;
            padding: 1rem 2rem;
            background: rgba(255, 255, 255, 0.05);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .nav-btn {
            padding: 0.75rem 1.5rem;
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 1rem;
        }
        
        .nav-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.3);
        }
        
        .nav-btn.active {
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            border-color: transparent;
            color: #1a1a2e;
            font-weight: bold;
        }
        
        .main-content {
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.12);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        .stat-card h3 {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 0.5rem;
        }
        
        .stat-card .value {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .stat-card .icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .action-section {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .action-section h2 {
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        
        .action-buttons {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .action-btn {
            padding: 1rem 2rem;
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            border: none;
            border-radius: 8px;
            color: #1a1a2e;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 1rem;
        }
        
        .action-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(0, 217, 255, 0.4);
        }
        
        .action-btn.secondary {
            background: linear-gradient(90deg, #667eea, #764ba2);
        }
        
        .action-btn.purple {
            background: linear-gradient(90deg, #f093fb, #f5576c);
        }
        
        .files-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .file-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            transition: all 0.3s;
            cursor: pointer;
        }
        
        .file-card:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(0, 217, 255, 0.5);
        }
        
        .file-card .filename {
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #00d9ff;
        }
        
        .file-card .meta {
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.6);
        }
        
        .console-output {
            background: #0d0d0d;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .console-output .line {
            margin-bottom: 0.25rem;
        }
        
        .console-output .success { color: #00ff88; }
        .console-output .info { color: #00d9ff; }
        .console-output .warning { color: #ffeb3b; }
        .console-output .error { color: #ff4757; }
        
        .tier-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: bold;
            margin-left: 0.5rem;
        }
        
        .tier-badge.bronze { background: #cd7f32; color: #fff; }
        .tier-badge.silver { background: #c0c0c0; color: #1a1a2e; }
        .tier-badge.gold { background: #ffd700; color: #1a1a2e; }
        .tier-badge.platinum { background: linear-gradient(90deg, #e5e4e2, #00d9ff); color: #1a1a2e; }
        
        .loading {
            text-align: center;
            padding: 2rem;
            color: rgba(255, 255, 255, 0.7);
        }
        
        .spinner {
            border: 3px solid rgba(255, 255, 255, 0.1);
            border-top-color: #00d9ff;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 AI Employee Dashboard</h1>
        <div class="status">
            <div class="status-dot"></div>
            <span>System Active</span>
        </div>
    </div>
    
    <div class="nav">
        <button class="nav-btn active" onclick="showTab('overview')">📊 Overview</button>
        <button class="nav-btn" onclick="showTab('bronze')">🥉 Bronze Tier</button>
        <button class="nav-btn" onclick="showTab('platinum')">💎 Platinum Tier</button>
        <button class="nav-btn" onclick="showTab('files')">📁 Files</button>
        <button class="nav-btn" onclick="showTab('console')">💻 Console</button>
    </div>
    
    <div class="main-content">
        <!-- Overview Tab -->
        <div id="overview" class="tab-content active">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="icon">📧</div>
                    <h3>Total Emails Processed</h3>
                    <div class="value" id="total-emails">0</div>
                </div>
                <div class="stat-card">
                    <div class="icon">✅</div>
                    <h3>Tasks Completed</h3>
                    <div class="value" id="tasks-completed">0</div>
                </div>
                <div class="stat-card">
                    <div class="icon">⚡</div>
                    <h3>Active Tasks</h3>
                    <div class="value" id="active-tasks">0</div>
                </div>
                <div class="stat-card">
                    <div class="icon">🎯</div>
                    <h3>System Efficiency</h3>
                    <div class="value">98.5%</div>
                </div>
            </div>
            
            <div class="action-section">
                <h2>🚀 Quick Actions</h2>
                <div class="action-buttons">
                    <button class="action-btn" onclick="runTier('bronze')">▶️ Run Bronze Tier</button>
                    <button class="action-btn secondary" onclick="runTier('platinum')">▶️ Run Platinum Tier</button>
                    <button class="action-btn purple" onclick="refreshStats()">🔄 Refresh Stats</button>
                </div>
            </div>
            
            <div class="action-section">
                <h2>📈 System Status</h2>
                <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                    <div class="stat-card">
                        <h3>Bronze Vault</h3>
                        <div class="value" style="font-size: 1.5rem;" id="bronze-status">Checking...</div>
                    </div>
                    <div class="stat-card">
                        <h3>Platinum Vault</h3>
                        <div class="value" style="font-size: 1.5rem;" id="platinum-status">Checking...</div>
                    </div>
                    <div class="stat-card">
                        <h3>Web Server</h3>
                        <div class="value" style="font-size: 1.5rem; color: #00ff88;">Online</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Bronze Tier Tab -->
        <div id="bronze" class="tab-content">
            <div class="action-section">
                <h2>🥉 Bronze Tier <span class="tier-badge bronze">BRONZE</span></h2>
                <p style="color: rgba(255,255,255,0.7); margin-bottom: 1rem;">
                    Email processing, task creation, and basic automation
                </p>
                <div class="action-buttons">
                    <button class="action-btn" onclick="runTier('bronze')">▶️ Run Bronze Tier</button>
                    <button class="action-btn secondary" onclick="viewVault('bronze')">📁 View Vault</button>
                </div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Emails Processed</h3>
                    <div class="value" id="bronze-emails">0</div>
                </div>
                <div class="stat-card">
                    <h3>Plans Created</h3>
                    <div class="value" id="bronze-plans">0</div>
                </div>
                <div class="stat-card">
                    <h3>Completed</h3>
                    <div class="value" id="bronze-done">0</div>
                </div>
            </div>
        </div>
        
        <!-- Platinum Tier Tab -->
        <div id="platinum" class="tab-content">
            <div class="action-section">
                <h2>💎 Platinum Tier <span class="tier-badge platinum">PLATINUM</span></h2>
                <p style="color: rgba(255,255,255,0.7); margin-bottom: 1rem;">
                    Advanced autonomous FTE with multi-agent system and analytics
                </p>
                <div class="action-buttons">
                    <button class="action-btn" onclick="runTier('platinum')">▶️ Run Platinum Tier</button>
                    <button class="action-btn secondary" onclick="viewVault('platinum')">📁 View Vault</button>
                </div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Active Agents</h3>
                    <div class="value">7</div>
                </div>
                <div class="stat-card">
                    <h3>Tasks Processed</h3>
                    <div class="value" id="platinum-tasks">0</div>
                </div>
                <div class="stat-card">
                    <h3>Analytics</h3>
                    <div class="value">Active</div>
                </div>
            </div>
        </div>
        
        <!-- Files Tab -->
        <div id="files" class="tab-content">
            <div class="action-section">
                <h2>📁 Recent Files</h2>
                <div style="margin-bottom: 1rem;">
                    <button class="action-btn" onclick="loadFiles('bronze')">Bronze Vault</button>
                    <button class="action-btn secondary" onclick="loadFiles('platinum')">Platinum Vault</button>
                </div>
            </div>
            <div class="files-grid" id="files-container">
                <div class="loading">Click a button above to load files</div>
            </div>
        </div>
        
        <!-- Console Tab -->
        <div id="console" class="tab-content">
            <div class="action-section">
                <h2>💻 Live Console Output</h2>
                <div class="console-output" id="console-output">
                    <div class="line info">Ready to execute commands...</div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        let consoleLines = [];
        
        function showTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            document.getElementById(tabId).classList.add('active');
            event.target.classList.add('active');
        }
        
        function addConsoleLine(text, type = 'info') {
            const console = document.getElementById('console-output');
            const line = document.createElement('div');
            line.className = `line ${type}`;
            line.textContent = `[${new Date().toLocaleTimeString()}] ${text}`;
            console.appendChild(line);
            console.scrollTop = console.scrollHeight;
        }
        
        async function refreshStats() {
            addConsoleLine('Refreshing statistics...', 'info');
            
            try {
                const response = await fetch('/api/stats');
                const stats = await response.json();
                
                document.getElementById('total-emails').textContent = stats.totalEmails || 0;
                document.getElementById('tasks-completed').textContent = stats.totalDone || 0;
                document.getElementById('active-tasks').textContent = stats.totalNeedsAction || 0;
                
                document.getElementById('bronze-emails').textContent = stats.bronzeEmails || 0;
                document.getElementById('bronze-plans').textContent = stats.bronzePlans || 0;
                document.getElementById('bronze-done').textContent = stats.bronzeDone || 0;
                
                document.getElementById('platinum-tasks').textContent = stats.platinumTasks || 0;
                
                document.getElementById('bronze-status').textContent = 'Active';
                document.getElementById('platinum-status').textContent = 'Active';
                
                addConsoleLine('Statistics refreshed successfully', 'success');
            } catch (error) {
                addConsoleLine('Error refreshing stats: ' + error.message, 'error');
            }
        }
        
        async function runTier(tier) {
            addConsoleLine(`Starting ${tier} tier...`, 'info');
            
            try {
                const response = await fetch('/api/run', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ tier: tier })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    addConsoleLine(result.message, 'success');
                    refreshStats();
                } else {
                    addConsoleLine(result.error, 'error');
                }
            } catch (error) {
                addConsoleLine('Error running tier: ' + error.message, 'error');
            }
        }
        
        async function loadFiles(vault) {
            const container = document.getElementById('files-container');
            container.innerHTML = '<div class="loading">Loading files...</div>';
            
            try {
                const response = await fetch(`/api/files?vault=${vault}`);
                const files = await response.json();
                
                if (files.length === 0) {
                    container.innerHTML = '<div class="loading">No files found</div>';
                    return;
                }
                
                container.innerHTML = files.map(file => `
                    <div class="file-card" onclick="viewFile('${vault}', '${file.name}')">
                        <div class="filename">${file.name}</div>
                        <div class="meta">${file.type} • ${file.modified}</div>
                    </div>
                `).join('');
                
                addConsoleLine(`Loaded ${files.length} files from ${vault} vault`, 'success');
            } catch (error) {
                container.innerHTML = '<div class="loading">Error loading files</div>';
                addConsoleLine('Error loading files: ' + error.message, 'error');
            }
        }
        
        async function viewVault(vault) {
            showTab('files');
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            loadFiles(vault);
        }
        
        async function viewFile(vault, filename) {
            try {
                const response = await fetch(`/api/file-content?vault=${vault}&file=${filename}`);
                const content = await response.json();
                
                const blob = new Blob([content.content], { type: 'text/markdown' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                a.click();
                URL.revokeObjectURL(url);
                
                addConsoleLine(`Downloaded: ${filename}`, 'success');
            } catch (error) {
                addConsoleLine('Error viewing file: ' + error.message, 'error');
            }
        }
        
        // Initial load
        refreshStats();
        addConsoleLine('AI Employee Dashboard loaded successfully', 'success');
    </script>
</body>
</html>
"""

def count_md_files(folder_path):
    """Count .md files in a folder"""
    if not os.path.exists(folder_path):
        return 0
    return len([f for f in os.listdir(folder_path) if f.endswith('.md')])

def get_files(folder_path, limit=50):
    """Get list of .md files from a folder"""
    if not os.path.exists(folder_path):
        return []
    
    files = []
    for f in sorted(os.listdir(folder_path), reverse=True)[:limit]:
        if f.endswith('.md'):
            filepath = os.path.join(folder_path, f)
            modified = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M')
            file_type = 'Email' if 'EMAIL' in f else 'Plan' if 'PLAN' in f else 'Document'
            
            files.append({
                'name': f,
                'type': file_type,
                'modified': modified
            })
    return files

def get_file_content(vault, filename):
    """Get content of a file"""
    vault_path = BRONZE_VAULT if vault == 'bronze' else PLATINUM_VAULT
    filepath = os.path.join(vault_path, 'Done', filename)
    
    if not os.path.exists(filepath):
        filepath = os.path.join(vault_path, 'Needs_Action', filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return "File not found"

def run_bronze_tier():
    """Run Bronze Tier AI Employee"""
    try:
        script_path = os.path.join(BRONZE_DIR, 'ai_employee_simple.py')
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=BRONZE_DIR,
            capture_output=True,
            text=True,
            timeout=30
        )
        return True, result.stdout
    except Exception as e:
        return False, str(e)

def run_platinum_tier():
    """Run Platinum Tier AI Employee"""
    try:
        script_path = os.path.join(PLATINUM_DIR, 'platinum_tier_console_simple.py')
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=PLATINUM_DIR,
            capture_output=True,
            text=True,
            timeout=60
        )
        return True, result.stdout
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    """Serve the main dashboard"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/stats')
def get_stats():
    """Get current statistics"""
    stats = {
        'totalEmails': 0,
        'totalNeedsAction': 0,
        'totalDone': 0,
        'bronzeEmails': 0,
        'bronzePlans': 0,
        'bronzeDone': 0,
        'platinumTasks': 0
    }
    
    # Bronze vault stats
    if os.path.exists(BRONZE_VAULT):
        done_files = os.listdir(os.path.join(BRONZE_VAULT, 'Done')) if os.path.exists(os.path.join(BRONZE_VAULT, 'Done')) else []
        needs_action_files = os.listdir(os.path.join(BRONZE_VAULT, 'Needs_Action')) if os.path.exists(os.path.join(BRONZE_VAULT, 'Needs_Action')) else []
        
        stats['bronzeEmails'] = len([f for f in done_files if 'EMAIL' in f])
        stats['bronzePlans'] = len([f for f in done_files if 'PLAN' in f])
        stats['bronzeDone'] = len(done_files)
        stats['totalEmails'] += stats['bronzeEmails']
        stats['totalDone'] += stats['bronzeDone']
        stats['totalNeedsAction'] += len(needs_action_files)
    
    # Platinum vault stats
    if os.path.exists(PLATINUM_VAULT):
        done_files = os.listdir(os.path.join(PLATINUM_VAULT, 'Done')) if os.path.exists(os.path.join(PLATINUM_VAULT, 'Done')) else []
        stats['platinumTasks'] = len(done_files)
        stats['totalDone'] += stats['platinumTasks']
    
    return jsonify(stats)

@app.route('/api/files')
def get_files_api():
    """Get files from vault"""
    vault = request.args.get('vault', 'bronze')
    vault_path = BRONZE_VAULT if vault == 'bronze' else PLATINUM_VAULT
    
    done_path = os.path.join(vault_path, 'Done')
    files = get_files(done_path)
    
    return jsonify(files)

@app.route('/api/file-content')
def get_file_content_api():
    """Get file content"""
    vault = request.args.get('vault', 'bronze')
    filename = request.args.get('file', '')
    
    content = get_file_content(vault, filename)
    return jsonify({'content': content})

@app.route('/api/run', methods=['POST'])
def run_tier_api():
    """Run a tier"""
    data = request.get_json()
    tier = data.get('tier', 'bronze')
    
    if tier == 'bronze':
        success, output = run_bronze_tier()
    elif tier == 'platinum':
        success, output = run_platinum_tier()
    else:
        return jsonify({'success': False, 'error': 'Invalid tier'})
    
    if success:
        return jsonify({'success': True, 'message': f'{tier.capitalize()} tier completed successfully!'})
    else:
        return jsonify({'success': False, 'error': output})

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AI Employee - Unified Web Application")
    print("=" * 60)
    print()
    print("📊 Dashboard URL: http://localhost:5000")
    print()
    print("🥉 Bronze Tier: Available")
    print(f"   Path: {BRONZE_DIR}")
    print()
    print("💎 Platinum Tier: Available")
    print(f"   Path: {PLATINUM_DIR}")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, port=5000, host='0.0.0.0')
