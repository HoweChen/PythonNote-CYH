class Queue(object):
    def __init__(self, val_list=None):
        self.stack_one = []
        self.stack_two = []
        if val_list:
            for item in val_list:
                self.stack_one.append(item)

    def push(self, val=None):
        if val:
            self.stack_one.append(val)

    def pop(self):
        for index in range(0, len(self.stack_one)):
            self.stack_two.append(self.stack_one.pop())

        self.stack_two.pop()


def main():
    a = Queue()


if __name__ == '__main__':
    main()
