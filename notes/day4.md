Here we are - th first puzzle without resolved part 2.
However, code passes test for both parts, but on real data it fails. 
Look likes some border conditions fails. 
Remember how I lost a lot of time at December's Saturday like it was yesterday.

# Part 1.

First, I have to reassemble all this spaghetti code to fit in existing structure.
After that I can finally measure timings.

|   DAY |   MEM 1, Kb | TIME 1         |
|-------|-------------|----------------|
|     4 |     180.429 | 0:00:00.037125 |

First iteration of refactoring give next results:
|   DAY |   MEM 1, Kb | TIME 1         |
|-------|-------------|----------------|
|     4 |     82.9178 | 0:00:00.030266 |

What was done:
* reading input: nothing really changed, just place all input parsing code in one function
* removes global variables
* checking winners uses list comprehension instead of iteration, refused rotation of matrix for working with columns