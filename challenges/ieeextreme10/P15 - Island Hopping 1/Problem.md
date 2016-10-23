# Island Hopping 1
Bob is the captain of a boat in the island nation of Artskjid. Most of the time he cannot go directly from his starting island to the ending island because his boat cannot hold enough fuel for the entire journey, and so he must make stops to refuel.

Bob’s boat holds up to 100 units of fuel. There is an additional complication in that fuel is rationed on the islands, and the maximum amount of fuel that he can receive at each stop varies from island to island. When stopping at an island, the fuel taken from previous stops at that island do not affect the current one. Furthermore, the fuel ration for an island resets every time Bob stops there.

While he can visit an island multiple times on the journey (in order to get fuel), he cannot visit the same island consecutively. He must go to one or more different islands, before returning to an island.

Bob wants to know the minimum amount of fuel he needs in order to complete his journey.

## Input Format
The input starts with a line containing an integer *t*, `1 ≤ t ≤ 10`, which gives the number of test cases in the input.

Each test case begins with a line containing an integer *n*, where *n* is the number of islands.

Then there are *n* lines containing a description of the islands in the form:
```
[name] [fuel]
```
where `[name]` is the name of the island, in the form of a string made up only of letters (no spaces), and `[fuel]` is an integer indicating the amount of fuel available, per stop, on the island.

On the next line is an integer *m*, where *m* is the number of navigable channels between islands.

Then there are *m* lines containing a description of the available paths between islands:
```
[island1] [island2] [fuel_needed]
```
where `[island1]` and `[island2]` are island names that appeared in the first n lines of the testcase, and `[fuel_needed]` is an integer indicating the amount of fuel needed to travel between these islands. Note that travel can occur in either direction, i.e. from `[island1]` to `[island2]` or from `[island2]` to `[island1]`.

Bob will always start with the island named `start`, and end at the island named `end`. Note that he starts with an empty tank of gas, so the `[fuel]` listed for the `start` island gives Bob’s initial amount of fuel.

## Constraints
```
2 ≤ n ≤ 50
0 ≤ m ≤ 500
0 ≤ [fuel] ≤ 100
0 ≤ [fuel_needed] ≤ 200
```

## Output Format
For each test case, you should output, on a line by itself, either the minimum units of fuel needed for Bob to get from the starting point to the ending point, or `Impossible` if there is no way for Bob to reach the ending point from the starting point.

## Sample Input
```
2
3
start 2
end 0
midway 50
3
start midway 1
end midway 90
start end 99
5
start 1
end 0
amity 2
atlantis 3
azkaban 4
5
start end 101
start amity 1
atlantis amity 2
azkaban atlantis 3
azkaban start 1
```

## Sample Output
```
93
Impossible
```

## Explanation
In the first test case, Bob can start with 2 units of fuel, and go to `midway` island. Since this trip uses 1 unit of fuel, he arrives with 1 unit of fuel, and then adds 50 more, for a total of 51 units of fuel.

He still cannot reach the final island. Instead, he returns to `start` island (with 50 units of fuel upon arrival). He adds 2 more units of fuel, for a total of 52 units of fuel, and then he goes back to `midway`.

He arrives with 51 units of fuel, and then fills up his tank so that it now holds 100 units of fuel. He now has enough fuel to make it to the destination, using 90 more units of fuel.

There are no other trips that require less fuel, so you would output 93, the total of units of fuel that was used.

For the second test case, there is no way to reach the `end` island with fuel that fits in Bob's tank.
