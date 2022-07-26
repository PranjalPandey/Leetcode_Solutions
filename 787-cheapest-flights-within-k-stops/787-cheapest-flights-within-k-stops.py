class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

#DFS with Prunning
#         graph = defaultdict(dict)
        
#         for s,d,p in flights:
#             graph[s][d]=p

#         visited = set()
#         def dfs_with_pruning(graph,src,dest,total,k):
#             nonlocal fare
#             if k<-1:
#                 return 
#             if src==dest:
#                 fare = min(fare,total)
#                 return
#             visited.add(src)
#             for neigh in graph[src]:
#                 if neigh not in visited and (total+graph[src][neigh]<=fare):
#                     dfs_with_pruning(graph,neigh,dest,total+graph[src][neigh],k-1)
#             visited.remove(src)
            
#         fare = 10**9
#         dfs_with_pruning(graph,src,dst,0,k)
#         if fare==10**9:
#             return -1
#         return fare

# Bellman Ford
        # prices = [float("inf")]*n
        # prices[src] = 0
        # for node in range(k+1):
        #     temp = prices.copy()
        #     for s,d,p in flights:
        #         if prices[s] == float("inf"):
        #             continue
        #         if prices[s]+p<temp[d]:
        #             temp[d] = prices[s]+p
        #     prices = temp
        # return -1 if prices[dst]==float("inf") else prices[dst]
        
#Dijkstra algorithm
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1
                    


        