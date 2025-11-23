"""
Vercel Serverless Function Handler for Medical Symptom Checker
"""
import os
import sys
import logging
from pathlib import Path

# Configure logging for Vercel
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set Vercel environment variable
os.environ['VERCEL'] = '1'

try:
    # Add the parent directory to the path so we can import our modules
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    
    # Insert parent directory at the beginning of the path
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))

    logger.info(f"Python version: {sys.version}")
    logger.info(f"Current dir: {current_dir}")
    logger.info(f"Parent dir: {parent_dir}")
    logger.info(f"Files in parent: {list(parent_dir.iterdir())[:10]}")

    # Import the Flask app from the parent directory
    from app import app as flask_app

    logger.info("Flask app imported successfully")
    logger.info(f"App config: {flask_app.config.get('FLASK_ENV')}")

except Exception as e:
    logger.error(f"Failed to import app: {e}", exc_info=True)
    logger.error(f"sys.path: {sys.path}")
    
    # Create a minimal error app
    from flask import Flask, jsonify
    flask_app = Flask(__name__)
    
    @flask_app.route('/')
    @flask_app.route('/<path:path>')
    def error_handler(path=''):
        return jsonify({
            'error': 'Application failed to initialize',
            'details': str(e),
            'path': sys.path
        }), 500

# This is the WSGI application entry point for Vercel
app = flask_app

