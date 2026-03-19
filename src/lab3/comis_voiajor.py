import itertools

def tsp_bruteforce(dist):
    n = len(dist)
    orase = range(n)
    best_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(orase[1:]):
        path = (0,) + perm + (0,)
        cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))

        if cost < best_cost:
            best_cost = cost
            best_path = path

    return best_path, best_cost


# Exemplu de matrice de distanțe
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_bruteforce(dist)
print("Cel mai bun traseu:", path)
print("Cost total:", cost)
