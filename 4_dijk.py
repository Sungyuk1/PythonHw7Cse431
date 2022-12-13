from queue import PriorityQueue

storage_room_num, hallways_num = input().split()
storage_room_num = int(storage_room_num)
hallways_num = int(hallways_num)

edge_list = []
cost_map = {}

for i in range(0, hallways_num):
    node1, node2, cost = input().split()
    edge_list.append([node1,node2])
    cost_map[tuple(node1,node2)] = cost
    cost_map[tuple(node2, node1)] = cost

#turn edge list into adjacency matrix
graph = {}

for i in range(0, len(edge_list)):

    if edge_list[i][0] not in graph.keys():
        graph[edge_list[i][0]] = []

    if edge_list[i][1] not in graph.keys():
        graph[edge_list[i][1]] = []

    graph[edge_list[i][0]].append(edge_list[i][1])
    graph[edge_list[i][1]].append(edge_list[i][0])


visted_set = set()
distance_dict = {}

#set initial distance to infinity
for elem in graph.keys():
    distance_dict[elem] = 999999999999999999999999999999

'''def Dijkstra(graph, starting_node, visited_Set, distance_dict, cost_map):
    distance_dict[starting_node] = 0
    visited_Set.add(starting_node)
    current_node = starting_node

    while(len(visited_Set) < len(graph)):
        for i in range(0, len(graph[current_node])):
            new_distance = distance_dict[current_node] + cost_map[tuple(current_node, graph[current_node][i])]
            if new_distance < distance_dict[graph[current_node][i]]:
                distance_dict[graph[current_node][i]] = new_distance'''

def dijkstra(graph, starting_node, distance_dict, visited_set, cost_map):
    pq = PriorityQueue()
    pq.put((0, starting_node))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited_set.add(current_vertex)

        for i in range(0, graph[current_vertex]):
            new_distance = distance_dict[current_vertex] + cost_map[tuple(current_vertex, graph[current_vertex][i])]
            if new_distance < distance_dict[graph[current_vertex][i]]:
                distance_dict[graph[current_vertex][i]] = new_distance
                pq.put((new_distance, graph[current_vertex][i]))

