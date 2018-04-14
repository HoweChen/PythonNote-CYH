class Stack(object):
    def __init__(self, value_list=None):
        self.stack = []
        if value_list:
            for item in value_list:
                self.push(item)

    def push(self, val=None):
        if val:
            self.stack.append(val)

    def pop(self):
        return self.stack.pop()


test = Stack()
test.push(1)
print(test.pop())
