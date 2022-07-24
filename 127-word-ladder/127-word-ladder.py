from collections import defaultdict, Counter
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #This won't work because dfs doesn't guarentee to give shortest path
#         s = set()
#         d=defaultdict(list)
#         for i in wordList:
#             s.add(i)
#         if beginWord not in s:
#             s.add(beginWord)
#             count=1
#         else:
#             count=0
#         for i in s:
#             for j in wordList:
#                 if len(Counter(i)-Counter(j)) == 1:
#                     d[i].append(j)
        
#         def dfs(d,src,dest,counts,visited,count):
#             visited.add((src))
#             if src==dest:
#                 counts[dest]=min(counts[dest],count)
#                 return
#             for neigh in d[src]:
#                 if (neigh not in visited) or neigh==dest:
#                     count+=1
#                     dfs(d,neigh, dest,counts, visited,count)
#         visited = set()
#         counts = {}
#         counts[endWord]=10**6
#         dfs(d,beginWord,endWord, counts, visited, count)
#         return 0 if counts[endWord]==10**6 else counts[endWord]
        

        # BFS works here
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) 
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0