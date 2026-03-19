import numpy as np

# 1. Setăm seed pentru reproductibilitate
np.random.seed(42)

# Generăm matricele A (4x3) și B (3x5)
A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))

print("Matricea A (4x3):")
print(A)

print("\nMatricea B (3x5):")
print(B)

# 2. Produsul matriceal C = A @ B
C = A @ B

print("\nProdusul matriceal C = A @ B:")
print(C)

# 3. Calcule statistice pe C
sum_C = np.sum(C)
mean_columns = np.mean(C, axis=0)
max_C = np.max(C)

print("\nSuma tuturor elementelor din C:", sum_C)
print("Media pe fiecare coloană:", mean_columns)
print("Valoarea maximă globală:", max_C)


# 4. BONUS
print("\n--- BONUS ---")

# Generăm matrice pătratică 3x3
M = np.random.randint(1, 11, size=(3, 3))

print("Matricea M:")
print(M)

# Determinant
det_M = np.linalg.det(M)
print("\nDeterminantul lui M:", det_M)

# Inversa
inv_M = np.linalg.inv(M)
print("\nInversa lui M:")
print(inv_M)

# Verificare M * M^-1 ≈ I
identity_check = M @ inv_M

print("\nM @ inv(M):")
print(identity_check)

print("\nEste aproape matrice identitate?",
      np.allclose(identity_check, np.eye(3)))