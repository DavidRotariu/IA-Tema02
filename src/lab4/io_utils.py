import random

def citeste_matrice(cale):
    """
    Citeste matricea de distante dintr-un fisier text.

    Args:
        cale (str): Calea catre fisierul de intrare.

    Returns:
        tuple: (n, matrice_distante)
            n (int): Numarul de orase.
            matrice_distante (list of lists): Matricea de distante NxN.
    """
    try:
        with open(cale, 'r') as f:
            lines = f.readlines()
            # Ignoram liniile goale sau de comentarii
            lines = [l.strip() for l in lines if l.strip()]
            
            n = int(lines[0])
            matrice = []
            
            for i in range(1, n + 1):
                linie = list(map(int, lines[i].split()))
                if len(linie) != n:
                    raise ValueError(f"Linia {i} nu contine {n} valori.")
                matrice.append(linie)
                
            return n, matrice
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{cale}' nu a fost gasit.")
        return 0, []
    except Exception as e:
        print(f"Eroare la citirea matricei: {e}")
        return 0, []

def genereaza_matrice_aleatorie(n, seed=None):
    """
    Genereaza o matrice de distante NxN simetrica cu valori in [1, 100].

    Args:
        n (int): Numarul de orase.
        seed (int, optional): Seed pentru random. Default None.

    Returns:
        list of list: Matricea generata.
    """
    if seed is not None:
        random.seed(seed)
        
    matrice = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = random.randint(1, 100)
            matrice[i][j] = dist
            matrice[j][i] = dist
            
    return matrice
