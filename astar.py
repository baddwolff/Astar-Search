import sys

def make_heu():
    h = {}
    with open("res.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    # print(h)
    return h

def shortest(que):
    min=float("inf")
    x=-1
    for i in range(len(que)):
        if que[i][1]<min:
            min=que[i][1]
            x=i

    print(que[x])
    temp=que[x][0]
    que.remove(que[x])
    return temp

def make_graph(file):
    graph = {}
    for line in file:
        v1, v2, w = line.split(',')
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return graph

def heuristic(node,h):
    return h[node]

def astar(graph, start, dest):
    que =[]
    h = make_heu()
    explored =set()
    que.append([[(start, 0)], 0])
    while len(que)>0:
        path = shortest(que)
        node = path[-1][0]
        g_cost = path[-1][1]
        explored.add(node)
        if node == dest:
            print(explored)
            return [x for x, y in path]
        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]
            que.append([new_path, f_cost])
    return False


with open('graph.txt', 'r') as file:
    lines = file.readlines()
# start = lines[1].strip()
# dest = lines[2].strip()
start=sys.argv[1]
dest =sys.argv[2]
graph = make_graph(lines[4:])
result=(astar(graph,start,dest))
print("Path Followed:")
for each in result:
    print '>',each,
