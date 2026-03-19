import argparse
import sys
import time

from io_utils import citeste_matrice, genereaza_matrice_aleatorie
from backtracking import rezolva_tsp_backtracking
from nearest_neighbor import rezolva_tsp_nn, rezolva_tsp_nn_multistart, rezolva_tsp_nn_timp
from nn_aima import rezolva_tsp_nn_aima, rezolva_tsp_nn_aima_multistart

def main():
    parser = argparse.ArgumentParser(description="Rezolvare TSP - Laborator 4")
    parser.add_argument("fisier", help="Calea catre fisierul cu matricea de distante (sau 'random-N' pentru generare)")
    parser.add_argument("--algoritm", choices=['bt', 'nn', 'nn_aima'], default='bt', help="Algoritmul de folosit: bt, nn, nn_aima")
    parser.add_argument("--mod", choices=['prima', 'toate', 'timp', 'y_solutii'], default='prima', help="Modul de oprire (pentru BT/NN)")
    parser.add_argument("--timp", type=float, default=60, help="Timpul maxim in secunde (pentru mod=timp)")
    parser.add_argument("--y", type=int, default=1, help="Numarul de solutii (pentru mod=y_solutii)")
    parser.add_argument("--start", type=int, default=0, help="Orasul de start (default 0)")

    args = parser.parse_args()

    # Citire sau generare matrice
    if args.fisier.startswith("random-"):
        try:
            n = int(args.fisier.split("-")[1])
            matrice = genereaza_matrice_aleatorie(n, seed=42)
            print(f"Generata matrice random {n}x{n}")
        except ValueError:
            print("Format invalid pentru random. Folositi random-N (ex: random-10).")
            return
    else:
        n, matrice = citeste_matrice(args.fisier)
        if n == 0:
            return

    start_time = time.perf_counter()
    
    if args.algoritm == 'bt':
        print(f"Running Backtracking with mod={args.mod}...")
        traseu, cost, nr_sol, t_exec = rezolva_tsp_backtracking(n, matrice, mod=args.mod, timp_max=args.timp, y_max=args.y)
        
        print(f"Traseu optim:   {' -> '.join(map(str, traseu))}")
        print(f"Cost minim:     {cost}")
        print(f"Solutii gasite: {nr_sol}")
        print(f"Timp de executie: {t_exec:.6f} secunde")
        
    elif args.algoritm == 'nn':
        print(f"Running Nearest Neighbor ({args.mod})...")
        
        if args.mod == 'prima':
            traseu, cost = rezolva_tsp_nn(n, matrice, start=args.start)
            print(f"Traseu: {' -> '.join(map(str, traseu))}")
            print(f"Cost: {cost}")
        
        elif args.mod == 'y_solutii' or args.mod == 'toate': # Interpretam 'toate' ca multistart pentru NN
            traseu, cost, toate = rezolva_tsp_nn_multistart(n, matrice)
            print(f"Cel mai bun traseu: {' -> '.join(map(str, traseu))}")
            print(f"Cost minim: {cost}")
            # print(f"Toate costurile: {toate}")
            
        elif args.mod == 'timp':
            traseu, cost = rezolva_tsp_nn_timp(n, matrice, timp_max=args.timp)
            print(f"Cel mai bun traseu (in {args.timp}s): {' -> '.join(map(str, traseu))}")
            print(f"Cost minim: {cost}")

        end_time = time.perf_counter()
        print(f"Timp total rulare: {end_time - start_time:.6f} secunde")

    elif args.algoritm == 'nn_aima':
        print(f"Running Nearest Neighbor AIMA ({args.mod})...")
        
        if args.mod == 'prima':
            traseu, cost = rezolva_tsp_nn_aima(n, matrice, start=args.start)
            print(f"Traseu: {' -> '.join(map(str, traseu))}")
            print(f"Cost: {cost}")
            
        elif args.mod == 'y_solutii' or args.mod == 'toate':
            traseu, cost, toate = rezolva_tsp_nn_aima_multistart(n, matrice)
            print(f"Cel mai bun traseu: {' -> '.join(map(str, traseu))}")
            print(f"Cost minim: {cost}")
            # print(f"Toate costurile: {toate}")
            
        else:
            print("Modul 'timp' nu este implementat explicit pentru nn_aima in acest exemplu. Folositi multistart.")

        end_time = time.perf_counter()
        print(f"Timp total rulare: {end_time - start_time:.6f} secunde")

if __name__ == "__main__":
    main()
