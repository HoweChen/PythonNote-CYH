from datetime import datetime

class BlockChain(object):
    def __init__(self, block):


class Block(object):
    def __init__(self):
        self.head = Head
        self.body = Body
        self.is_packed = False

    def package_block(self,head,body):
        if not self.is_packed:
            self.head = head
            self.body = body
            self.is_packed=True
        return True



class Head(object):
    def __init__(self):
        self.version = None

class Body(object):
    pass

def generate_genises_block():


if __name__ == '__main__':
