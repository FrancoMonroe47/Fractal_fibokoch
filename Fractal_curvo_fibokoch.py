import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from matplotlib.colors import hsv_to_rgb

phi = (1 + np.sqrt(5)) / 2
iterations = 6

# Configura colores
colors = []
for i in range(iterations + 1):
    hue = (i * 137.5) % 360
    rgb = hsv_to_rgb([hue/360, 0.8, 0.8])
    colors.append(rgb)

# Curva de Bézier para "doblar" los triángulos
def curved_triangle(points, tension=0.5):
    tck, u = splprep(points.T, s=0, per=True)
    new_points = splev(np.linspace(0, 1, 100), tck)
    return np.array(new_points).T

# Función recursiva para triángulos curvos
def draw_curved_fractal(start, scale, angle, iteration):
    if iteration > iterations:
        return
    
    # Crea un triángulo curvo
    points = np.array([
        start,
        start + scale * np.array([np.cos(angle), np.sin(angle)]),
        start + scale * np.array([np.cos(angle + 2*np.pi/3), np.sin(angle + 2*np.pi/3)]),
        start  # Cierra el triángulo
    ])
    
    # Aplica curvatura
    curved = curved_triangle(points, tension=0.7)
    plt.fill(curved[:, 0], curved[:, 1], color=colors[iteration], alpha=0.4)
    
    # Subdivide con Fibonacci
    for i in range(2):  # Ramas según Fibonacci (1, 1, 2...)
        new_angle = angle + (-1)**i * np.pi / (phi ** 2)
        new_scale = scale / phi
        draw_curved_fractal(points[i+1], new_scale, new_angle, iteration + 1)

# Configura la figura
plt.figure(figsize=(12, 12))
plt.axis('equal')
plt.axis('off')
plt.gca().set_facecolor('#1a1a1a')

# Inicia desde el centro
draw_curved_fractal(np.array([0, 0]), 3.0, 0, 0)

plt.savefig('curvo_fibokoch.png', dpi=300, bbox_inches='tight')
plt.show()
