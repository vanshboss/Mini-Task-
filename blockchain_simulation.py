import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.get_hash()

    def get_hash(self):
        info = self.data + self.previous_hash
        return hashlib.sha256(info.encode()).hexdigest()

# Create 3 blocks
block1 = Block("I am Block 1", "0")
block2 = Block("I am Block 2", block1.hash)
block3 = Block("I am Block 3", block2.hash)

#  Tamper with Block 1
block1.data = "Hacked Block 1"
block1.hash = block1.get_hash()

# Show blocks
for block in [block1, block2, block3]:
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("My Hash:", block.hash)
    print("-" * 40)
