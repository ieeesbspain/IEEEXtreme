# Dog Walking
Your friend, Alice, is starting a dog walking business. She already has *K* dog walkers employed, and today there are *N* dogs that need to be walked. Each dog walker can walk multiple dogs at the same time, so the dogs will be arranged into *K* nonempty groups, and each group will then be walked by a single dog walker. However, smaller dogs can be aggressive towards larger dogs, and that makes it harder to walk them together.

More formally, if the smallest dog in a group has size *a*, and the largest dog in the group has size *b*, then the range of the group is defined as *b-a*. In particular, the range of a group consisting of a single dog is 0. The smaller the range of a group is, the easier it is to walk that particular group. Hence Alice would like to distribute the dogs among the dog walkers so that the sum of ranges of the groups is minimized. Also, since she doesn't want any of the dog walkers to feel left out, she makes sure each dog walker gets to walk at least one dog.

Given *N*, *K* and the sizes of the dogs, can you help Alice determine what is the minimum sum of ranges over the *K* groups if the dogs are arranged optimally?

## Input Format
The first line of input contains *t*, `1 ≤ t ≤ 5`, which gives the number of test cases.

Each test case starts with a line containing two integers *N*, the number of dogs, and *K*, the number of employees, separated by a single space. Then *N* lines follow, one for each dog, containing an integer x representing the size of the corresponding dog.

## Constraints
```
1 ≤ K ≤ N ≤ 10^5
0 ≤ x ≤ 10^9
```

## Output Format
For each test case, you should output, on a line by itself, the minimum sum of ranges over the *K* groups if the dogs are arranged optimally.

## Sample Input
```
2
4 2
3
5
1
1
5 4
30
40
20
41
50
```

## Sample Output
```
2
1
```

## Explanation
In the first test case there are four dogs: one of size 3, one of size 5, and two of size 1. There are two dog walkers, and we want to distribute the dogs among them. One optimal way to do this is to make one dog walker walk the dogs of size 3 and 5, and the other dog walker walk the two dogs of size 1. Then the first group has range `5-3=2`, while the second group has range `1-1=0`, giving a total of `2+0=2`.

In the second test case there are dogs of size 30, 40, 20, 41 and 50, and four dog walkers. There are so many dog walkers that we can ask all but one of them to walk a single dog. We will make the last dog walker walk the dogs of size 40 and 41, which gives a range of `41-40=1`. All other groups have range 0, so the total is 1.
