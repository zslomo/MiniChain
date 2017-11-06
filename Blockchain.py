from BlockchainBase import BlockchainBase as bcb
import hashlib
import json
from time import time

#区块链实现类

__author__ = "Bin Tan"
__date__ = "2017.11.6"


class BlockChain(bcb):

    def __init__(self):
        self.chain = [{
            'index': 1,
            'timestamp': time(),
            'transactions': '',
            'proof': 0,
            'previous_hash': '',
        }]
        self.current_transactions = []

    def new_transaction(self, sender, recipient, amount):
        """
        创建新的交易
        :param sender: <str> 发送者地址
        :param recipient: <str> 接受者地址
        :param amount: <int> 数量
        :return: <int> 包含此交易的区块
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1


    def new_block(self, proof, previous_hash=None):
        """
        创建新的区块
        :param proof: <int> pow算法给出的证明
        :param previous_hash: (Optional) <str> 父块hash
        :return: <dict> 新的区块
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # 重置当前的交易列表
        self.current_transactions = []

        self.chain.append(block)
        return block




    @property
    def last_block(self):
        return self.chain[-1]


    @staticmethod
    def hash(block):
        """
        创建块的SHA-256
        :param block: <dict> 区块
        :return: <str> hash值
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        pow简单实例:
         - 查找一个 p' 使得 hash(pp') 以4个0开头
         - p 是上一个块的证明,  p' 是当前的证明
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        验证：hash(last_proof，proof)是否前四位都是0？

        :param last_proof: <int> 上一次的证明
        :param proof: <int> 当前证明
        :return: <bool> 正确与否.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
