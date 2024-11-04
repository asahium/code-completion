import heapq

def prims_minimum_spanning(graph_used):
    vis=[]
    heap=[[0,1]]
    prim = set()
    mincost=0

    while len(heap) > 0:
        cost, node = heapq.heappop(heap)
        if node in vis:
            continue

        mincost += cost
        prim.add(node)
        vis.append(node)

        for distance, adjacent in graph_used[node]:
            if adjacent not in vis:
                heapq.heappush(heap, [distance, adjacent])

    return mincost
