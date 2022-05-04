Have to fix foolish mistake in original code to get correct answer.

Original solution performance:

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    10 |     95.8164 | 0:00:00.004284 |     95.8165 | 0:00:00.004467 |

Surprisingly, I already use list comprehension in data reading. Bad for me, there is no need to have all data in memory.

## Part 1

Start with changing `range(len(line))` to simple iteration on line. This opens us a way to removing index-based access to values.

Change work with input data - now only one line is loaded in time.
Instead of direct compare symbols I choose a little bit more advanced solution - by comparing ASCII codes.

At some point I discover that I use Python 3.9.0 and I have access to walrus operator `:=`. This simplifies my code a lot.

|   DAY |   MEM 1, Kb | TIME 1         |
|-------|-------------|----------------|
|    10 |     21.6143 | 0:00:00.003030 |