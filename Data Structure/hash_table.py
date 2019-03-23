# only for method 2
class LinkedList:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None


class MyHashMap:
     # method 1: use list, too expensive
    #     def __init__(self):
    #         """
    #         Initialize your data structure here.
    #         """
    #         self.capacity = 1000000
    #         self.key = [None for _ in range(self.capacity)]
    #         self.value = [None for _ in range(self.capacity)]

    #     def put(self, key: int, value: int) -> None:
    #         """
    #         value will always be non-negative.
    #         """
    #         self.key[key] = key
    #         self.value[key] = value

    #     def get(self, key: int) -> int:
    #         """
    #         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    #         """
    #         value = self.value[key]
    #         if value is not None:
    #             return value
    #         else:
    #             return -1

    #     def remove(self, key: int) -> None:
    #         """
    #         Removes the mapping of the specified value key if this map contains a mapping for the key
    #         """
    #         self.key[key] = None
    #         self.value[key] = None

    # method 2 use Linked list

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        # the reason why chose 1000 is that the maximum number of range is 1m
        self.list = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.capacity

        if self.list[index] is None:
            self.list[index] = LinkedList(key, value)
        else:
            ptr = self.list[index]
            while ptr.next is not None and ptr.pair[0] != key:
                ptr = ptr.next
            if ptr.pair[0] == key:
                ptr.pair = (key, value)
            else:
                tmp = LinkedList(key, value)
                ptr.next = tmp

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.capacity

        ptr = self.list[index]
        while ptr is not None:
            if ptr.pair[0] == key:
                return ptr.pair[1]
            else:
                ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # 这里需要单向删除单向链表的某一个元素。需要将上一个链表的next，指向当前链表的next
        index = key % self.capacity
        if self.list[index] is not None:
            ptr = self.list[index]
            next_ptr = ptr.next
            if ptr.pair[0] == key:  # 比较第一个链表
                self.list[index] = next_ptr
            else:
                while next_ptr is not None:
                    stored_index, sotred_value = next_ptr.pair
                    if stored_index == key:
                        ptr.next = next_ptr.next
                        del(next_ptr)
                        break
                    next_ptr = next_ptr.next
                    ptr = ptr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
