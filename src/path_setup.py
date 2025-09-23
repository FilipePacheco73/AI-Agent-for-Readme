"""
Path setup utility for the AI-Agent-for-Readme project.
This module ensures that the src directory is properly added to the Python path
for relative imports to work correctly across all modules.
"""

import os
import sys


def setup_project_path():
    """
    Add the src directory to the Python path if it's not already present.
    This allows for proper relative imports within the project structure.
    """
    # Get the absolute path to the src directory
    src_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add src directory to Python path if not already present
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)


# Automatically set up the path when this module is imported
setup_project_path()
