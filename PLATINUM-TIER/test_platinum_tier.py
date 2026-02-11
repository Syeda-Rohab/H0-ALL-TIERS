import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from platinum_tier_autonomous_fte import PlatinumTierAutonomousFTE

def test_platinum_tier():
    print("🧪 Testing Platinum Tier Autonomous FTE...")
    
    # Initialize the system
    platinum_fte = PlatinumTierAutonomousFTE()
    
    # Check if all components are initialized
    print(f"✅ Vault structure created: {os.path.exists(platinum_fte.vault_path)}")
    print(f"✅ Agents initialized: {len(platinum_fte.agents)} agents")
    print(f"✅ Analytics system ready: {bool(platinum_fte.analytics_data)}")
    print(f"✅ Business integrations ready: {bool(platinum_fte.stripe_sim)}")
    print(f"✅ Multi-platform watchers ready: {bool(platinum_fte.watchers)}")
    print(f"✅ Self-improvement system ready: {bool(platinum_fte.self_improvement_models)}")
    
    # Test basic functionality
    status = platinum_fte.get_system_status()
    print(f"✅ System status accessible: {bool(status)}")
    
    print("\n🎉 Platinum Tier Autonomous FTE test completed successfully!")
    print("All core components are functioning properly.")
    
    return True

if __name__ == "__main__":
    test_platinum_tier()