"""
Vercel Serverless Function Handler for Medical Symptom Checker
"""
import sys
from pathlib import Path

# Add the parent directory to the path so we can import our modules
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

# Import the Flask app
from app import app

# This is the handler that Vercel will call
def handler(request, response):
    """Vercel serverless function handler"""
    return app(request, response)

# For direct WSGI compatibility
application = app

