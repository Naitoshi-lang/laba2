from collections import deque, defaultdict

#Работа с графом

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_matrix = [[0]*n for _ in range(n)]  # матрица смежности
        self.adj_list = [[] for _ in range(n)]       # список смежности
    
    def add_edge(self, u, v):
        """Добавить ребро в граф (неориентированный)"""
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
    
    def get_connected_components(self):
        """Найти компоненты связности графа"""
        visited = [False] * self.n
        components = []
        
        def dfs(v, component):
            stack = [v]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    component.append(node)
                    for neighbor in self.adj_list[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return component
        
        for v in range(self.n):
            if not visited[v]:
                components.append(dfs(v, []))
        
        return components
    
    def get_degrees(self):
        """Вычислить степени вершин и найти min/max"""
        degrees = []
        
        # По матрице смежности
        for i in range(self.n):
            degree = sum(self.adj_matrix[i])  # сумма строки = степень вершины
            degrees.append(degree)
        
        min_degree = min(degrees)
        max_degree = max(degrees)
        
        min_vertices = [i for i, d in enumerate(degrees) if d == min_degree]
        max_vertices = [i for i, d in enumerate(degrees) if d == max_degree]
        
        return degrees, min_degree, max_degree, min_vertices, max_vertices

#поиск в лаберинте

def find_shortest_path_in_maze(n, m, maze):
    """Найти кратчайший путь в лабиринте с помощью BFS"""
    
    # Находим стартовую и конечную позиции
    start = end = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)
    
    if not start or not end:
        return -1, ""
    
    # Направления: U, D, R, L
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L')]
    
    # BFS
    queue = deque([start])
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    # Для восстановления пути
    parent = [[None]*m for _ in range(n)]
    move_char = [[None]*m for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        
        # Если дошли до выхода
        if (x, y) == end:
            # Восстанавливаем путь
            path = []
            dist = 0
            cx, cy = x, y
            
            while (cx, cy) != start:
                path.append(move_char[cx][cy])
                cx, cy = parent[cx][cy]
                dist += 1
            
            path.reverse()
            return dist, ''.join(path)
        
        # Проверяем все соседние клетки
        for dx, dy, char in directions:
            nx, ny = x + dx, y + dy
            
            # Проверка границ и проходимости
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] != '#':
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    move_char[nx][ny] = char
                    queue.append((nx, ny))
    
    # Путь не найден
    return -1, ""
