number_of_wardrones, number_of_pairs = input().split()
number_of_wardrones = int(number_of_wardrones)
number_of_pairs = int(number_of_pairs)

edge_list = []

for i in range(0, number_of_pairs):
    node1, node2 = input().split()
    edge_list.append([node1,node2])

max_num = 0

#turn edge list into adjacency matrix
graph = {}

for i in range(0, len(edge_list)):

    if edge_list[i][0] not in graph.keys():
        graph[edge_list[i][0]] = []

    if edge_list[i][1] not in graph.keys():
        graph[edge_list[i][1]] = []

    graph[edge_list[i][0]].append(edge_list[i][1])
    graph[edge_list[i][1]].append(edge_list[i][0])

#dfs implentation
def dfs(graph, visited_set, starting_node):
    stack = []
    stack.append(starting_node)

    visited_set.add(starting_node)

    while(len(stack) > 0):
        current = stack.pop()
        for i in range(0, len(graph[current])):
            if graph[current][i] not in visted_set:
                visited_set.add(graph[current][i])
                stack.append(graph[current][i])


visted_set = set()
count = 0

for i in graph.keys():
    if i not in visted_set:
        dfs(graph, visted_set, i)
        count = count + 1

print(count)

