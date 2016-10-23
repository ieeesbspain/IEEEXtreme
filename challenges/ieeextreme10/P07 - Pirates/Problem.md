# Pirates
Fierce pirates have just arrived in the archipelago. They are searching for a hidden treasure and only have a map to help them. The map looks like a matrix with N rows and M columns with every cell containing one of the two symbols: 'O' or '~'. A land cell is represented by the symbol 'O' and a sea cell by '~'. Two land cells are part of the same island if there is a way from one to the other walking only on land cells, and from a cell one can walk in all 8 directions. The pirates are in cell *(x1, y1)* and the treasure is in cell *(x2, y2)*, both of which are sea cells. To get to the treasure, the pirates may need to cross some islands. The police only watch over the land cells, and thus you have to help the pirates find a path to the treasure crossing a minimal number of islands. You need to help the pirates *Q* times.

Note:
* The top left cell is designated as (1,1), and the bottom right cell is *(N, M)*.

* Crossing an island occurs whenever the pirates go from a sea cell to a land cell. If the pirates cross the same island multiple times, it should be counted that many times.

## Input Format
The first line of input contains three space-separated integers, *N*, *M* and *Q*.

The next *N* lines contain the description of the map.

The last *Q* lines contain the queries, in the form of four space-separated integers, *x1*, *y1*, *x2*, and *y2*.

## Constraints
```
1 ≤ N, M ≤ 1000
1 ≤ Q ≤ 105
1 ≤ x1, x2 ≤ N
1 ≤ y1, y2 ≤ M
```

## Output Format
For each query, you should output, on a line by itself, the minimum number of islands that must be traversed when travelling from *(x1, y1)* to *(x2, y2)*.

## Sample Input
```
4 12 2
OOOOO~~OOOOO
O~~OO~OO~~~O
OO~OO~~O~O~O
OOOOOO~OOOOO
2 2 3 11
4 7 3 9
```

## Sample Output
```
2
1
```

## Explanation
The map for this test case consists of two islands.

In the first query, the pirates begin in the water body that is surrounded by the island to the left, and end in the water body surrounded by the island to the right. They must cross both these islands to get from start to finish.

For the second query, they begin in the body of water between the two islands, and end in the body surrounded by the island to the right. They must cross the island to the right to reach the treasure.
