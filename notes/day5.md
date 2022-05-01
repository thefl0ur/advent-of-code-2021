Start with reviewing what was done.
I print generated map and compare it with provided in puzzle description/ Looks like I screwed in index somewhere.

```
    Exception:                Reality
    
. . . . . . . 1 . .     . . . . . . . . . 2
. . 1 . . . . 1 . .     . . . . 1 . . . . 2
. . 1 . . . . 1 . .     . 1 1 . 1 . . . . 2
. . . . . . . 1 . .     . . . . 2 . . . . 1
. 1 1 2 1 1 1 2 1 1     . . . . 1 . . . . 1
. . . . . . . . . .     . . . . 1 . . . . 1
. . . . . . . . . .     . . . . 1 . . . . .
. . . . . . . . . .     1 1 1 1 2 . . . . .
. . . . . . . . . .     . . . . 1 . . . . .
2 2 2 1 1 1 . . . .     . . . . 1 . . . . .
```

Being to lazy to properly fix this issue, so I just swap x and y in `get_all_points` method on `Line`,
I go correct map and start searching for issue. I found pretty fast that diagonals was the problem.

Original code in `get_all_points` doesn't work correct with lines where one part of first coordinate was lower
than second. So slightly change generator - and viola! Map was generated absolutely correct.

Last change to obtain answer for part 2 was removing test in `else` block while obtaining points for map.

Performance test for original solution

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     5 |     13141.9 | 0:00:00.280611 |     18276.2 | 0:00:00.329590 |

Code was so general than I easily split it in functions. So small change and so big impact :(

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     5 |       13142 | 0:00:00.353127 |     18276.4 | 0:00:00.435212 |

Looking through profiler I find slowest parts of code:
`get_intersections`, `build_map`, `get_lines_points` and `read_data`.

First, I change map - i go to work with integer values only, so later I can use arithmetics in calculation and drop type checking.

Next, I replace my summing loop with sweet combination of `sum`, `len` and `filter` over list comprehension. 
Instead of using `lambda` in `filter` I move that login into local function in case of small speed improvement.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     5 |     13151.7 | 0:00:00.230683 |     18286.2 | 0:00:00.272033 |

Tired of joke when x as actual y and visa verse. Find and fix this.
Slightly simplify finding `max_x` and `max_y`.
Refactor `get_all_points` method. Don't think it give any significant impact on performance.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     5 |     13151.8 | 0:00:00.235130 |     18286.3 | 0:00:00.274364 |
