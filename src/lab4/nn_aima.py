try:
    from aima3.search import nearest_neighbor_tsp
except ImportError:
    # Fallback implementation if aima3 doesn't have it (common with PyPI package)
    def nearest_neighbor_tsp(start, cities, distances):
        """
        Construieste un tur TSP prin euristica celui mai apropiat vecin.
        (Implementare locala bazata pe aima-python)
        """
        current_city = start
        path = [current_city]
        unvisited = set(cities)
        unvisited.remove(current_city)
        
        while unvisited:
            next_city = min(unvisited, key=lambda city: distances[current_city][city])
            unvisited.remove(next_city)
            path.append(next_city)
            current_city = next_city
            
        return path

def rezolva_tsp_nn_aima(n, matrice, start=0):
    """
    Wrapper peste nearest_neighbor_tsp din aima3.

    Args:
        n (int): Numar orase.
        matrice (list of list): Matricea de distante.
        start (int): Orasul de start.

    Returns:
        tuple: (traseu, cost)
    """
    cities = list(range(n))
    distances = {}
    for i in range(n):
        distances[i] = {}
        for j in range(n):
            distances[i][j] = matrice[i][j]
            
    # Apel aima
    traseu_aima = nearest_neighbor_tsp(start, cities, distances)
    
    # Conversie la formatul nostru (traseu inchis, cost calculat)
    traseu = list(traseu_aima)
    
    # Calcul cost
    cost = 0
    for i in range(len(traseu) - 1):
        u = traseu[i]
        v = traseu[i+1]
        cost += matrice[u][v]
        
    # Adaugare retur la start
    if traseu[-1] != start:
        last = traseu[-1]
        cost += matrice[last][start]
        traseu.append(start)
        
    return traseu, cost

def rezolva_tsp_nn_aima_multistart(n, matrice):
    """
    Multistart NN folosind aima.
    """
    best_cost = float('inf')
    best_traseu = []
    toate_costurile = []
    
    for start in range(n):
        traseu, cost = rezolva_tsp_nn_aima(n, matrice, start)
        toate_costurile.append(cost)
        
        if cost < best_cost:
            best_cost = cost
            best_traseu = traseu
            
    return best_traseu, best_cost, toate_costurile
