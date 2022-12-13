vertices_num, edges_num, k = input().split()
vertices_num = int(vertices_num)
edges_num = int(edges_num)
k = int(k)

edge_list = []
edge_set = set()
for i in range(0, edges_num):
    node1, node2 = input().split()
    edge_list.append([node1, node2])
    #if node1 == '2' and node2 == '10':
    #    debug = 2
    node1 = int(node1)
    node2 = int(node2)
    if node1<node2:
        edge_set.add(tuple([node1, node2]))
    else:
        edge_set.add(tuple([node2, node1]))

#turn edge list into adjacency matrix
graph = {}

for i in range(0, len(edge_list)):

    if int(edge_list[i][0]) not in graph.keys():
        graph[int(edge_list[i][0])] = set()

    if int(edge_list[i][1]) not in graph.keys():
        graph[int(edge_list[i][1])] = set()

    graph[int(edge_list[i][0])].add(int(edge_list[i][1]))
    graph[int(edge_list[i][1])].add(int(edge_list[i][0]))

new_k = vertices_num - k

possible_edges_num = vertices_num*((vertices_num-1)/2)
new_edges = possible_edges_num - len(edge_list)
print(vertices_num, int(new_edges), new_k)

output_edges = []

for key in graph.keys():
    for key2 in graph.keys():
        if key != key2:
            #if key ==2 and key2 == 10:
            #    debug = 1
            if(key<key2):
                if tuple([key, key2]) not in edge_set:
                    output_edges.append([key, key2])
                    edge_set.add(tuple([key, key2]))
            else:
                if tuple([key2, key]) not in edge_set:
                    output_edges.append([key2, key])
                    edge_set.add(tuple([key2, key]))

output_edges.sort(key=lambda x: (x[0], x[1]))
#print(len(output_edges))
for i in range(0, len(output_edges)):
    print(str(output_edges[i][0]) + ' ' + str(output_edges[i][1]))






