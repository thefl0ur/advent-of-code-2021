Ok, I see my code and...

Part 1 is pretty easy and can be done by just reading puzzle description.
In short: Numbers 1, 4, 7 and 8 unique in terms of number of active segments.

Part 2 requires us to decode that segments to get final result

```
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```

On the start we have knowledge of all 10 numbers, but not sure what is what.

Algorithm is based on segments overlapping.

We already knew some numbers (1, 4, 7 and 8) and we hate to get lest and detect which number is which display segment. This is needed for detection more complex numbers.

We initialize segments with next data:
segment `a` - all from number 7 minus all from number 1. 
segment `b` - all from number 4 minus all from number 1. 
segment `c` - all from number 1
segment `d` - all from number 4 minus all from number 1. 
segment `e` - empty
segment `f` - all from number 1
segment `g` - empty

There are 6 numbers left, grouped by segments length.

We start with 5-segment group.

We can filter number 5 by validation that all from segments `b` and `d`.
After what we can confirm which segment in number 1 in charge for `c` and `f` segments

Next we find numbers 3 and 2. 
In number 3 no `f` segment and segment `c` is presented.
Number 2 is last from 5-segments group.

In remaining group we fan filter number 6 as number 8 minus segment `c`

Now we have to find segment `d` to detect remaining numbers.
We can find `d` as intersection of number 2 and what we think is `d`.
With it we can find 9 as 6-segment number with segment `d` and remaining number would by zero.

Tricky part of puzzle is over.

Performance:

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     8 |       41.72 | 0:00:00.001595 |      41.584 | 0:00:00.025164 |

