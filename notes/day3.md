### Part 1
Do same routine for day 3 solution.
Nothing interesting here, but I got better understanding of handling bits in python.
Let me explain.

```
>>> print(int('101', 2))
5
```

What if we invert our variable? I bet you expect '010' (2 dec)?
Nope.
```
>>>  print(~int('101', 2))
-6
```

Short explain: generated int have much more then 3 bits, and all of them inverts.
For x32 our int variable will be represented as `0000 0000 0000 0000 0000 0000 0000 0101`

For detailed: check out [this](https://en.wikipedia.org/wiki/Two%27s_complement).

So I just use [bitarray](https://pypi.org/project/bitarray/) to get expected behavior.

In later days (spoiler!) I discover `Counter` from `collections`. I find it useful for calculations there.

Combining previous knowledge and technics I get next results: 2x memory usage improvements and ~75% speed boost.

| Solution |   MEM, Kb   | TIME           |
|----------|-------------|----------------|
| Original |     176.087 | 0:00:00.008895 |
| Improved |     83.5794 | 0:00:00.002165 |

Memory and speed improves almost only due the fact I decide to not operate on transformed matrix.
Using bitarray library is mostly a choose of convenience.

### Part 2
Nothing really interesting here, just improvements.

| Solution |   MEM 2, Kb | TIME 2         |
|----------|-------------|----------------|
| Original |       336.9 | 0:00:00.024874 |
| Refactor |     206.535 | 0:00:00.006348 |

Memory usage was improved by 40%, and time improvement was 75%.

There is al least one thing to improve left: in part 2 we can refuse from creating `tmp` list with filtered data
and use indexes instead. From first attempt i can't do it, so may be i return to this later. 