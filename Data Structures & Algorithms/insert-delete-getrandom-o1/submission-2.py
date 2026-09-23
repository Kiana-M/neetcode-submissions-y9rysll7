class RandomizedSet:

    def __init__(self):
        self.vals={}
        self.lst = []       

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        else:
            self.lst.append(val)
            self.vals[val] = len(self.lst)-1
            return True  

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        last_ind = len(self.lst)-1
        val_ind = self.vals[val]
        self.vals[self.lst[last_ind]] = val_ind
        self.lst[val_ind], self.lst[last_ind] = self.lst[last_ind], self.lst[val_ind]
        self.lst.pop()
        self.vals.pop(val)
        return True

    def getRandom(self) -> int:
        rand_int = random.randrange(len(self.lst))
        return self.lst[rand_int]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()