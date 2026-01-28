import random
class RandomizedSet:

    def __init__(self):
        self.dic = dict()
        self.arr = []

    def insert(self, val: int) -> bool:
        
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            idx = len(self.arr)-1
            self.dic[val] = idx
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        idx, last = self.dic[val], self.arr[-1]

        self.arr[idx], self.dic[last] = last, idx

        self.arr.pop()
        self.dic.pop(val)

        return True
        
    def getRandom(self) -> int:
        hold = random.choice(self.arr)


        return hold

        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()

ss = set()
ss.add(1)
ss.add(10)
ss.add(100)
ss.add(100)

print(ss)
if 10 in ss:
    ss
    print("aa")