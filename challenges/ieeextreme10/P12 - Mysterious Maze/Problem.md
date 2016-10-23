# Myterious Maze
There is a valuable treasure that is hidden below a complex maze. The maze is made of rooms and are square in shape, and a maze of size *N* will have *N × N* rooms with all of them closed initially. When a room is open, one can enter into it from any of its adjacent open rooms; two rooms are adjacent if they share a common wall.

The maze was built in a way that it opens itself by opening its rooms randomly. A maze is said to be open if there is at least one path from any one of the rooms facing the top of the maze to any room on the bottom side facing the treasure. Anyone, who attempts to enter the maze without being able to reach the treasure and return, will be cruelly killed by the maze.

The local government has spent years researching the maze and figured out a way to determine the sequence of rooms being opened in almost real time. Based on this data, the government has posed the following challenge, with a small percentage of the treasure to whomever solves the problem:

Given the sequence of room openings, determine when the maze becomes open, or if it remains closed throughout.

## Input Format
Input begins with a single integer *N*, which denotes the size of maze.

All of the next lines (except the last one) denotes the sequence of the rooms the maze is opening. Each line contains 2 integers *X* and *Y* which denotes the row and column of the room opened by the maze. The last line just includes -1 and marks the end of input.

## Constraints
```
1 <= X
Y <= N <= 1000
```

## Output Format
Output a single integer *R* based on the final status of the maze. *R* denotes the number of room openings that occur before the maze first becomes open, or -1 if the maze remains closed.

## Sample Input
```
4
1 4
2 3
3 2
4 3
4 1
2 1
1 1
-1
```

## Sample Output
```
-1
```

## Explanation
It is easy to understand if you plot the maze. The following is the state of the maze at the end of the inputs. `X` indicates that a room is closed and `O` that a room is open. Note that there is no path from the top of the maze to the bottom of the maze.
```
O X X O
O X O X
X O X X
O X O X
```

Consider the second input sample (which is available if you click on the `Run Code` button):
```
4
1 4
2 3
3 2
4 3
4 1
2 1
1 1
3 1
3 4
2 2
-1
```

Below is a figure with the maze after 7 rooms are open. Note that there is no path from the top of the maze to the bottom of the maze, and therefore the maze is closed.
```
O X X O
O X O X
X O X X
O X O X
```

However, after 8th room is open, there is a path, as shown below:
```
O X X O
O X O X
O O X X
O X O X
```

Thus, the expected output is:
```
8
```
