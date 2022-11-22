from src.entities.blockchain import Blockchain
from src import mine

from src.net.server import *


# Build blockchain from genesis

# Create an instance of the blockchain
b = Blockchain()

# Mine the genesis block
gensis = mine()

# Connect to the network

# Start Application