import random

class RandomizedSet:

    def __init__(self):
        self.total_dict = {}

    def insert(self, val: int) -> bool:
        val_in_dict = val in self.total_dict
        if val_in_dict is False:
            self.total_dict[val] = val
        return not val_in_dict

    def remove(self, val: int) -> bool:
        val_in_dict = val in self.total_dict
        if val_in_dict is True:
            self.total_dict.pop(val, None)
        return val_in_dict

    def getRandom(self) -> int:
        return random.choice(list(self.total_dict.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()