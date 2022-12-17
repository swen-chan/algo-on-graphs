#The first function is basically origin,but change the auguments.
def bipartite(s,color_arr):
    queue = [s]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if color_arr[v] == -1:
                color_arr[v] = 1 - col[u]
                queue.append(v)
            elif color_arr[v] == color_arr[u]:
                return False
    return True
#this function is to traveral every node,avoiding disconnected graph.
def ispartite(adj):
    color_arr = [-1] * len(adj)
    for i in range(len(adj)):
        if color_arr[i] == -1:
            if not bipartite(i, color_arr):
                return 0
    return 1
'''
    color_arr = [-1] * len(adj)
    color_arr[0] = 1
    queue = []
    queue.append(0)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if color_arr[v] == -1:
                color_arr[v] = 1 - color_arr[u]
                queue.append(v)
            elif color_arr[v] == color_arr[u]:
                return 0
    return 1
'''
if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, raw_input().split())
        # adjacency list		
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #change the function into print
    print(ispartite(adj))
    
