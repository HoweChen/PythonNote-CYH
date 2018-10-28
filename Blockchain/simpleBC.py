from datetime import datetime


class BlockChain(object):
    def __init__(self, block):


class Block(object):
    def __init__(self):
        self.head = None
        self.body = None
        self.is_packed = False

    def package_block(self, head, body):
        if not self.is_packed:
            self.head = head
            self.body = body
            self.is_packed = True
        return True


class Head(object):
    def __init__(self,version,time,hash,prev_hash):
        self.version = None
        self.time = datetime.date()
        self.hash = ""
        self.prev_hash = ""


class Body(object):
    def __init__(self, data=None):
        self.data = data


def generate_genises_block():


if __name__ == '__main__':
