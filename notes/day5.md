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