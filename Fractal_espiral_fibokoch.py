import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

phi = (1 + np.sqrt(5)) / 2
iterations = 8       # ¡Puedes subir a 10+ si MyBinder lo permite!
L = 4.0              # Longitud base
angle_step = np.deg2rad(137.5)  # Ángulo áureo en radianes

# Configura colores (rotación áurea en tonos)
colors = []
for i in range(iterations + 1):
    hue = (i * 137.5) % 360
    rgb = hsv_to_rgb([hue/360, 0.8, 0.9])
    colors.append(rgb)

# Función recursiva para dibujar la espiral
def draw_spiral(start_point, direction, length, iteration):
    if iteration > iterations:
        return
    
    # Calcula el nuevo punto "avanzando" en la dirección actual
    end_point = start_point + length * direction
    
    # Dibuja un triángulo equilátero en el punto actual
    triangle_height = length / (phi ** iteration)
    angle = np.pi / 2  # Ajusta para orientación vertical inicial
    
    # Crea vértices del triángulo (rotado según ángulo áureo)
    v1 = end_point
    v2 = v1 + triangle_height * np.array([np.cos(angle + angle_step), np.sin(angle + angle_step)])
    v3 = v1 + triangle_height * np.array([np.cos(angle - angle_step), np.sin(angle - angle_step)])
    
    # Dibuja y rellena el triángulo
    triangle = np.array([v1, v2, v3, v1])
    plt.fill(triangle[:, 0], triangle[:, 1], color=colors[iteration], alpha=0.7)
    
    # Actualiza dirección para la próxima iteración (rotación áurea)
    new_direction = direction * np.cos(angle_step) + np.array([-direction[1], direction[0]]) * np.sin(angle_step)
    
    # Llama recursivamente para las siguientes ramas
    draw_spiral(end_point, new_direction, length / phi, iteration + 1)
    draw_spiral(end_point, -new_direction, length / phi, iteration + 1)

# Configura la figura
plt.figure(figsize=(12, 12))
plt.axis('equal')
plt.axis('off')
plt.gca().set_facecolor('#0f0f23')

# Punto inicial y dirección (centro hacia arriba)
start = np.array([0, 0])
initial_direction = np.array([0, 1])  # Apunta hacia arriba

# Dibuja la espiral principal y sus ramas
draw_spiral(start, initial_direction, L, 0)

# Añade el triángulo central (opcional)
plt.fill([-0.1, 0.1, 0], [0, 0, 0.2], color=colors[0], alpha=1)

plt.savefig('espiral_fibokoch.png', dpi=300, bbox_inches='tight')
plt.show()
