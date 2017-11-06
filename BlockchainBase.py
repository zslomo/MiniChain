from abc import ABCMeta, abstractmethod

# 区块链基类
__author__ = "Bin Tan"
__date__ = "2017.11.6"

class BlockchainBase(metaclass=ABCMeta):


    @abstractmethod
    def new_block(self):
        # 创建一个新的块并将其添加到链中
        pass

    @abstractmethod
    def new_transaction(self):
        # 将新的交易添加到交易列表
        pass


    @staticmethod
    def hash(block):
        # 创建块hash
        pass

    @abstractmethod
    def proof_of_work(self, last_proof):
        # pow工作证明
        pass

    @abstractmethod
    def valid_proof(last_proof, proof):
        #验证工作证明
        pass

    @property
    def last_block(self):
        # 返回链中的最后一个块
        pass

