from queue import PriorityQueue

storage_room_num, hallways_num = input().split()
storage_room_num = int(storage_room_num)
hallways_num = int(hallways_num)

edge_list = []
cost_map = {}

pq = PriorityQueue()

for i in range(0, hallways_num):
    node1, node2, cost = input().split()
    edge_list.append([node1, node2])
    cost_map[tuple([node1, node2])] = cost
    cost_map[tuple([node2, node1])] = cost
    pq.put((int(cost), [node1, node2]))

#turn edge list into adjacency matrix
graph = {}

for i in range(0, len(edge_list)):

    if edge_list[i][0] not in graph.keys():
        graph[edge_list[i][0]] = []

    if edge_list[i][1] not in graph.keys():
        graph[edge_list[i][1]] = []

    graph[edge_list[i][0]].append(edge_list[i][1])
    graph[edge_list[i][1]].append(edge_list[i][0])


'''visited_set = set()

current_cost = 0
edge_count = 0

while edge_count < len(graph)-1:
    (cost, nodes) = pq.get()
    if nodes[0] not in visited_set or nodes[1] not in visited_set:
        current_cost = current_cost + int(cost)
        visited_set.add(nodes[0])
        visited_set.add(nodes[1])
        edge_count = edge_count + 1'''



visited_set = set()

current_cost = 0
edge_count = 0
current_node = '0'
visited_set.add(current_node)

pq2 = PriorityQueue()
#and int(cost_map[tuple([elem, current_node])]) < int(min_cost):
while len(visited_set) < len(graph):
    for elem in graph[current_node]:
        if elem not in visited_set:
            pq2.put((int(cost_map[tuple([elem, current_node])]), elem))
    run = True
    while(run):
        (cost, node) = pq2.get()
        if node not in visited_set:
            current_cost = current_cost + cost
            current_node = node
            visited_set.add(node)
            run = False

#kruskal

print(current_cost)



