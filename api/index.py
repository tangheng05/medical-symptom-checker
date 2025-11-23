"""
Vercel Serverless Function Handler for Medical Symptom Checker
"""
import os
import sys
import logging
from pathlib import Path

# Set Vercel environment variable FIRST
os.environ['VERCEL'] = '1'

# Configure logging for Vercel with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger(__name__)

# Log Python environment info
logger.info(f"Python version: {sys.version}")
logger.info(f"Python executable: {sys.executable}")
logger.info(f"Current working directory: {os.getcwd()}")

try:
    # Add the parent directory to the path so we can import our modules
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    
    # Insert parent directory at the beginning of the path
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))

    logger.info(f"Current dir: {current_dir}")
    logger.info(f"Parent dir: {parent_dir}")
    logger.info(f"sys.path: {sys.path}")
    
    # Check what files exist
    try:
        logger.info(f"Files in parent: {list(parent_dir.iterdir())}")
        data_dir = parent_dir / 'data'
        if data_dir.exists():
            logger.info(f"Data directory exists: {data_dir}")
            logger.info(f"Files in data: {list(data_dir.iterdir())}")
        else:
            logger.error(f"Data directory NOT found at: {data_dir}")
    except Exception as e:
        logger.error(f"Error listing files: {e}")

    # Import the Flask app from the parent directory
    logger.info("Attempting to import Flask app...")
    from app import app as flask_app
    logger.info("Flask app imported successfully")
    logger.info(f"App config FLASK_ENV: {flask_app.config.get('FLASK_ENV')}")

except Exception as e:
    logger.error(f"CRITICAL ERROR during import: {e}", exc_info=True)
    logger.error(f"Error type: {type(e).__name__}")
    logger.error(f"Error args: {e.args}")
    
    # Create a minimal error app that shows the actual error
    from flask import Flask, jsonify
    flask_app = Flask(__name__)
    
    error_details = {
        'error': 'Application failed to initialize',
        'error_type': type(e).__name__,
        'error_message': str(e),
        'python_version': sys.version,
        'cwd': os.getcwd(),
        'sys_path': sys.path[:5],  # First 5 entries
    }
    
    @flask_app.route('/')
    @flask_app.route('/<path:path>')
    def error_handler(path=''):
        logger.error(f"Error handler called for path: {path}")
        return jsonify(error_details), 500

# This is the WSGI application entry point for Vercel
app = flask_app
logger.info("API module initialization complete")

