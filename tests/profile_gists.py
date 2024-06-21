import cProfile
import pstats
import sys
from pathlib import Path

# cProfile is a built-in Python module for performance profiling. 
# It helps to measure where the program spends most of its time, 
# which functions are called frequently, and how long they take to execute. 
# This is crucial for identifying bottlenecks and optimising the code's performance.

# Adds the repository root to the Python path
repo_root = Path(__file__).parent.parent
sys.path.append(str(repo_root))

from scripts.update_gists import main

def profile():
    """Profiles the main function and saves the results to 'restats'."""
    cProfile.run('main()', 'tests/restats')

if __name__ == '__main__':
    profile()
    p = pstats.Stats('tests/restats')
    p.strip_dirs().sort_stats('cumtime').print_stats(20)