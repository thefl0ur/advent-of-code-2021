Fist I measure timings for my original solution, which, in fact, works good.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    13 |     19940.7 | 0:00:00.567186 |     19940.7 | 0:00:00.780367 |

But memory usage was too big, code code was strange and I decide to optimize it.
Instead of manipulating matrices I operate only indexes on formula `2*center - position` to find reflected point.
It works good for memory but was really slow. Event after more optimizations.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    13 |     10201.7 | 0:00:00.247939 |     10201.9 | 0:00:02.165182 |

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    13 |     10201.7 | 0:00:00.210287 |     10201.9 | 0:00:01.201718 |

So I decide not to operate on 2d matrix - I really need only informational points, which are provided.
Looks like it was right decision, memory and speed improves dramatically.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    13 |     154.148 | 0:00:00.002967 |     154.148 | 0:00:00.007769 |

I make a lippy changes in types and way of data reading - lose some memory but get speed.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    13 |     159.027 | 0:00:00.002591 |     159.027 | 0:00:00.006378 |

After that point I do not found oblivious parts for optimization.
