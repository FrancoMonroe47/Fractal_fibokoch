import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import hsv_to_rgb

phi = (1 + np.sqrt(5)) / 2  # Proporción áurea
iterations = 5               # Iteraciones (¡cuidado con >6!)

# Configura colores
colors = []
for i in range(iterations + 1):
    hue = (i * 137.5) % 360
    rgb = hsv_to_rgb([hue/360, 0.8, 0.8])
    colors.append(rgb)

# Vértices de un tetraedro regular
def tetrahedron():
    return np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0.5, np.sqrt(3)/2, 0],
        [0.5, np.sqrt(3)/6, np.sqrt(6)/3]
    ])

# Divide una cara en subtetraedros según Fibonacci
def divide_face(face, iteration):
    new_faces = []
    centroid = np.mean(face, axis=0)
    scale = 1 / (phi ** iteration)
    
    # Añade nuevos tetraedros en las subdivisiones
    for vertex in face:
        direction = (vertex - centroid) * scale
        new_face = vertex + direction * phi
        new_faces.append(new_face)
    
    return new_faces

# Construye el fractal recursivamente
def build_fractal(faces, iteration):
    if iteration > iterations:
        return faces
    
    new_faces = []
    for face in faces:
        subdivided = divide_face(face, iteration)
        new_faces.extend(subdivided)
    
    return build_fractal(new_faces, iteration + 1)

# Configura la figura 3D
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#0f0f23')

# Inicia con un tetraedro base
initial_faces = [tetrahedron()]
fractal_faces = build_fractal(initial_faces, 1)

# Dibuja todas las caras
for i, face in enumerate(fractal_faces):
    ax.plot_trisurf(
        face[:, 0], face[:, 1], face[:, 2],
        color=colors[i % len(colors)],
        alpha=0.6,
        edgecolor='white'
    )

ax.axis('off')
plt.savefig('fractal_3d.png', dpi=200, bbox_inches='tight')
plt.show()
