"""Primary file for creating the application."""

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from textwrap import dedent


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

    
    def proof_of_work(self, last_proof):
        '''
        PoW algorithm that finds the proof p' such that hash(previous block) contains 4 leading zeros
        p is the previous proof and p' is the new proof
        
        Parameters:
        -----------
        last_proof: <int> 

        Return:
        -------
        <int>
        '''

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        '''
        Validates the proof > Does has(last_proof, proof) contain 4 leading 0's
        Parameters:
        -----------
        last_proof: <int> 
        proof: <int> current proof
        Return:
        -------
        <bool> the last 4 characters of the guess hash, True if hash contains the 4 leading 0's, false if not
        '''

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'


# Instatiate the Node
app = Flask(__name__)

# Generate globally unique address for the node and remove the '-'
node_identifier = str(uuid4()).replace('-','')


# Instantiate the Blockchain Class
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "Mining a new block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # validate all fields are in posted data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing Values", 400

    # create new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)