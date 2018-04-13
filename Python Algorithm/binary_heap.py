import create_random_number_list
import random


class Node:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def show_node_info(self):
        print(self.val, self.left.val, self.right.val)


class Heap:
    def __init__(self, heapify_list=None):
        self.heap_dict = {}
        if heapify_list:
            self.heap_list = []
            list_length = len(heapify_list)
            # let all element in the temp_list transfer into node
            for element in heapify_list:
                self.heap_list.append(Node(val=element))
            if (list_length - 1) % 2 == 0:
                heapify_range = (list_length - 1) // 2 - 1
            else:
                heapify_range = (list_length - 1) // 2

            for index in range(heapify_range + 1):
                print(index * 2 + 2, list_length)
                if index * 2 + 2 >= list_length:
                    self.heap_list[index].left = self.heap_list[index * 2 + 1]
                    self.heap_list[index * 2 + 1].parent = self.heap_list[index]
                else:
                    self.heap_list[index].left = self.heap_list[index * 2 + 1]
                    self.heap_list[index].right = self.heap_list[index * 2 + 2]
                    self.heap_list[index * 2 + 1].parent = self.heap_list[index]
                    self.heap_list[index * 2 + 2].parent = self.heap_list[index]
                self.heap_dict[index] = self.heap_list[index]
            for index in range(heapify_range + 1, list_length):
                self.heap_dict[index] = self.heap_list[index]

    def __getitem__(self, item):
        return self.heap_dict[item]

    def push(self, val):
        pass

    def show_heap_info(self):
        for item in self.heap_dict.values():
            if not item.left or not item.right:
                print(item.val)
            else:
                print(item.val, item.left.val, item.right.val)
def main():
    # rand_num_list = create_random_number_list.main()
    # random.shuffle(rand_num_list)
    rand_num_list = list(range(14))
    sol = Heap(rand_num_list)
    sol.heap_dict


if __name__ == '__main__':
    main()
