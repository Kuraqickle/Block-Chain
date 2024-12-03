class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    # creates a new block and adds it to the chain
    def new_block(self):
        pass

    # adds a new transaction to the list of transaction
    def new_transaction(self):
        pass

    # hashes a block
    @staticmethod
    def hash(block):
        pass

    # returns the last block in the chain
    @property
    def last_block(self):
        pass