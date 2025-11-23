"""
Configuration Module
====================

Centralized configuration for the Medical Symptom Checker application.
"""

import os
from pathlib import Path

# Base directory - handle both local and Vercel environments
if os.environ.get('VERCEL'):
    # On Vercel, use absolute path resolution
    BASE_DIR = Path(__file__).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

# Data directory
DATA_DIR = BASE_DIR / 'data'

# JSON file paths
DISEASES_JSON = DATA_DIR / 'diseases.json'
RECOMMENDATIONS_JSON = DATA_DIR / 'recommendations.json'

# Flask configuration
class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False

    # Application settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max request size
    JSON_SORT_KEYS = False

    # Diagnosis settings
    MIN_CONFIDENCE_THRESHOLD = 20  # Minimum confidence to include disease
    MAX_RESULTS = 5  # Maximum number of diagnoses to return

    # Temperature thresholds
    MIN_TEMPERATURE = 35.0
    MAX_TEMPERATURE = 43.0
    NORMAL_TEMP_MIN = 36.1
    NORMAL_TEMP_MAX = 37.2

    # Symptom severity thresholds
    SEVERITY_LOW = 3
    SEVERITY_MEDIUM = 5
    SEVERITY_HIGH = 7

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # Add production-specific settings here

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

