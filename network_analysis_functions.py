# network_analysis_functions.py

import itertools
from collections import deque
import networkx as nx

def calculate_social_capital(year, edges_by_year):
    rolling_edges = deque()
    for y in range(year - 3, year):
        edges = edges_by_year.get(y, [])
        rolling_edges.extend(edges)
    
    G = nx.Graph()
    G.add_edges_from(rolling_edges)
    
    brokerage_scores = {
        'constraint': nx.constraint(G),
        'effective_size': nx.effective_size(G),
        'local_clustering': nx.clustering(G)
    }
    return year, brokerage_scores
