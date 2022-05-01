That's tricky. 

Part 1 i solve in 5 minutes, some how I guess that median would give me right answer.

As part 1 was easy, part 2 was hard.

I say it load and clear: I dont' know how to solve part 2 without some help and brute force.

As I remember from comments on reddit I should use `mean` instead of `median`. 
It also can give me wrong result so I should check range `[mean-1, mean, mean+1]` and also from comments I get algorithm for fuel consumption `n(n+1)/2`.
Let's try to combine that and take another lost star for 2021 AoC.

So, it works well, and i get stat star. Also minimal result I get not from `mean` point, but from `mean+1`.

|   DAY |   MEM 1, Kb | TIME 1         |   MEM 2, Kb | TIME 2         |
|-------|-------------|----------------|-------------|----------------|
|     7 |     95.8385 | 0:00:00.001017 |     95.8382 | 0:00:00.002896 

As we can see, part 2 is about 3x slower, which is reasonable - we run almost same code from part 1 3 times. I bet, if we knew for sure which point would be optimal timeing was almost the same as in part 1.