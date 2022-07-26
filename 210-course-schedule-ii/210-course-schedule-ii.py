class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1->0,2->0,3->[1,2]
        g = defaultdict(list)
        ans = []
        visited, cycle = set(), set()
        for p in prerequisites:
            g[p[0]].append(p[1])
            
        def topological_sort(graph,visited,src,ans, cycle):
            if src in visited:
                return True
            if src in cycle:
                return False
            cycle.add(src)
            for i in graph[src]:
                if topological_sort(graph,visited,i,ans, cycle)==False:
                    return False
            cycle.remove(src)
            visited.add(src)
            ans.append(src)
            return True
        for course in range(numCourses):
            if topological_sort(g,visited,course,ans, cycle) ==False:
                return []
        
        return ans
            
        
                