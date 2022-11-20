Originl code performance:

Running perfomance test  [####################################]  100%  Finished                             
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    14 |     30.9468 | 0:00:00.001156 |     35.4223 | 0:00:00.004287 |

First thing to improve was data reading function. Save somy bytes of ram. Perpormance impact almost unexist.

Running perfomance test  [####################################]  100%  Finished                             
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    14 |     24.5469 | 0:00:00.001158 |      29.022 | 0:00:00.004269 |


Next I try to convert solver function into recursime.
Here is the code for it:

```
def generate(pairs, rules, cntr, stop, current = 0):
    if current >= stop:
        return cntr

    current += 1
    result = defaultdict(int)
    for pair, num in pairs.items():
        new_element = rules[pair]
        cntr[new_element] += num

        result[f'{pair[0]}{new_element}'] += num
        result[f'{new_element}{pair[1]}'] += num
    
    return generate(result, rules, cntr, stop, current)
```
It was almost beautiful but totally non-efficient. 

Running perfomance test  [####################################]  100%  Finished                             
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    14 |     70.3919 | 0:00:00.001143 |     328.165 | 0:00:00.004680 |

Under profiler I was tring to find next points for improvement. I try to change pairs generation to smooth one-liner
and it makes code little slower. Rollback.

```
 pairs = defaultdict(int, {x:1 for x in [base_template[index:index+2:] for index in range(len(base_template)-1)]})
```

Running perfomance test  [####################################]  100%  Finished                             
|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|    14 |     24.5869 | 0:00:00.001301 |      29.062 | 0:00:00.004510 |