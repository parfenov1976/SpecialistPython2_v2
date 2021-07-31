# В 7-ом модуле мы изучали "алгоритм поиска в ширину(bfs)".
# Перепишите предложенный алгоритм, используя в качестве очереди класс "Очередь" из модуля collections
# collections.deque()

import collections
queue = collections.deque()
#  BFS(Breadth-First Search). Алгоритм поиска в ширину.
# Позволяет найти кратчайшие расстояния из одной вершины невзвешенного (ориентированного или неориентированного) графа
# до всех остальных вершин.
# Под кратчайшим путем подразумевается путь, содержащий наименьшее число ребер.
# Алгоитм:
# 1. Начальную вершину помещаем в очередь
# 2. Пока очередь не пуста:
#   2.1 Достаем из очереди первую вершину
#   2.2 Для каждой вершины списка смежности
#       2.2.1 Если еще до этой вершины еще не доходили, то помечаем расстояние до нее и добавляем ее в конец очереди
#       2.2.1 Если вершину уэе посещали, то игнорируем ее
#         3 --5--2   6--7
#        / \ /  /
#       0---1--4
graph = [
    # список смежности
    [1, 3],         # 0
    [0, 3, 4, 5],   # 1
    [4, 5],         # 2
    [0, 1, 5],      # 3
    [1, 2],         # 4
    [1, 2, 3],      # 5
    [7],            # 6
    [6]             # 7
]

start = 0
lengths = [None] * (len(graph))
lengths[start] = 0
queue.append(start)
while queue:
    cur_vertex = queue.popleft()
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)

print(lengths)
