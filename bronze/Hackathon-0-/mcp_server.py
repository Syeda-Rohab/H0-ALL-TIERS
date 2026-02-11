"""
MCP Server for Silver Tier AI Assistant
Handles email sending and approval notifications
"""

from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import time
import json
from datetime import datetime
import os

app = Flask(__name__)

class MCPServer:
    def __init__(self):
        # Load configuration from environment or config file
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.sender_email = os.getenv('SENDER_EMAIL', 'your-email@gmail.com')
        self.sender_password = os.getenv('SENDER_PASSWORD', 'your-app-password')
        
        self.approval_requests = {}
        self.notifications = []
        
    def send_email(self, recipient, subject, body, html_body=None):
        """Send an email using SMTP"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Add body to email
            if html_body:
                msg.attach(MIMEText(html_body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            # Create SMTP session
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable security
            server.login(self.sender_email, self.sender_password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.sender_email, recipient, text)
            server.quit()
            
            print(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False
    
    def send_approval_request(self, recipient, action_id, action_details):
        """Send approval request to human operator"""
        subject = f"Action Approval Required - ID: {action_id}"
        body = f"""
Action Approval Required

Action ID: {action_id}
Request Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Details: {action_details}

Please review the action and respond with either:
- APPROVE {action_id} to approve
- REJECT {action_id} to reject

This action requires your approval before proceeding.
"""
        
        success = self.send_email(recipient, subject, body)
        if success:
            self.approval_requests[action_id] = {
                'action_details': action_details,
                'request_time': datetime.now().isoformat(),
                'status': 'pending'
            }
            print(f"Approval request sent for action {action_id}")
        
        return success
    
    def process_approval_response(self, action_id, decision):
        """Process approval response from human operator"""
        if action_id in self.approval_requests:
            self.approval_requests[action_id]['status'] = decision
            self.approval_requests[action_id]['response_time'] = datetime.now().isoformat()
            print(f"Approval response processed for action {action_id}: {decision}")
            return True
        return False

# Global MCP Server instance
mcp_server = MCPServer()

@app.route('/send-email', methods=['POST'])
def handle_send_email():
    """API endpoint to send emails"""
    data = request.json
    
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    html_body = data.get('html_body')
    
    if not recipient or not subject or not body:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success = mcp_server.send_email(recipient, subject, body, html_body)
    
    if success:
        return jsonify({'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send email'}), 500

@app.route('/request-approval', methods=['POST'])
def handle_request_approval():
    """API endpoint to request human approval"""
    data = request.json
    
    recipient = data.get('recipient')
    action_id = data.get('action_id')
    action_details = data.get('action_details')
    
    if not recipient or not action_id or not action_details:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success = mcp_server.send_approval_request(recipient, action_id, action_details)
    
    if success:
        return jsonify({'message': f'Approval request sent for action {action_id}'}), 200
    else:
        return jsonify({'error': 'Failed to send approval request'}), 500

@app.route('/process-approval', methods=['POST'])
def handle_process_approval():
    """API endpoint to process approval responses"""
    data = request.json
    
    action_id = data.get('action_id')
    decision = data.get('decision')  # 'approve' or 'reject'
    
    if not action_id or not decision:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success = mcp_server.process_approval_response(action_id, decision)
    
    if success:
        return jsonify({'message': f'Approval response processed for action {action_id}'}), 200
    else:
        return jsonify({'error': 'Failed to process approval response'}), 500

@app.route('/status', methods=['GET'])
def get_status():
    """API endpoint to get server status"""
    return jsonify({
        'status': 'running',
        'approval_requests': len(mcp_server.approval_requests),
        'notifications_sent': len(mcp_server.notifications),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/approvals', methods=['GET'])
def get_approvals():
    """API endpoint to get all approval requests"""
    return jsonify(mcp_server.approval_requests)

def run_server():
    """Run the MCP server in a separate thread"""
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def start_mcp_server():
    """Start the MCP server in a background thread"""
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    print("MCP Server started on port 5000")
    return server_thread

if __name__ == '__main__':
    print("Starting MCP Server...")
    print("Server will listen on port 5000")
    print("API endpoints:")
    print("  POST /send-email - Send an email")
    print("  POST /request-approval - Request human approval")
    print("  POST /process-approval - Process approval response")
    print("  GET  /status - Get server status")
    print("  GET  /approvals - Get approval requests")
    
    # Start the server
    run_server()