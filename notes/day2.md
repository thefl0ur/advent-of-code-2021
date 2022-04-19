Do same routine with day 2 solution.

Stats for original solution
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002176 |     78.1681 | 0:00:00.002333 |
```

There is same as day 1 problem with input - for some reason I manually fill list, instead of using list comprehension
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.3043 | 0:00:00.002125 |     78.3041 | 0:00:00.002362 |
```
Again, no profit. Now, i think it is time to understand what is going on here.
After multiple runnings of profiler and  performance test all I can say: changes less than 0.0001 seconds, so it is absolutely useless to optimize reading.
So unlike in day 1, I stick with my original function. Maybe it will be the only unchanged part of code.

Jump in profiler to find out next steps.
```
name                                  ncall  tsub      ttot      tavg      
..ive.py:11 Dive.calculcate_position  1      0.002871  0.006678  0.006678
..s/day2/dive.py:26 Dive._parce_line  1000   0.002543  0.003807  0.000004

name                                  ncall  tsub      ttot      tavg      
...py:34 DiveAim.calculcate_position  1      0.004058  0.008760  0.008760
..ay2/dive.py:26 DiveAim._parce_line  1000   0.003157  0.004702  0.000005
```

There is only 2 function remain. Starts with `_parce_line`.

See no reason to split line in class, lets try to move that login into beloved `read_data`
Moving that part in reading gives as next results: algorithm become faster, but memory skyrockets almost 3 times.
I set `maxsplit=2`, and that gives somewhere good result: performance increased, and memory only 2x times.
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002299 |     223.745 | 0:00:00.001667 |
```

But what if I split into tuple?
```
def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            (vector, value) = line.rstrip().split(' ', 2)
            data.append((vector, value))
    return data
```
Bingo! Memory struggle was fixed! There is site-by-side comparison of 2 reading functions:
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002478 |     76.1682 | 0:00:00.001713 |
```

So, intermediate result are next:
```
Running perfomance test  [####################################]  100%  Finished                            
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     76.1684 | 0:00:00.001640 |     76.1681 | 0:00:00.002036 |
```
But reading (and basic data processing) in `read_data` is slowest part of solution. Calculation takes about 1/10 of all time of execution.