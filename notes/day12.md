This puzzle is graph-based, and have zero experience of working with them. Not touch it even in university.
I remember what most part of code I get from internet.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    12 |     649.409 | 0:00:00.037005 |     19065.1 | 0:00:18.685921 |

Part 2 is ridiculous slow, so I guess I have to understand graphs and move even from brute force solution.

First, I decide to compare my solution with other peoples, to find ot how bad I am
Compare with some other peoples solutions, available on github
https://github.com/AkaruiYami/AdventOfCode/blob/main/AOC-2021/D12/main.py
                      
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    12 |      11.073 | 0:00:00.058557 |      14.117 | 0:00:01.234518 |

https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2021/d12_paths_through_caves_bfs_adjacency_dict_networkx/cave_navigating_graph.py

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    12 |     976.913 | 0:00:00.104902 |     36151.9 | 0:00:02.625312 |

https://github.com/Akumatic/Advent-of-Code/blob/master/2021/12/code.py

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    12 |     838.234 | 0:00:00.034801 |       24223 | 0:00:05.670509 |


And I was very bad.
So I take a break.

Next, I try to read a little bit about graphs and staff and left again.
One day I just come to work and before working hour write my new solution in just 5 minutes.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    12 |      15.178 | 0:00:00.032622 |      15.178 | 0:00:00.804268 |
