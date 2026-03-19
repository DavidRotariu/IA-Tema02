from scipy.spatial.distance import cityblock


def read_vectors(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    v1 = list(map(float, lines[0].split()))
    v2 = list(map(float, lines[1].split()))

    return v1, v2


def manhattan_manual(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune.")

    distance = 0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])

    return distance


def manhattan_scipy(v1, v2):
    return cityblock(v1, v2)

if __name__ == "__main__":
    v1, v2 = read_vectors("src/data/input.txt")

    distance_manual = manhattan_manual(v1, v2)
    distance_scipy = manhattan_scipy(v1, v2)

    print(f"Distanța Manhattan (manual): {distance_manual}")
    
    print(f"Distanța Manhattan (SciPy): {distance_scipy}")