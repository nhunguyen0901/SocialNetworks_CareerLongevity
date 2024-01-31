# parallel_functions.py

from network_analysis_functions import calculate_social_capital

def calculate_social_capital_wrapper(year, edges_by_year):
    return calculate_social_capital(year, edges_by_year)
