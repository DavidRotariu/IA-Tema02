import numpy as np

np.random.seed(42)

A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))

print(f"\nMatricea A (4×3):")
print(A)
print(f"\nMatricea B (3×5):")
print(B)
print(f"\nDimensiuni A: {A.shape}")
print(f"Dimensiuni B: {B.shape}")

print("\nProdusul matriceal C = A @ B")
C = A @ B 
print(f"Matricea C (4×5) - rezultatul înmulțirii:")
print(C)
print(f"\nDimensiuni C: {C.shape}")

print(f"\nVerificare compatibilitate: A are {A.shape[1]} coloane, B are {B.shape[1]} coloane")
print(f"Înmulțirea este posibilă deoarece A are 3 coloane și B are 3 linii")


suma_totala = np.sum(C)
print(f"\nSuma tuturor elementelor din C: {suma_totala}")

media_pe_coloane = np.mean(C, axis=0)
print(f"\nMedia pe fiecare coloană (axis=0):")
for i, media in enumerate(media_pe_coloane):
    print(f"  Coloana {i+1}: {media:.2f}")

max_global = np.max(C)
print(f"\nValoarea maximă globală din C: {max_global}")