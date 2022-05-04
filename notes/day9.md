Whoa, part 2 was easy. All I have to do is implement [flood fill](https://en.wikipedia.org/wiki/Flood_fill)

Original performance:

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     9 |     106.563 | 0:00:00.030136 |     106.563 | 0:00:00.074847 |

I start refactoring with `read_data` method. Most obvious thing to change was removing useless list comprehension  - `[x for x in line.strip()]`, because string naturally is iterable.

Next I decide to move my matrix in separate class - this will give me access to class properties and I can remove simplify some things.

On this iteration iteration of refactoring:
* from `range` move to `enumerate`
* change inner loop, so i don't need extra access to matrix to get current value
* if value is 9 (border 9) - leave immediately
* instaed of calculation `len` and checking border of matrix I move to `try...catch` - it's faster to recover. Checking values below 0 stays, because negative index is a thing

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     9 |     106.755 | 0:00:00.028503 |     106.714 | 0:00:00.029892 |

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