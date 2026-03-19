import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Generare orașe (exemplu)
# -----------------------------
def generate_cities(n):
    return np.random.rand(n, 2) * 100  # coordonate X,Y

# -----------------------------
# 2. Distanța dintre două orașe
# -----------------------------
def distance(a, b):
    return np.linalg.norm(a - b)

# -----------------------------
# 3. Costul unui traseu
# -----------------------------
def route_length(route, cities):
    return sum(distance(cities[route[i]], cities[route[(i+1) % len(route)]])
               for i in range(len(route)))

# -----------------------------
# 4. Inițializare populație
# -----------------------------
def create_population(size, n_cities):
    return [random.sample(range(n_cities), n_cities) for _ in range(size)]

# -----------------------------
# 5. Crossover (Order Crossover)
# -----------------------------
def crossover(parent1, parent2):
    a, b = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[a:b] = parent1[a:b]

    fill = [x for x in parent2 if x not in child]
    j = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = fill[j]
            j += 1
    return child

# -----------------------------
# 6. Mutare (swap mutation)
# -----------------------------
def mutate(route, rate=0.02):
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route

# -----------------------------
# 7. Selectie (tournament)
# -----------------------------
def select(pop, cities, k=5):
    best = None
    for _ in range(k):
        candidate = random.choice(pop)
        if best is None or route_length(candidate, cities) < route_length(best, cities):
            best = candidate
    return best

# -----------------------------
# 8. Algoritmul Genetic
# -----------------------------
def genetic_tsp(cities, pop_size=100, generations=500):
    population = create_population(pop_size, len(cities))

    for gen in range(generations):
        new_pop = []

        for _ in range(pop_size):
            p1 = select(population, cities)
            p2 = select(population, cities)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

        if gen % 50 == 0:
            best = min(population, key=lambda r: route_length(r, cities))
            print(f"Gen {gen}: {route_length(best, cities):.2f}")

    best = min(population, key=lambda r: route_length(r, cities))
    return best, route_length(best, cities)

# -----------------------------
# 9. Vizualizare traseu
# -----------------------------
def plot_route(cities, route, title="Cel mai bun traseu TSP"):
    ordered = cities[route + [route[0]]]  # închidem circuitul
    plt.figure(figsize=(8, 6))
    plt.plot(ordered[:, 0], ordered[:, 1], '-o')
    for i, (x, y) in enumerate(cities):
        plt.text(x + 0.5, y + 0.5, str(i), fontsize=9)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 10. Rulare exemplu
# -----------------------------
if __name__ == "__main__":
    cities = generate_cities(20)
    best_route, best_cost = genetic_tsp(cities)

    print("\nCel mai bun traseu găsit:")
    print(best_route)
    print("Cost total:", best_cost)

    # vizualizare
    plot_route(cities, best_route, title=f"Cel mai bun traseu (cost = {best_cost:.2f})")
