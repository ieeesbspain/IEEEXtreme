# Flower Games
Joy and her friends found a flower with N petals and want to play a modified version of the [He loves me... he loves me not](https://en.wikipedia.org/wiki/He_loves_me..._he_loves_me_not) game. The girls number the petals with numbers from 1 to *N* in the clockwise direction. They will traverse the petals in circular order starting with 1, then 2, ..., then *N*, then 1... At the first petal, they will shout "He loves me", at the second "He loves me not" and tear it, at the third "He loves me", at the fourth "He loves me not" and tear it. The girls will continue the game until there is only one petal left. The task is to identify the number of the last petal.

## Input Format
The input begins with an integer *T*, giving the number of test cases in the input.

Each testcase consists of an integer *N*, on a line by itself.

## Constraints
```
1 <= T <= 100000
1 <= N < 2^63
```

## Output Format
The location of the last petal, on a line by itself.

## Sample Input
```
4
2
3
4
6
```

## Sample Output
```
1
3
1
5
```

## Explanation
There are four test cases in the input.

With 2 petals, one would skip 1, tear 2, and then only 1 is left.

With 3 petals, one would skip 1, tear 2, skip 3, tear 1, and then only 3 is left.

With 4 petals, one would skip 1, tear 2, skip 3, tear 4, skip 1, tear 3, and then only 1 is left.

With 6 petals, one would skip 1, tear 2, skip 3, tear 4, skip 5, tear 6, skip 1, tear 3, skip 5, tear 1, and then only 5 is left.
