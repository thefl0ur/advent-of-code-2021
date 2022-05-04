Have to fix foolish mistake in original code to get correct answer.

Original solution performance:

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    10 |     95.8164 | 0:00:00.004284 |     95.8165 | 0:00:00.004467 |

Surprisingly, I already use list comprehansion in data reading. Bad for me, there is no need to have all data in memory.

