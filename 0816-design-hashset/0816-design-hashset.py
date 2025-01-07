class MyHashSet:
    # brute force solution
    # def __init__(self):
    #     self.keys = list()
    #     # values = []

    # def add(self, key: int) -> None:
    #     if key not in self.keys:
    #         self.keys.append(key)

    # def remove(self, key: int) -> None:
    #     if key in self.keys:
    #         self.keys.remove(key)

    # def contains(self, key: int) -> bool:
    #     if key in self.keys:
    #         return True
    #     return False

    # solution 2
    def __init__(self):
        self.Len = pow(10,6)
        self.keys = [None for i in range(0, self.Len)]
        # values = []

    def add(self, key: int) -> None:
        if key != self.keys[key%self.Len]:
            self.keys[key%self.Len] = key


    def remove(self, key: int) -> None:
        if key ==  self.keys[key%self.Len]:
            self.keys[key%self.Len] = None

    def contains(self, key: int) -> bool:
        if key ==  self.keys[key%self.Len]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)