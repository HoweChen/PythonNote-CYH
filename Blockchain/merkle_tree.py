import hashlib


# from collections import deque


class MT(object):
    def __init__(self, input_data=None):
        # self.root = Node()  # for now the root node is a node without data but with two sons

        if input_data:
            tmp_nodeStack = []
            data_length = len(input_data)
            for data in test_case:
                print(data)
                tmp_node = Node(content=data, type="SINGLE")
                tmp_node.son = data
                tmp_nodeStack.append(tmp_node)
        while (len(tmp_nodeStack) != 1):
            print(tmp_nodeStack)
            self.merkle_up(tmp_nodeStack)
        self.root = tmp_node

    def merkle_up(self, tmp_nodeStack):
        tmp_nodeStack_bkp = tmp_nodeStack[:]
        tmp_nodeStack.clear()
        for i in range(0, len(tmp_nodeStack_bkp), 2):
            if i != len(tmp_nodeStack_bkp) - 1:
                left = tmp_nodeStack_bkp[i]
                right = tmp_nodeStack_bkp[i + 1]
                tmp_node = Node()
                tmp_node.left_son = left
                tmp_node.right_son = right
                if
                tmp_node.value = hashlib.sha256((tmp_node.left_son.value + tmp_node.right_son.value)).hexdigest()

            else:
                son = tmp_nodeStack_bkp[i]
                tmp_node = Node(type="SINGLE")
                tmp_node.son = son
                tmp_node.value = hashlib.sha256(tmp_node.son.value).hexdigest()
        tmp_nodeStack.append(tmp_node)


class Node(object):
    def __init__(self, content=None, type="DOUBLE"):
        self.value = content
        self.father = None
        self.type = type
        if self.type == "DOUBLE":
            self.left_son = None
            self.right_son = None
        elif self.type == "SINGLE":
            self.son = None


if __name__ == '__main__':
    test_case = ["a", "b", "c", "d", "e"]
    for i in range(0, len(test_case)):
        test_case[i] = hashlib.sha256(test_case[i].encode()).hexdigest()
    # print(test_case)
    merkle_tree = MT(test_case)
    print(merkle_tree.root)
