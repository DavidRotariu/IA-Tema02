import time

def rezolva_tsp_nn(n, matrice, start=0):
    """
    Rezolva TSP folosind euristica Nearest Neighbor (NN).

    Args:
        n (int): Numarul de orase.
        matrice (list of list): Matricea de distante.
        start (int): Orasul de start.

    Returns:
        tuple: (traseu, cost)
    """
    traseu = [start]
    vizitat = {start}
    oras_curent = start
    cost_total = 0
    
    # Mergem in cel mai apropiat vecin nevizitat
    for _ in range(n - 1):
        cel_mai_aproape = -1
        dist_min = float('inf')
        
        for urmator in range(n):
            if urmator not in vizitat:
                dist = matrice[oras_curent][urmator]
                if dist < dist_min:
                    dist_min = dist
                    cel_mai_aproape = urmator
        
        cost_total += dist_min
        traseu.append(cel_mai_aproape)
        vizitat.add(cel_mai_aproape)
        oras_curent = cel_mai_aproape
        
    # Intoarcere la start
    cost_total += matrice[oras_curent][start]
    traseu.append(start)
    
    return traseu, cost_total

def rezolva_tsp_nn_multistart(n, matrice):
    """
    Rezolva TSP folosind NN multistart (toti nodurile de start).

    Returns:
        tuple: (best_traseu, best_cost, toate_costurile)
    """
    best_cost = float('inf')
    best_traseu = []
    toate_costurile = []
    
    for start in range(n):
        traseu, cost = rezolva_tsp_nn(n, matrice, start)
        toate_costurile.append(cost)
        
        if cost < best_cost:
            best_cost = cost
            best_traseu = traseu
            
    return best_traseu, best_cost, toate_costurile

def rezolva_tsp_nn_timp(n, matrice, timp_max):
    """
    Rezolva TSP folosind NN, oprindu-se dupa timp_max.

    Returns:
        tuple: (best_traseu, best_cost)
    """
    start_time = time.perf_counter()
    best_cost = float('inf')
    best_traseu = []
    
    for start in range(n):
        if time.perf_counter() - start_time >= timp_max:
            break
            
        traseu, cost = rezolva_tsp_nn(n, matrice, start)
        
        if cost < best_cost:
            best_cost = cost
            best_traseu = traseu
            
    return best_traseu, best_cost
