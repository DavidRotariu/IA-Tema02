import time

def rezolva_tsp_backtracking(n, matrice, mod='prima', timp_max=60, y_max=1):
    """
    Rezolva TSP folosind backtracking cu 4 moduri de oprire.

    Args:
        n (int): Numarul de orase.
        matrice (list of list): Matricea de distante.
        mod (str): 'prima', 'toate', 'timp', 'y_solutii'.
        timp_max (float): Timpul maxim in secunde (pentru 'timp').
        y_max (int): Numarul de solutii (pentru 'y_solutii').

    Returns:
        tuple: (traseu_optim, cost_minim, nr_solutii, timp_executie)
    """
    
    cost_minim = float('inf')
    traseu_optim = []
    nr_solutii = 0
    oprire = False
    
    start_time = time.perf_counter()

    vizitat = [False] * n
    vizitat[0] = True
    traseu_curent = [0]
    
    def backtrack(oras_curent, cost_curent):
        nonlocal cost_minim, traseu_optim, nr_solutii, oprire
        
        if oprire:
            return

        # Solutie completa
        if len(traseu_curent) == n:
            dist_retur = matrice[oras_curent][0]
            if dist_retur == 0 and n > 1: # Ar trebui sa fie nonzero daca nu suntem tot in 0
                 # Daca matricea are 0 pe diagonala si 0 la nod 0->0, nu e o problema, dar intoarcerea 
                 # trebuie sa existe. In general distanta e > 0.
                 pass

            cost_total = cost_curent + dist_retur
            nr_solutii += 1
            
            if cost_total < cost_minim:
                cost_minim = cost_total
                traseu_optim = list(traseu_curent) + [0] # Adaugam intoarcerea la start pentru afisare
                
            # Conditii de oprire
            if mod == 'prima':
                oprire = True
            elif mod == 'y_solutii' and nr_solutii >= y_max:
                oprire = True
            
            return

        # Explorare vecini
        for urmator in range(n):
            if oprire:
                return
                
            if not vizitat[urmator]:
                # Verificare timp
                if mod == 'timp':
                    if time.perf_counter() - start_time >= timp_max:
                        oprire = True
                        return

                cost_nou = cost_curent + matrice[oras_curent][urmator]
                
                # Prunere (Branch and Bound)
                # Daca costul curent deja depaseste minimul gasit, nu mai continuam
                if mod in ['toate', 'prima', 'y_solutii'] and cost_nou >= cost_minim:
                    continue
                
                vizitat[urmator] = True
                traseu_curent.append(urmator)
                
                backtrack(urmator, cost_nou)
                
                traseu_curent.pop()
                vizitat[urmator] = False

    backtrack(0, 0)
    end_time = time.perf_counter()
    
    return traseu_optim, cost_minim, nr_solutii, end_time - start_time
