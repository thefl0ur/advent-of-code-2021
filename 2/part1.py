from helpers import read_data
from dive import Dive

dive = Dive(read_data('data/input.md'))
print(dive.calculcate_position())