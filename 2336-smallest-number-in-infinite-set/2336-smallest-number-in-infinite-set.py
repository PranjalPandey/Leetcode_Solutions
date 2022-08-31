class SmallestInfiniteSet:

    def __init__(self):
        self.index = 1
        self.heap = []
        self.s = set()
        

    def popSmallest(self) -> int:
        if self.heap:
            smallest = self.heap[0]
            self.s.remove(smallest)
            heapq.heappop(self.heap)
            return smallest
        self.index += 1
        return self.index-1
        

    def addBack(self, num: int) -> None:
        if num<self.index and num not in self.s:
            self.s.add(num)
            heapq.heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)