from helpers import read_data
from dive import DiveAim

dive = DiveAim(read_data('data/input.md'))
print(dive.calculcate_position())