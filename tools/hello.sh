#!/bin/bash

# Hello World Test Script for Azure Developer CLI Issues Analysis
# Simple verification script to demonstrate basic functionality

echo "🚀 Azure Developer CLI Issues Analysis - Hello Test"
echo "============================================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    exit 1
fi

# Change to tools directory
cd "$(dirname "$0")"

echo "📁 Current directory: $(pwd)"

# Run the hello test
echo "🔍 Running hello world test..."
python3 hello_test.py

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Hello test completed successfully!"
    echo "✅ System is ready for Azure Developer CLI issues analysis"
    echo ""
    echo "📋 Next steps:"
    echo "   • Run 'python3 test_auth.py' to test GitHub authentication"
    echo "   • Run 'python3 simple_test.py' to test GitHub API access"
    echo "   • Run 'python3 run_queries.py --help' for full analysis options"
else
    echo ""
    echo "❌ Hello test failed!"
    echo "⚠️  Check the output above for error details"
    exit 1
fi