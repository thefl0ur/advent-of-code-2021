Do same routine with day 2 solution.

Stats for original solution

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002176 |     78.1681 | 0:00:00.002333 |


There is same as day 1 problem with input - for some reason I manually fill list, instead of using list comprehension

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.3043 | 0:00:00.002125 |     78.3041 | 0:00:00.002362 |

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

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002299 |     223.745 | 0:00:00.001667 |


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

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     78.1683 | 0:00:00.002478 |     76.1682 | 0:00:00.001713 |


After this manipulations code for class become next:
```
class Dive:
    def __init__(self, data: List[str]):
        self.horizontal = 0
        self.depth = 0
        self.data = data

    def calculcate_position(self) -> int:
        for vector, value in self.data:
            if vector == 'up':
                self.depth -= value
            elif vector == 'down':
                self.depth += value
            else: 
                self.horizontal += value

        return self.horizontal * self.depth

class DiveAim(Dive):
    def __init__(self, data: List[str]):
        super().__init__(data)
        self.aim = 0

    def calculcate_position(self) -> int:
        for vector, value in self.data:
            if vector == 'up':
                self.aim -= value
            elif vector == 'down':
                self.aim += value
            else:
                self.horizontal += value
                self.depth += self.aim * value

        return self.horizontal * self.depth
```

Performance results:
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     76.1684 | 0:00:00.001752 |     76.1681 | 0:00:00.001961 |

But reading (and basic data processing) in `read_data` is slowest part of solution. Calculation takes about 1/10 of all time of execution.

I guess I can't find any way for faster processing, so may be I'll try to optimize memory consumption?

For now all data is loaded and stored in memory.
Rewrite `read_data` to generator and change `Dive::calculcate_position` function to take this generator.

```
def read_data_generator(file_name: str):
    with open(file_name, 'r') as file:
        for line in file:
            (vector, value) = line.rstrip().split(' ', 2)
            yield  (vector, int(value))
```
In term of perfomance it was not great at all, but memory consumption decreased in almost 4 times.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     20.8543 | 0:00:00.002351 |     20.8541 | 0:00:00.002068 |


Next let's try to rewrite all ito single function.

```
def part1(input_file: str) -> int:
    depth, horizontal = 0, 0
    with open(input_file, 'r') as file:
        for line in file:
            (vector, value) = line.rstrip().split(' ', 2)
            value = int(value)
            if vector == 'forward':
                horizontal += value
            else:
                depth += value if vector == 'down' else - value

    return horizontal * depth
```
Small win on both fileds!

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     20.6543 | 0:00:00.001799 |     20.6541 | 0:00:00.001733 |


At this moment I run out of ideas how to really increase performance, so i just remove castring result of split into tuple and remove `rstrip` - second value will be converted to `int`. Result after that:
                           
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     2 |     20.6543 | 0:00:00.001453 |     20.6541 | 0:00:00.001587 |


### Conclusion

| solution           | MEM 1, Kb | TIME 1   | MEM 2, Kb | TIME 2   |
|--------------------|-----------|----------|-----------|----------|
| Original           | 78.1683   | 0.002176 | 78.1681   | 0.002333 |
| list comprehension | 78.3043   | 0.002125 | 78.3041   | 0.002362 |
| maxsplit=2 + tuple | 76.1684   | 0.001752 | 76.1681   | 0.001961 |
| class + generator  | 20.8543   | 0.002351 | 20.8541   | 0.002068 |
| single function    | 20.6543   | 0.001799 | 20.6541   | 0.001733 |
| final              | 20.6543   | 0.001453 | 20.6541   | 0.001587 |

This time results was not so excellent. Max performance was increased only by 32% and memory consumption decreased by 75% only by the fact that data was not been stored in memory but processed on the fly.