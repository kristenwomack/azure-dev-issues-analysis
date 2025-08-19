#!/usr/bin/env python3
"""
Unit tests for hello_test.py
Validates the hello world functionality
"""

import unittest
import sys
import os
import json

# Add the tools directory to the path to import hello_test
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from hello_test import hello_world, basic_system_check
except ImportError as e:
    print(f"Error importing hello_test: {e}")
    sys.exit(1)

class TestHelloFunctionality(unittest.TestCase):
    """Test cases for hello world functionality"""
    
    def test_hello_world_output(self):
        """Test that hello_world returns the expected string"""
        result = hello_world()
        self.assertEqual(result, "hello : hello")
        self.assertIsInstance(result, str)
    
    def test_basic_system_check(self):
        """Test that basic_system_check returns valid data"""
        result = basic_system_check()
        
        # Check required keys are present
        required_keys = ["python_version", "timestamp", "system_status", "message"]
        for key in required_keys:
            self.assertIn(key, result)
        
        # Check the message is correct
        self.assertEqual(result["message"], "hello : hello")
        
        # Check system status
        self.assertEqual(result["system_status"], "operational")
        
        # Check python version format
        self.assertTrue(result["python_version"].count(".") >= 2)
    
    def test_json_serializable(self):
        """Test that system check results are JSON serializable"""
        result = basic_system_check()
        try:
            json.dumps(result)
        except (TypeError, ValueError):
            self.fail("System check results are not JSON serializable")

class TestHelloIntegration(unittest.TestCase):
    """Integration tests for hello functionality"""
    
    def test_hello_test_file_execution(self):
        """Test that hello_test.py can be executed successfully"""
        import subprocess
        
        script_path = os.path.join(os.path.dirname(__file__), "hello_test.py")
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0, 
                        f"hello_test.py failed with: {result.stderr}")
        self.assertIn("hello : hello", result.stdout)
        self.assertIn("SUCCESS", result.stdout)

def run_tests():
    """Run all tests and return the result"""
    print("🧪 Running hello world tests...")
    print("=" * 50)
    
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(unittest.makeSuite(TestHelloFunctionality))
    suite.addTest(unittest.makeSuite(TestHelloIntegration))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("🎉 All tests passed!")
        return True
    else:
        print(f"❌ {len(result.failures)} test(s) failed, {len(result.errors)} error(s)")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)