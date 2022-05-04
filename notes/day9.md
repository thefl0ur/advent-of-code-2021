Whoa, part 2 was easy. All I have to do is implement [flood fill](https://en.wikipedia.org/wiki/Flood_fill)

Original performance:

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     9 |     106.563 | 0:00:00.030136 |     106.563 | 0:00:00.074847 |

## Part 1

I start refactoring with `read_data` method. Most obvious thing to change was removing useless list comprehension  - `[x for x in line.strip()]`, because string naturally is iterable.

Next I decide to move my matrix in separate class - this will give me access to class properties and I can remove simplify some things.

On this iteration of refactoring:
* change from `range` move to `enumerate`
* change inner loop, so i don't need extra access to matrix to get current value
* if value is 9 (border 9) - leave immediately
* insted of calculation `len` and checking border of matrix I move to `try...catch` - it's faster to recover. Checking values below 0 stays, because negative index is a thing.

Do some observation to discover that call of `all` is pretty slow.
I try next things to change that:
1. Pass list not generator into
2. Pass set
3. revert all to any in list
4. write custom function

| method             | TIME 1   |
|--------------------|----------|
| all with generator | 0.029892 |
| all with list      | 0.021671 |
| all with set       | 0.022610 |
| any with list      | 0.019256 |
| custom function    | 0.014237 |

I try to understand why this happening, but do not get it, just stick with my solution.

## Part 2

I start with almost the same code. In flooding function I can now remove `len` in border checking function and use `self`. Calculation of product stays same too.

For now performanse is next:
|   DAY |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|
|     9 |     106.715 | 0:00:00.111860 |

Lol, new approach is much slower. Dive in profiler

```
name                                  ncall  tsub      ttot      tavg      
..aoc/days/day9/solution.py:45 part2  1      0.000049  0.236516  0.236516
..solution.py:103 Heatmap.get_basins  1      0.001275  0.231968  0.231968
..day9/solution.py:110 Heatmap.flood  289..  0.127878  0.135449  0.000005
..n.py:71 Heatmap._get_lowest_points  1      0.056112  0.094748  0.094748
..y9/solution.py:65 Heatmap.is_lower  7185   0.009377  0.009377  0.000001
../days/day9/solution.py:8 read_data  1      0.000015  0.004454  0.004454
..ays/day9/solution.py:10 <listcomp>  1      0.002986  0.003174  0.003174
..y9/solution.py:58 Heatmap.__init__  1      0.000008  0.000011  0.000011
```
Calls for `flood` takes more than half of time. Go deeper with `line_profiler`

```
Line #  Hits      Time   Per Hit  % Time  Line Contents
==============================================================
 111    28964    24088.0   0.8      11.0   x, y = position
 112                                                      
 113                                       # map border check
 114    28964    33510.0   1.2      15.3   if x < 0 or x > self.max_x or y < 0 or y > self.max_y:
 116      309      182.0   0.6       0.1       return
 117                                                          
 118    28655    28449.0   1.0      12.9   if self.matrix[x][y] == 9:
 119     7353     4683.0   0.6       2.1       return
 120                                                          
 121    21302    40505.0   1.9      18.4   if position in stack:
 122    14117     9216.0   0.7       4.2       return
 123                                       else:
 124     7185     7792.0   1.1       3.5       stack.append(position)
 125                                                          
 126     7185    17766.0   2.5       8.1   self.flood((x, y+1), stack)
 127     7185    17803.0   2.5       8.1   self.flood((x+1, y), stack)
 128     7185    17863.0   2.5       8.1   self.flood((x, y-1), stack)
 129     7185    17878.0   2.5       8.1   self.flood((x-1, y), stack)
```

 Try to use already approved thing:
* try ... catch for getting border value
* check border only for negative indexes 

|   DAY |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|
|     9 |     106.715 | 0:00:00.065216 |

Bam! We finally faster than original solution was. And... that all! I didn't find way to improve solution.

## Summary

| Solution |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|----------|-------------|----------------|-------------|----------------|
| Original |     106.563 | 0:00:00.030136 |     106.563 | 0:00:00.074847 |
| Refactor |     106.714 | 0:00:00.016284 |     106.714 | 0:00:00.058577 |

Part 1 improved on 46% and part 2 on 22% in term of execution time. Memory consumption stay almost same, so no calculations was made.