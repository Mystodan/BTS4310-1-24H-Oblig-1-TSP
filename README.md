# BTS4310-1-24H-Oblig-1-TSP
By Daniel Hao Huynh
In this assignment , we are going to solve the travelling salesman problem.
This implementation has implemented threading, meaning that after the city is generated, all the algorithms run concurrently.
### TSP
This problem is NP- hard, in computational complexity theory, NP-Hardness is used to classify problems that are, in a sense, as hard as the hardest problems in NP (nondeterministic polynomial time)
We are going to use the nearest neighbor heuristic algorithm as our greedy initial algorithm
### Random algorithm for TSP
Well this algorithm just randomizes the matrix inputted and outputs a random tour.
### Nearest Neighbor Heuristic for TSP
The Nearest Neighbor heuristic for TSP is a greedy algorithm that builds a tour by repeatedly visiting the nearest unvisited city until all cities have been visited. Here's a breakdown of how it works:

1. Start at a Random City: Select a random starting city.
2. Initialize Visited and Unvisited Lists: Keep track of visited and unvisited cities.
3. Find the Nearest Unvisited City: From the current city, find the nearest unvisited city and move to it.
4. Repeat Until All Cities are Visited: Continue the process until all cities have been visited.
5. Return the Tour and Time Taken: Return the sequence of visited cities (the tour) and the time taken to compute it.

### Results
1. 1000 Tours
```
time elapsed to solve using a basic random algorithm: 
        0.0 seconds
time to optimize:
        657.702832698822 seconds
total time elapsed:
        657.702832698822 seconds
old distance:
        1973
new distance:
        1000
time elapsed to solve using a basic greedy algorithm: 
        0.1880350112915039 seconds
time to optimize:
        446.1343762874603 seconds
total time elapsed:
        446.32241129875183 seconds
old distance:
        1002
new distance:
        1000
```
3. 3000 Tours
```
time elapsed to solve using a basic random algorithm: 
        0.0010035037994384766 seconds
time to optimize:
        7733.079829454422 seconds
total time elapsed:
        7733.080832958221 seconds
old distance:
        6049
new distance:
        3002
time elapsed to solve using a basic greedy algorithm: 
        1.40675950050354 seconds
time to optimize:
        7153.289403915405 seconds
total time elapsed:
        7154.696163415909 seconds
old distance:
        3002
new distance:
        3000
```
5. 5000 Tours  
```
time elapsed to solve using a basic random algorithm:
        0.0010035037994384766 seconds
time to optimize:
        24925.62091612816 seconds
total time elapsed:
        24925.621919631958 seconds
old distance:
        9992
new distance:
        5001
time elapsed to solve using a basic greedy algorithm:
        1.9668128490447998 seconds
time to optimize:
        16849.462002277374 seconds
total time elapsed:
        16851.42881512642 seconds
old distance:
        5003
new distance:
        5000
```
Using this command in the terminal from root would run the application
```sh
python .\tsp.py   
```


