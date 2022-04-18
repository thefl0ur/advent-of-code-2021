Ok, I managed to solve puzzle correctly, but can I make it *better*?

### Profiling and Optimization

I run performance test 1000 times and get next result:
```                          
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |      84.544 | 0:00:00.006826 |      84.544 | 0:00:00.006724 |
```
LGTM, but what is happening under the hood? Runs [yappi](https://github.com/sumerc/yappi) profiler via my cli.

```
name                                  ncall  tsub      ttot      tavg      
../aoc/days/day1/solution.py:5 part1  1      0.000037  0.034306  0.034306
..33 SonarSweep.get_increments_count  1      0.008379  0.023224  0.023224
..c/days/day1/helpers.py:4 read_data  1      0.004621  0.011042  0.011042
..0 SonarSweep._get_next_window_pair  2000   0.007953  0.010076  0.000005
..ar_sweep.py:12 SonarSweep.__init__  1      0.000003  0.000003  0.000003
```

Almost 1/3 of execution time is used for reading input.
Make `read_data` a little bit prettier - instead of manually filling `data` list, uses list comprehension (oh, I still can't memorize this phrase).

```
def read_data(file_name: str) -> List[int]:
    with open(file_name, 'r') as file:
        return [int(line) for line in file]
```

Now, go to profiler
```
../aoc/days/day1/solution.py:5 part1  1      0.000048  0.024180  0.024180
..33 SonarSweep.get_increments_count  1      0.007847  0.021532  0.021532
..0 SonarSweep._get_next_window_pair  2000   0.007308  0.009336  0.000005
..c/days/day1/helpers.py:4 read_data  1      0.000017  0.002597  0.002597
../days/day1/helpers.py:6 <listcomp>  1      0.001396  0.001476  0.001476
..ar_sweep.py:12 SonarSweep.__init__  1      0.000003  0.000003  0.000003
```

Wow, looks like we got HUGE improvement! Let's run benchmark on it!

```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |       84.68 | 0:00:00.006682 |       84.68 | 0:00:00.006894 |
```

Well, that change not really have impact on performance.
As wise man says: optimize things what runs thousand times, but not ones. 
Im my case the thing is `_get_next_window_pair` function with 2k calls. And we calculate length of input 2k times here! Nonsense! Moving that part in class initializer.
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |     84.6804 | 0:00:00.005571 |     84.6801 | 0:00:00.005554 |
```
Finally, some result.

After that moment I try to find some other ways to improve performance, like change class to [slotted](https://wiki.python.org/moin/UsingSlots), moving parts of code up and down. That was useless.
So I decide to give up on class-based solution and give a shoot to old good imperative function.
Wrap all code in one function. Also, looking in puzzle text, I figure out, what there is no matter how big is window, all but first and last elements in windows are same. So we can remove `sum()`.
```
def get_increments_count(input_data, window_size):
    data_len = len(input_data)
    current_index = 0
    step = 1 + window_size
    increments_count = 0
    while data_len >= current_index + step:
        sub = input_data[current_index: current_index + step]
        if sub[0] < sub[:-1]:
            increments_count += 1
        current_index += 1
    return increments_count
```

And it gives me pretty good boost, almost 2x faster!
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |     84.6804 | 0:00:00.002261 |     84.6801 | 0:00:00.002546 |
```

Next, I rewrite `while loop` into `for loop` - why I manually check borders when Python can do it on himself.

```
def get_increments_count(input_data, window_size):
    increments_count = 0
    for index in range(0, len(input_data)-window_size):
        if input_data[index] < input_data[index+window_size]:
            increments_count += 1
    return increments_count
```
That was good suggestion.
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |     84.6804 | 0:00:00.001810 |     84.6801 | 0:00:00.001602 |
```

Now, the only thing I manually do here is summing, so i place my list in `sum()`

```
def get_increments_count(input_data, window_size):
    return sum(
        [1 if input_data[index] < input_data[index+window_size] else 0
            for index in range(0, len(input_data)-window_size)])
```

Ooo, such Pythonic, wow. Love oneliners. And what about performance?

```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     1 |     87.4395 | 0:00:00.001600 |     87.4391 | 0:00:00.001492 |
```

Almost nothing was improved here. Looking at memory consumption, we make it even worse. But i loves it.

#### Analysis

Summing up my data. 

| Change            | Avg. Time Part 1 | Avg. Time Part 2 |
|-------------------|------------------|------------------|
| Original solution | 0.006826         | 0.006724         |
| Improved input    | 0.006682         | 0.006894         |
| Input length calc | 0.005571         | 0.005554         |
| While loop        | 0.002261         | 0.002546         |
| For loop          | 0.001810         | 0.001602         |
| Sum() on list     | 0.001600         | 0.001492         |

After optimization I increase performance on ~75% in execution time.