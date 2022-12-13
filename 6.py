vertices_num, edges_num = input().split()
vertices_num = int(vertices_num)
edges_num = int(edges_num)

edge_list = []
for i in range(0, edges_num):
    node1, node2 = input().split()
    edge_list.append([node1, node2])

cycle_num = int(input())
cycles = []

for i in range(0, cycle_num):
    current_cycle = input()
    current_cycle = [c for c in current_cycle.split(' ')]
    if current_cycle[len(current_cycle)-1] == '':
        current_cycle.pop()
    for x in range(0, len(current_cycle)):
        current_cycle[x] = int(current_cycle[x])
    cycles.append(current_cycle)

#turn edge list into adjacency matrix
graph = {}

for i in range(0, len(edge_list)):

    if int(edge_list[i][0]) not in graph.keys():
        graph[int(edge_list[i][0])] = set()

    if int(edge_list[i][1]) not in graph.keys():
        graph[int(edge_list[i][1])] = set()

    graph[int(edge_list[i][0])].add(int(edge_list[i][1]))
    graph[int(edge_list[i][1])].add(int(edge_list[i][0]))

for i in range(0, len(cycles)):
    cycle_test = cycles[i]
    cycle_test.append(cycle_test[0])

    visted_set = set()

    current_node = cycle_test.pop()

    invalid = False

    while(len(cycle_test)>0):
        next_node = cycle_test.pop()
        if current_node not in graph[next_node] or (next_node in visted_set):
            print('NO')
            invalid = True
            break
        current_node = next_node
        visted_set.add(current_node)

    if not invalid:
        print('YES')


