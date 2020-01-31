import hashlib
import datetime


class Transaction:
    # each block has 7 attributes
    # 1 number of the block
    transactionNo = 0
    # 2 what data is stored in this block?
    data = None
    # 3 pointer to the next block
    next = None
    # 4 The hash of this block (serves as a unique ID and verifies its integrity)
    # A hash is a function that converts data into a number within a certain range.
    hash = None
    # 5 A nonce is a number only used once
    nonce = 0
    # 6 store the hash (ID) of the previous block in the chain
    previous_hash = 0x0
    # 7 timestamp
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data
        self.approved = 0

        # Function to compute 'hash' of a block
        # a hash acts as both a unique identifier
        # & verifies its integrity
        # if someone changes the hash of a block
        # every block that comes after it is changed
        # this helps make a blockchain immutable

    def hash(self):
        # SHA-256 is a hashing algorithm that
        # generates an almost-unique 256-bit signature that represents
        # some piece of text
        h = hashlib.sha256()
        # the input to the SHA-256 algorithm
        # will be a concatenated string
        # consisting of 5 block attributes
        # the nonce, data, previous hash, timestamp, & block #
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.transactionNo).encode('utf-8')
        )
        # returns a hexademical string
        return h.hexdigest()

    def set_approval(self, status):
        self.approved = status

    def get_approval(self):
        return self.approved

    def __str__(self):
        # print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.transactionNo) + "\nBlock Data: " + str(
            self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


class TransactionChain:
    # mining difficulty
    diff = 20
    # 2^32. This is the maximum number
    # we can store in a 32-bit number
    maxNonce = 2 ** 32
    # target hash, for mining
    target = 2 ** (256 - diff)

    # generates the first block in the blockchain
    # this is called the 'genesis block'
    transaction = Transaction("Root")
    # sets it as the head of our blockchain
    head = transaction

    # adds a given block to the chain of blocks
    # the block to be added is the only parameter
    def add(self, transaction):

        # set the hash of a given block
        # as our new block's previous hash
        transaction.previous_hash = self.transaction.hash()
        # set the block # of our new block
        # as the given block's # + 1, since
        # its next in the chain
        transaction.transactionNo = self.transaction.transactionNo + 1

        # set the next block equal to
        # itself. This is the new head
        # of the blockchain
        self.transaction.next = transaction
        self.transaction = self.transaction.next

    # Determines whether or not we can add a given block to
    # the blockchain
    def mine(self, transaction):
        # from 0 to 2^32
        for n in range(self.maxNonce):
            # is the value of the given block's hash less than our target value?
            if int(transaction.hash(), 16) <= self.target:
                # if it is,
                # add the block to the chain
                self.add(transaction)
                transaction.set_approval(1)
                print(transaction)
                break
            else:
                transaction.nonce += 1

    @staticmethod
    def print_status(self):
        for i in range(0, TransactionChain.block_chain_len()):
            print(TransactionChain.head)

    @staticmethod
    def block_chain_len():
        current_block = TransactionChain()
        block_length = 0
        while current_block.head is not None:
            block_length += 1
        return block_length
