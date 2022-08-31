class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.data = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        index = self.map[val]
        last = self.data[-1]
        self.data[index],self.data[-1] = self.data[-1],self.data[index]
        self.data.pop()
        self.map[last] = index
        self.map.pop(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()