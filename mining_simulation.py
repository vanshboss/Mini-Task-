import hashlib
import time

# Define the Block class
class Block:
    def __init__(self, data, previous_hash):
        self.data = data                  # Block data (e.g., transactions)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0                    # Starts at 0 and is incremented to find a valid hash
        self.hash = self.calculate_hash() # Initial hash with nonce = 0

    # Calculate hash based on block content
    def calculate_hash(self):
        content = self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    # Mining function: adjust nonce until hash starts with a certain number of zeros
    def mine_block(self, difficulty):
        print(f"\n⛏️  Mining block with difficulty: {difficulty}")
        start_time = time.time()                     # Start the timer
        target = "0" * difficulty                    # e.g., '0000'

        while self.hash[:difficulty] != target:
            self.nonce += 1                          # Try next nonce
            self.hash = self.calculate_hash()        # Recalculate hash

        end_time = time.time()                       # Stop the timer

        # Final mined block details
        print(f" Block successfully mined!")
        print(f" Valid Hash     : {self.hash}")
        print(f" Nonce Used     : {self.nonce}")
        print(f" Time Taken     : {round(end_time - start_time, 4)} seconds")

# --- Main Simulation ---

# Create a block with dummy data and previous hash
block = Block("This is a test block", "0")

# Set mining difficulty (number of leading 0's in the hash)
difficulty = 4

# Start mining
block.mine_block(difficulty)
