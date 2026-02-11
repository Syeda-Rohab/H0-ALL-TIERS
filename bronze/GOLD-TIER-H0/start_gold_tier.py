#!/usr/bin/env python3
"""
Gold Tier AI Team - Production Startup Script
Use this script to run the system with proper service management
"""

from gold_tier_orchestrator import GoldTierOrchestrator
import signal
import sys
import time

def signal_handler(sig, frame):
    print('\nShutting down Gold Tier system...')
    if 'orchestrator' in globals():
        orchestrator.shutdown()
    print('Gold Tier system stopped.')
    sys.exit(0)

if __name__ == "__main__":
    print("Starting Gold Tier AI Team in production mode...")
    print("MCP Server will be available at http://127.0.0.1:5001")
    print("Press Ctrl+C to stop the system\n")
    
    # Initialize and start the orchestrator
    orchestrator = GoldTierOrchestrator()
    orchestrator.start_all_services()
    
    # Run one orchestration cycle to demonstrate functionality
    orchestrator.run_full_orchestration_cycle()
    
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    print("\nGold Tier system is running!")
    print("- MCP Server: http://127.0.0.1:5001/status")
    print("- Dashboard files are being generated in gold_vault/")
    print("- All services are operational")
    print("\nWaiting for tasks... (Press Ctrl+C to stop)")
    
    # Keep the system running
    try:
        while True:
            time.sleep(10)  # Sleep in small chunks to remain responsive to Ctrl+C
    except KeyboardInterrupt:
        signal_handler(None, None)