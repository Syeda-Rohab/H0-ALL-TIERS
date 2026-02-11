from advanced_mcp_server import app

print('Starting MCP server on port 5001...')
print('Access at: http://127.0.0.1:5001/status')
print('Press Ctrl+C to stop the server')

# Run the Flask app
app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)