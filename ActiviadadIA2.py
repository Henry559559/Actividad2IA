import networkx as nx
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

# Generar datos ficticios
estaciones = [f'Estacion{num}' for num in range(1, 51)]
rutas = [(f'Estacion{i}', f'Estacion{j}', random.randint(5, 15)) for i in range(1, 51) for j in range(i+1, 51) if random.random() < 0.05]

# Construcción de la Base de Conocimiento
G = nx.Graph()
G.add_nodes_from(estaciones)
G.add_weighted_edges_from(rutas)

def encontrar_mejor_ruta(grafo, inicio, fin):
    return nx.shortest_path(grafo, source=inicio, target=fin, weight='weight')

def visualizar_red_3d(grafo, ruta=None):
    # Crear una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Generar posiciones 3D aleatorias para cada nodo
    pos_3d = {node: (random.random(), random.random(), random.random()) for node in grafo.nodes()}
    
    # Dibujar nodos
    for node, coordinates in pos_3d.items():
        ax.scatter(*coordinates, s=100)
    
    # Dibujar aristas
    for edge in grafo.edges():
        x_coords = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
        y_coords = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
        z_coords = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
        ax.plot(x_coords, y_coords, z_coords, color='gray')
    
    # Dibujar la ruta
    if ruta:
        for i in range(1, len(ruta)):
            x_coords = [pos_3d[ruta[i-1]][0], pos_3d[ruta[i]][0]]
            y_coords = [pos_3d[ruta[i-1]][1], pos_3d[ruta[i]][1]]
            z_coords = [pos_3d[ruta[i-1]][2], pos_3d[ruta[i]][2]]
            ax.plot(x_coords, y_coords, z_coords, color='red', linewidth=2)
    
    plt.show()

# Encontrar la mejor ruta
mejor_ruta = encontrar_mejor_ruta(G, 'Estacion1', 'Estacion50')

# Visualizar la red y la mejor ruta en 3D
visualizar_red_3d(G, mejor_ruta)
