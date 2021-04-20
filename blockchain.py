"""Primary file for creating the application."""

import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        '''create an empty list to store the blockchain'''
        self.chain = []
        self.current_transactions = []

        # create a genesis block 
        self.new_block(previous_hash=1, proof=100)


    def new_block(self, proof, previous_hash):
        '''
        create a new block and add it to a chain
        
        Parameters:
        -----------
        proof: <int> The proof given by proof of work algorithm
        previous_hash: <str> optional hash of previous block

        Return:
        -------
        <dict> New Block  
        '''
        block = {
            'index':len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block


    def new_transaction(self, sender, recipient, amount):
        '''
        Store transactions on the block
        
        Parameters:
        -----------
        sender: <str> Address of the sender
        recipient:  <str> address of person receiving the amount
        amount: <int> value of the transaction 
        
        Return:
        -------
        <int> the index of the block that holds the current transaction
        '''
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    
    @staticmethod
    def hash(block):
        '''
        Hashes the block with SHA-256
        
        Parameters:
        -----------
        block: <dict> dictionary of the full block  
        
        Returns:
        --------
        <str> Output of the hash function
        '''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    

    @property
    def last_block(self):
        '''returns the last block in the chain'''
        return self.chain[-1]
