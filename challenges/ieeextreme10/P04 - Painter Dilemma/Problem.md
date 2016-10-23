# Painter's Dilemma
Bob just got his first job as a house painter. Today, on his first day on the job, he has to paint a number of walls.

For those of you that have done some house painting before, you know that this is no easy task. Each wall has to be painted in multiple rounds, possibly with a different color of paint each time, and there needs to be sufficient time of waiting between consecutive rounds for the paint to dry.

To make optimal use of their time, house painters usually paint walls while waiting for other walls to dry, and hence interleave the rounds of painting different walls. But this also brings up another challenge for the painters: different walls may require different colors of paint, so they might have to replace the color on one of their paint brushes before painting that wall. But this requires washing the paint brush, waiting for it to dry, and then applying the new paint to the brush, all of which takes precious time.

The more experienced house painters circumvent the issue by bringing a lot of paint brushes. But Bob is not that fortunate, and only has two paint brushes!

Given a sequence of colors *c1*, *c2*, *...*, *cN* that Bob needs, in the order that he needs them, can you help him determine the minimum number of times he needs to change the color of one of his brushes? Both of his brushes will have no color to begin with.

Bob may ask you to compute this number for a few different scenarios, but not many. After all, he only needs to do this until he gets his first paycheck, at which point all his effort will have been worth the trouble, and he can go buy more paint brushes.

## Input Format
The first line of input contains *t*, `1 ≤ t ≤ 5`, which gives the number of scenarios.

Each scenario consists of two lines. The first line contains an integer *N*, the length of the sequence of colors Bob needs. The second line contains a sequence of *N* integers *c1*, *c2*, *...*, *cN*, representing the sequence of colors that Bob needs, in the order that he needs them. Each distinct color is represented with a distinct integer.

## Constraints
```
1 ≤ N ≤ 500
1 ≤ ci ≤ 20
```

## Output Format
For each scenario, you should output, on a line by itself, the minimum number of times Bob needs to change the color of one of his brushes.

## Sample Input
```
2
5
7 7 2 11 7
10
9 1 7 6 9 9 8 7 6 7
```

## Sample Output
```
3
6
```

## Explanation
In the first scenario, Bob needs to paint using the colors 7, 7, 2, 11, and 7, in that order. He could start by applying color 7 to the first brush. Then he can use the first brush for the first two times. The third time he needs the color 2. He could apply that color to his second brush, and thus use his second brush for the third time. Next he needs the color 11, so he might apply this color to the first brush, and use the first brush this time. Finally, he needs the color 7 just as before. But the first brush no longer has this color, so we need to reapply it. Just as an example, he could apply 7 to the second brush, and then use the second brush. In total, he had to change the color of one of his brushes 4 times.

However, Bob can be smarter about the way he changes colors. For example, considering the same sequence as before, he could start by applying color 7 to the first brush, and use the first brush for the first two times. Then he could use the second brush twice, first by applying the color 2, and then by applying the color 11. This leaves the first brush with paint 7, which he can use for the last time. This leaves him with only 3 color changes in total.
