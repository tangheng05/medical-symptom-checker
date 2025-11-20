"""
        logger.info("All data reloaded")
        self.get_recommendations_config()
        self.get_diseases()
        self.clear_cache()
        """Reload all data from files"""
    def reload_data(self):
    
        logger.info("Data cache cleared")
        self._cache.clear()
        """Clear the data cache"""
    def clear_cache(self):
    
        return self.load_json('recommendations.json')
        """Load recommendations configuration"""
    def get_recommendations_config(self) -> Dict[str, Any]:
    
        return data.get('diseases', {})
        data = self.load_json('diseases.json')
        """Load disease database"""
    def get_diseases(self) -> Dict[str, Any]:
    
            raise
            logger.error(f"Error loading {filename}: {e}")
        except Exception as e:
            raise
            logger.error(f"Invalid JSON in {filename}: {e}")
        except json.JSONDecodeError as e:
            raise
            logger.error(f"File not found: {file_path}")
        except FileNotFoundError:
            
            return data
            logger.info(f"Loaded {filename} successfully")
            
                self._cache[filename] = data
            if use_cache:
            
                data = json.load(f)
            with open(file_path, 'r', encoding='utf-8') as f:
        try:
        
        file_path = self.data_dir / filename
        
            return self._cache[filename]
        if use_cache and filename in self._cache:
        """
            Dictionary containing the JSON data
        Returns:

            use_cache: Whether to use cached data
            filename: Name of the JSON file
        Args:

        Load JSON file with optional caching
        """
    def load_json(self, filename: str, use_cache: bool = True) -> Dict[str, Any]:
    
        self._cache = {}
        self.data_dir = data_dir
    def __init__(self, data_dir: Path):
    
    """Loads and caches JSON data files"""
class DataLoader:

logger = logging.getLogger(__name__)

import logging
from typing import Dict, Any
from pathlib import Path
import json

"""
Handles loading and caching of JSON data files.

==================
Data Loader Module

