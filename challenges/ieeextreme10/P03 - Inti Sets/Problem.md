# Inti Sets
In order to motivate his Peruvian students, a teacher includes words in the Quechua language in his math class.

Today, he defined a curious set for a given positive integer *N*. He called this set, an *Inti set*, and defined it as the set of all positive integer numbers that have the number *1* as their single common positive divisor with number *N*.

The math class about Inti sets was amazing. After class, the students try to challenge to teacher. They each ask questions like this: "Could you tell me the sum of all numbers, between *A* and *B* (inclusive), that are in the Inti set of *N*?"

Since the teacher is tired and he's sure that you are the best in class, he wants to know if you can help him.

## Input Format
The first line of input contains an integer *Q*, `1 ≤ Q ≤ 20`, representing the number of students. Each of the next *Q* lines contain three space-separated integers *N*, *A* and *B*, which represent a query.

## Constraints
```
1 ≤ A ≤ B ≤ N ≤ 10^12
```

## Output Format
The output is exactly *Q* lines, one per student query. For each query you need to find the sum of all numbers between A and B, that are in the Inti set of N, and print the sum modulo 1000000007.

## Sample Input
```
2
12 5 10
5 1 4
```

## Sample Output
```
12
10
```

## Explanation
In the sample input, `Q = 2`, so you have to answer two questions:

In the first question `N = 12`, `A = 5` and `B = 10`. So you have to find the sum of all numbers between 5 and 10, that are in the Inti set of 12.

`Inti set ( 12 ) = { 1, 5, 7, 11, 13, ... }`

2 and 4 are not in the Inti set (12) because 12 and these numbers are also divisible by 2.

3 and 9 are not in the Inti set (12) because 12 and these numbers are also divisible by 3.

The numbers in the Inti set, which are in the query's range, are 5 and 7, so answer is `( 5 + 7 ) MOD 1000000007 = 12`

In the second question, the numbers in the Inti set of 5 between 1 and 4 are: 1, 2, 3, 4; so the answer is `( 1 + 2 + 3 + 4 ) MOD 1000000007 = 10`
