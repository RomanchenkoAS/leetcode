from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        remove_index = self.dict[val]
        last_element = self.list[-1]
        if remove_index != len(self.list):
            self.list[-1], self.list[remove_index] = self.list[remove_index], self.list[-1]
            self.dict[last_element] = remove_index
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
