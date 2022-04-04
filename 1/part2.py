from helpers import read_data
from sonar_sweep import SonarSweep

sonar = SonarSweep(read_data('data/input.md'), 3)
print(sonar.get_increments_count())
