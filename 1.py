


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

'''for key in graph:
    contact_list = []
    for elem in graph[key]:
        contact_list.append(elem)
        for elem2 in graph[elem]:
            contact_list.append(elem2)

    if len(contact_list) > max_num:
        max_num = len(contact_list)
'''

for key in graph:
    contact_set = set()
    '''for elem in graph[key]:
        contact_set.add(tuple([key, elem]))'''

    for elem in graph[key]:
        if tuple([elem,key]) not in contact_set:
            contact_set.add(tuple([key, elem]))
        for elem2 in graph[key]:
            if tuple([elem2, elem]) not in contact_set and elem2 != elem:
                contact_set.add(tuple([elem, elem2]))

    if len(contact_set) > max_num:
        max_num = len(contact_set)

print(max_num)