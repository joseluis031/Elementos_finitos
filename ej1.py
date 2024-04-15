import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dimensiones del dominio
nx = 10  # Número de puntos en la dirección x
ny = 10  # Número de puntos en la dirección y
nz = 10  # Número de puntos en la dirección z

# Crear una malla tridimensional con valores de 0 en todas partes
domain = np.zeros((nx, ny, nz))

# Definir una región en el dominio con valores distintos (por ejemplo, una esfera)
center = (nx // 2, ny // 2, nz // 2)  # Centro de la esfera
radius = min(nx, ny, nz) // 4  # Radio de la esfera

# Generar la esfera en el dominio
for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            if (i - center[0])**2 + (j - center[1])**2 + (k - center[2])**2 <= radius**2:
                domain[i, j, k] = 1  # Asignar valor 1 dentro de la esfera

# Visualizar el dominio estructural
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Encontrar los índices donde el dominio tiene valor 1 (dentro de la esfera)
x, y, z = np.where(domain == 1)

# Graficar los puntos dentro de la esfera
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Dominio Estructural')

plt.show()
