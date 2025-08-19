#!/usr/bin/env python3
"""
Hello World Test for Azure Developer CLI Issues Analysis
Simple verification script that demonstrates basic functionality
"""

import sys
import json
from datetime import datetime

def hello_world():
    """Basic hello world function that returns a greeting"""
    return "hello : hello"

def basic_system_check():
    """Perform basic system checks to verify setup"""
    checks = {
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "timestamp": datetime.now().isoformat(),
        "system_status": "operational",
        "message": hello_world()
    }
    return checks

def test_hello_functionality():
    """Test the hello functionality"""
    print("🚀 Azure Developer CLI Issues Analysis - Hello Test")
    print("=" * 60)
    
    # Test basic hello function
    greeting = hello_world()
    print(f"✅ Hello Test: {greeting}")
    
    # Perform system checks
    print("\n🔍 Running basic system checks...")
    checks = basic_system_check()
    
    print(f"🐍 Python Version: {checks['python_version']}")
    print(f"⏰ Timestamp: {checks['timestamp']}")
    print(f"📊 System Status: {checks['system_status']}")
    print(f"💬 Message: {checks['message']}")
    
    # Verify expected output
    if greeting == "hello : hello":
        print("\n🎉 SUCCESS: Hello test passed!")
        print("✅ System is ready for Azure Developer CLI issues analysis")
        return True
    else:
        print("\n❌ FAILED: Hello test did not return expected output")
        return False

def save_test_results():
    """Save test results to a JSON file"""
    results = basic_system_check()
    results["test_name"] = "hello_test"
    results["test_passed"] = (results["message"] == "hello : hello")
    
    try:
        with open('hello_test_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Test results saved to: hello_test_results.json")
        return True
    except Exception as e:
        print(f"\n⚠️  Could not save test results: {e}")
        return False

def main():
    """Main test function"""
    success = test_hello_functionality()
    save_test_results()
    
    print("\n" + "=" * 60)
    if success:
        print("🎯 All tests completed successfully!")
        print("📋 Next steps: Run 'python simple_test.py' or 'python test_auth.py'")
    else:
        print("⚠️  Some tests failed. Check the output above.")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())