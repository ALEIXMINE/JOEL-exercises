# Nom: Asteroides
# Enllaç: https://jo-el.es/problem/asteroides

from queue import Queue

# No entenc aquest codic pero funciona :D

# Función para obtener los vecinos de una celda
def get_neighbors(grid, row, col):
    neighbors = []
    if row > 0 and grid[row - 1][col] != '*':
        neighbors.append((row - 1, col))
    if row < len(grid) - 1 and grid[row + 1][col] != '*':
        neighbors.append((row + 1, col))
    if col > 0 and grid[row][col - 1] != '*':
        neighbors.append((row, col - 1))
    if col < len(grid[0]) - 1 and grid[row][col + 1] != '*':
        neighbors.append((row, col + 1))
    return neighbors

# Función para buscar la salida del campo de asteroides
def find_exit(grid, start, end):
    visited = set() # Conjunto de celdas visitadas
    q = Queue() # Cola de celdas a visitar
    q.put(start)
    while not q.empty():
        cell = q.get()
        if cell == end:
            return 'SI' # Se encontró la salida
        if cell in visited:
            continue
        visited.add(cell)
        row, col = cell
        for neighbor in get_neighbors(grid, row, col):
            q.put(neighbor)
    return 'NO' # No se encontró la salida

# Lectura de casos de prueba
cases = int(input())
for i in range(cases):
    rows, cols = map(int, input().split())
    grid = []
    start = None
    end = None
    for j in range(rows):
        row = input().strip()
        if 'S' in row:
            start = (j, row.index('S'))
        if 'F' in row:
            end = (j, row.index('F'))
        grid.append(row)
    print(find_exit(grid, start, end))