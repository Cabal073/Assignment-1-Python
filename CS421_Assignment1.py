import math

def overlaps(c1, c2):
    # Return True if circle c1 overlaps or touches circle c2.
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    # Distance between the two centers
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # They overlap if that distance is at most the sum of the radii
    return dist <= r1 + r2

def build_graph(circles):
    # Return adjacency list: graph[i] = list of circles overlapping circle i.
    n = len(circles)
    graph = [[] for _ in range(n)]   # one empty list per circle
    for i in range(n):
        for j in range(i + 1, n):    # check each pair only once
            if overlaps(circles[i], circles[j]):
                graph[i].append(j)
                graph[j].append(i)   # overlap is two-way
    return graph

def is_cluster(circles):
    # Return True if all circles form a single cluster.
    n = len(circles)
    if n == 0:
        return False
    if n == 1:
        return True

    graph = build_graph(circles)

    # Visit circles starting from circle 0
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 0

    while stack:
        u = stack.pop()          # take a circle off the stack
        count += 1
        for v in graph[u]:       # look at everything it touches
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    # One cluster only if we reached every circle
    return count == n

# ============================================
# TEST CASES
# ============================================

test1 = [(1.0, 3.0, 0.7), (2.0, 3.0, 0.4), (3.0, 3.0, 0.9)]
print(is_cluster(test1))

test2 = [(1.5, 1.5, 1.3), (4.0, 4.0, 0.7)]
print(is_cluster(test2))

test3 = [(0.5, 0.5, 0.5), (1.5, 1.5, 1.1), (0.7, 0.7, 0.4), (4.0, 4.0, 0.7)]
print(is_cluster(test3))

test4 = [(0.0, 0.0, 1.0), (1.5, 0.0, 1.0), (5.0, 0.0, 1.0), (6.5, 0.0, 1.0)]
print(is_cluster(test4))
