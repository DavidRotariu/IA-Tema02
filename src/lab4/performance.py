import random
import time
import matplotlib.pyplot as plt
from backtracking import rezolva_tsp_backtracking
from nearest_neighbor import rezolva_tsp_nn, rezolva_tsp_nn_multistart
from io_utils import genereaza_matrice_aleatorie

# Set backend to avoid display issues
plt.switch_backend('Agg')

def masoara_timp_bt(n, matrice, mod, **kwargs):
    """Masoara timpul de executie pentru backtracking."""
    start = time.perf_counter()
    rezolva_tsp_backtracking(n, matrice, mod=mod, **kwargs)
    end = time.perf_counter()
    return end - start

def masoara_timp_nn(n, matrice, multistart=False):
    """Masoara timpul de executie pentru NN."""
    start = time.perf_counter()
    if multistart:
        rezolva_tsp_nn_multistart(n, matrice)
    else:
        rezolva_tsp_nn(n, matrice, start=0)
    end = time.perf_counter()
    return end - start

def ruleaza_experiment():
    """Ruleaza experimentul comparativ si genereaza graficul de performanta."""
    valori_n_bt = [5, 8, 10, 12]
    valori_n_nn = [5, 8, 10, 12, 15, 20, 30, 50]

    random.seed(42)
    
    timpi_bt_prima = []
    timpi_bt_ysol = [] # y_max=N
    timpi_nn_simplu = []
    timpi_nn_multi = []

    print("Rulare experimente BT...")
    for n in valori_n_bt:
        matrice = genereaza_matrice_aleatorie(n, seed=42)
        
        # BT Prima solutie
        t = masoara_timp_bt(n, matrice, mod='prima')
        timpi_bt_prima.append(t)
        
        # BT Y Solutii (Y=N)
        t = masoara_timp_bt(n, matrice, mod='y_solutii', y_max=n)
        timpi_bt_ysol.append(t)

        print(f"N={n} done.")

    print("Rulare experimente NN...")
    for n in valori_n_nn:
        matrice = genereaza_matrice_aleatorie(n, seed=42)
        
        # NN Simplu
        t = masoara_timp_nn(n, matrice, multistart=False)
        timpi_nn_simplu.append(t)
        
        # NN Multistart
        t = masoara_timp_nn(n, matrice, multistart=True)
        timpi_nn_multi.append(t)
        
        print(f"N={n} done.")

    genereaza_grafic_timpi(valori_n_bt, timpi_bt_prima, timpi_bt_ysol,
                           valori_n_nn, timpi_nn_simplu, timpi_nn_multi)

def genereaza_grafic_timpi(n_bt, t_bt_prima, t_bt_ysol, n_nn, t_nn_simplu, t_nn_multi):
    """Genereaza graficul 1 (timpi de rulare)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot Scala Liniara
    ax1.plot(n_bt, t_bt_prima, 'o-', label='BT Prima Solutiie')
    ax1.plot(n_bt, t_bt_ysol, 's-', label='BT Y Solutii')
    ax1.plot(n_nn, t_nn_simplu, 'x-', label='NN Simplu')
    ax1.plot(n_nn, t_nn_multi, '^-', label='NN Multistart')
    
    ax1.set_title('Timp de Rulare (Scala Liniara)')
    ax1.set_xlabel('N (Numar orase)')
    ax1.set_ylabel('Timp (s)')
    ax1.legend()
    ax1.grid(True)

    # Plot Scala Logaritmica
    ax2.plot(n_bt, t_bt_prima, 'o-', label='BT Prima Solutiie')
    ax2.plot(n_bt, t_bt_ysol, 's-', label='BT Y Solutii')
    ax2.plot(n_nn, t_nn_simplu, 'x-', label='NN Simplu')
    ax2.plot(n_nn, t_nn_multi, '^-', label='NN Multistart')
    
    ax2.set_yscale('log')
    ax2.set_title('Timp de Rulare (Scala Logaritmica)')
    ax2.set_xlabel('N (Numar orase)')
    ax2.set_ylabel('Timp (s) - Log')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('comparare_performanta.png')
    print("Graficul a fost salvat in 'comparare_performanta.png'")

if __name__ == "__main__":
    ruleaza_experiment()
