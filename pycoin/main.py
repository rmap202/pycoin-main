from src.entities.blockchain import Blockchain
from src import mine

from src.net.server import *


# Build blockchain from genesis

b = Blockchain()

res = mine()

# Connect to the network

# Start Application