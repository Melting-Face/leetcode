class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 0
        self.length = n
        self.order_dict = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.order_dict[idKey-1] = value
        return_list = []
        if idKey == self.ptr + 1:
            for idx in range(self.ptr, self.length):
                rst = self.order_dict.get(idx, None)
                if rst is None:
                    self.ptr = idx
                    break
                return_list.append(rst)
            return return_list
        else:
            return return_list


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)