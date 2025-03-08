import os
from pathlib import Path

if __name__ == '__main__':
    
    # Get the absolute path to the directory containing main.py
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    # Change the working directory to that directory
    os.chdir(script_dir)
