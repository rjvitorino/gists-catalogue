import pstats

def analyse_profiling_results():
    """Analyses and prints profiling results from a 'restats' file."""
    profile = pstats.Stats('tests/restats')
    profile.strip_dirs().sort_stats('cumtime').print_stats(20)

if __name__ == '__main__':
    analyse_profiling_results()