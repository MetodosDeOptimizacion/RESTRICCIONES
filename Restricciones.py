# Solución en Python para los ejercicios planteados
import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 3: Restricciones
x = np.linspace(0, 12, 100)
y1 = 12 - x  # Restricción: x + y <= 12
y2 = np.full_like(x, 6)  # Restricción: y >= 6
x2 = np.full_like(x, 4)  # Restricción: x >= 4

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="x + y = 12")
plt.axhline(6, color="r", linestyle="--", label="y = 6")
plt.axvline(4, color="g", linestyle="--", label="x = 4")
plt.fill_between(x, 6, y1, where=(x >= 4) & (y1 >= 6), color="gray", alpha=0.3)
plt.xlabel("Tiempo en reuniones (x)")
plt.ylabel("Tiempo en documentación (y)")
plt.title("Región factible del Ejercicio 3")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 4: Restricciones
P1 = np.linspace(0, 18, 100)
P2_1 = (18 - 2 * P1) / 3  # Restricción: 2P1 + 3P2 <= 18
P2_2 = np.full_like(P1, 0)  # Restricción: P2 >= 0
P1_2 = np.full_like(P1, 0)  # Restricción: P1 >= 0

plt.figure(figsize=(8, 6))
plt.plot(P1, P2_1, label="2P1 + 3P2 = 18")
plt.axhline(0, color="r", linestyle="--", label="P2 = 0")
plt.axvline(0, color="g", linestyle="--", label="P1 = 0")
plt.fill_between(P1, 0, P2_1, where=(P2_1 >= 0), color="gray", alpha=0.3)
plt.xlabel("Modelos 3D (P1)")
plt.ylabel("Texturas (P2)")
plt.title("Región factible del Ejercicio 4")
plt.legend()
plt.grid()
plt.show()

# Ejercicio 5: Restricciones
A = np.linspace(0, 10, 100)
B = (50 - 5 * A) / 10  # Restricción: 5A + 10B <= 50
B2 = np.full_like(A, 0)  # Restricción: B >= 0
A2 = np.full_like(A, 0)  # Restricción: A >= 0

plt.figure(figsize=(8, 6))
plt.plot(A, B, label="5A + 10B = 50")
plt.axhline(0, color="r", linestyle="--", label="B = 0")
plt.axvline(0, color="g", linestyle="--", label="A = 0")
plt.fill_between(A, 0, B, where=(B >= 0), color="gray", alpha=0.3)
plt.xlabel("Dispositivos tipo A")
plt.ylabel("Dispositivos tipo B")
plt.title("Región factible del Ejercicio 5")
plt.legend()
plt.grid()
plt.show()
