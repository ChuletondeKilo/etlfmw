from os import path, chdir
from pathlib import Path

# Get the absolute path to the directory containing main.py
script_dir = Path(path.dirname(path.abspath(__file__)))
# Change the working directory to that directory
chdir(script_dir)

cwd = Path.cwd()