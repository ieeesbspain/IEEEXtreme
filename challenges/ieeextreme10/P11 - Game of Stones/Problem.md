# Game of Stones 1
Alice and Bob play a game. The game is turn based: Alice moves first, then Bob, and so on. There are *N* piles of stones; in every pile there is an odd number of stones. At every turn, the one to play must pick a pile and splits it into 3 piles with an odd number of stones each.

The player who cannot split any pile loses. As this game is too simple for both of them, they decided to play multiple games in parallel. The rules remain the same, but at every turn, the one to play must first pick a game and then split a pile only in that game. The one who loses is the one that can't split any pile in any game, i.e. all the piles in all the games have only 1 stone. Bob still thinks that he is at a disadvantage, since he is the second to move. Your task is to find the winner if both the players play optimally.

## Input Format
The input begins with an integer *T*, giving the number of test cases in the input.

Each testcase begins with an integer *G*, on a line by itself, giving the number of games to be played in parallel.

The *G* games are then described in two lines as follows: The first line gives the number of piles in the game, and the second contains the number of stones in each of the piles.

## Constraints
```
1 <= T <= 10
1 <= [Number of piles in all games in a testcase] <= 105
1 <= [Number of stones in a pile] <= 109
```

## Output Format
For each testcase, output the winner, i.e. either `Alice` or `Bob`, on a line by itself.

## Sample Input
```
2
2
3
1 3 5
2
3 7
1
5
1 3 5 7 9
```

## Sample Output
```
Alice
Bob
```

## Explanation
The sample input can be annotated as follows:
```
2 (the number of tests)
2 (the number of parallel games for the first test)
3 (the number of piles in the first game)
1 3 5
2 (the number of piles in the second game)
3 7
1 (the number of parallel games for the second test)
5 (the number of piles)
1 3 5 7 9
```
