import numpy as np

import matplotlib.pyplot as plt

from matplotlib.colors import hsv_to_rgb

 

# Configuración inicial

phi = (1 + np.sqrt(5)) / 2  # Proporción áurea

iterations = 5               # Número de iteraciones

L = 3.0                      # Longitud inicial del lado (para escalar coordenadas)

 

# Paleta de colores (basada en ángulo áureo 137.5°)

colors = []

for i in range(iterations + 1):

    hue = (i * 137.5) % 360  # Ángulo áureo en HSV

    saturation = 0.8

    value = 0.8 if i < 3 else 0.6  # Oscurece en iteraciones altas

    rgb = hsv_to_rgb([hue/360, saturation, value])

    colors.append(rgb)

 

# Función para dividir un segmento en proporción áurea

def divide_segment(start, end):

    direction = end - start

    length = np.linalg.norm(direction)

    unit = direction / length

    split_point = start + unit * (length / phi)

    return [start, split_point, end]

 

# Función para añadir triángulos según Fibonacci

def add_triangles(segments, iteration):

    fib_sequence = [0, 1, 1, 2, 3, 5]  # F(0)=0, F(1)=1,... F(5)=5

    new_segments = []

    

    for segment in segments:

        # Divide el segmento en proporción áurea

        points = divide_segment(segment[0], segment[1])

        

        # Añade triángulos en los puntos de división

        num_triangles = fib_sequence[iteration]

        for i in range(num_triangles):

            # Posición del triángulo (oscila entre los puntos 1 y 2)

            base = points[1] if i % 2 == 0 else points[2]

            height = L / (phi ** (iteration + 1))

            

            # Calcula vértices del triángulo

            angle = np.pi / 3  # 60 grados (triángulo equilátero)

            v1 = base

            v2 = base + height * np.array([np.cos(angle), np.sin(angle)])

            v3 = base + height * np.array([np.cos(-angle), np.sin(-angle)])

            

            # Añade al plot

            triangle = np.array([v1, v2, v3, v1])

            plt.fill(triangle[:, 0], triangle[:, 1], color=colors[iteration], alpha=0.7)

    

        new_segments.extend([(points[0], points[1]), (points[1], points[2])])

    

    return new_segments

 

# Inicializa con un triángulo equilátero

vertices = np.array([

    [0, 0],

    [L, 0],

    [L/2, L * np.sin(np.pi/3)],

    [0, 0]

])

 

plt.figure(figsize=(10, 10))

plt.fill(vertices[:, 0], vertices[:, 1], color=colors[0])

 

# Iteraciones del fractal

segments = [ (vertices[i], vertices[i+1]) for i in range(3) ]

for iteration in range(1, iterations + 1):

    segments = add_triangles(segments, iteration)

 

# Ajustes estéticos

plt.axis('equal')

plt.axis('off')

plt.gca().set_facecolor('#1a1a1a')  # Fondo oscuro

plt.savefig('fibokoch.png', dpi=300, bbox_inches='tight')

plt.show()

