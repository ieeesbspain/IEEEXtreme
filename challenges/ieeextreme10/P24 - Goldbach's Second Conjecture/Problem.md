# Goldbach's Second Conjecture
An integer p > 1 is called a prime if its only divisors are 1 and p itself. A famous conjecture about primes is Goldbach's conjecture, which states that

> Every *even* integer greater than *2* can be expressed as the sum of *two primes*.

The conjecture dates back to the year 1742, but still no one has been able to come up with a proof or find a counterexample to it. We considered asking you prove it here, but realized it would be too easy. Instead we present here a more difficult conjecture, known as Goldbach's second conjecture:

> Every *odd* integer greater than *5* can be expressed as the sum of *three primes*.

In this problem we will provide you with an odd integer *N* greater than 5, and ask you to either find three primes *p1*, *p2*, *p3* such that `p1 + p2 + p3 = N`, or inform us that *N* is a counterexample to Goldbach's second conjecture.

## Input Format
The input contains a single odd integer `5 < N ≤ 10^18`.

## Output Format
Output three primes, separated by a single space on a single line, whose sum is *N*. If there are multiple possible answers, output any one of them. If there are no possible answers, output a single line containing the text "*counterexample*" (without quotes).

## Sample Input
```
65
```

## Sample Output
```
23 31 11
```

## Explanation
In the sample input *N* is 65. Consider the three integers 11, 23, 31. They are all prime, and their sum is 65. Hence they form a valid answer. That is, a line containing "11 23 31", "23 31 11", or any permutation of the three integers will be accepted. Other possible answers include "11 37 17" and "11 11 43".
