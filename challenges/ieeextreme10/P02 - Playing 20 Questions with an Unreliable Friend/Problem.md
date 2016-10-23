# Playing 20 Questions with an Unreliable Friend
To celebrate the 10th anniversary of Xtreme, your friend has arranged 10 balloons in a row in the next room, and has challenged you to guess the sequence of the colors in the row of balloons. The balloons can be red, blue, or green. Your friend will answer a series of yes/no questions about the colors of the balloons. Unfortunately, your friend will tell a certain number of lies when answering your questions.

The questions can be in one of the following forms:

1. You may ask if a particular balloon is a particular color, e.g.:
    * "Is the second balloon red?"
    * "Is the 10th balloon blue?"
2. You may ask about the count of balloons of a particular color, e.g.:
    * "Are there 3 red balloons?"
    * "Are there 0 blue balloons?"
3. The previous types of questions can be subquestions that are combined together into a larger question with *or*'s or *and*'s. When combined with an *or*, only one of the answers to the subquestions must be `yes` for the answer to the entire question to be `yes`, and when combined with *and*, all of the answers to the subquestions must be `yes` in order to the answer to the larger question to be `yes`.
    * "Is the third balloon green *or* the fourth balloon red?"
    * "Is the tenth balloon red *and* are there three red balloons *and* is the first balloon blue?"

Note that subquestions in a particular question will be combined either with *or*'s or *and*'s, but not both. You are not allowed to ask a question like "Is the tenth balloon red or are there three red balloons *and* is the first balloon blue?"

At the beginning of the game, your friend will tell you how many answers to your questions will be lies. *Your friend will be honest when telling you the number of lies he is about to tell*. Your task is to determine what colors each of the balloons could be given the answers to your questions, and the number of lies that were told.

## Input Format
The input begins an integer *t*, `1 ≤ t ≤ 20`, which gives the number of testcases in the input.

There will be a blank line preceding each testcase. Each testcase begins a line containing two space-separated integers *q* and *n*, where *q* is the number of questions that you asked, and n is the number of lies that your friend told when answering your questions. Note: `1 ≤ q ≤ 20`, `0 ≤ n ≤ q`

The next 2 *q* lines represent the questions and answers. A question will be made up of between 1 and 10, inclusive, subquestions in one of the following forms:

```
color i c

count c j
```

The first type of subquestion is asking if the *ith* balloon is the color *c*. *i* will be an integer, `1 ≤ i ≤ 10`, and *c* will be one of the following characters: `r`, `g`, or `b`.

The second type of subquestion is asking if the number of balloons of color *c* is equal to *j*. *c* will again be one of the following characters: `r`, `g`, or `b`. *j* will be an integer, `0 ≤ j ≤ 10`.

When there are multiple subquestions in a question, they will be separated by `or` or `and`.

The answer to each question will appear on the line immediately following the question, and it will be either `yes` or `no`.

## Output Format
For each test case, you should output a single line containing ten space separated values, where the *ith* value in the line corresponds to what you conclude about the color of the *ith* balloon. Each of the values will be one of the following strings:

* `r`, if you know that the balloon is red.
* `g`, if you know that the balloon is green.
* `b`, if you know that the balloon is blue.
* `rg`, if you know that the balloon must be either red or green.
* `rb`, if you know that the balloon must be either red or blue.
* `gb`, if you know that the balloon must be either blue or green.
* `rgb`, if you know that the balloon could be any of the possible colors.

Note that there should not be a space after the last value in the line.

## Sample Input
```
3

2 2
color 1 b
yes
color 2 r
no

3 1
count r 4 and count g 7
yes
color 1 b and color 2 r and color 3 b
yes
color 1 g or color 4 g
yes

2 0
count r 1
yes
color 6 b or color 1 r
yes
```

## Sample Output
```
rg r rgb rgb rgb rgb rgb rgb rgb rgb
b r b g rgb rgb rgb rgb rgb rgb
rgb rgb rgb rgb rgb gb rgb rgb rgb rgb
```

## Explanation
### First Testcase
In the first testcase, you ask two questions, and your friend lies about both of the answers.

Your first question is "Is the first balloon blue?" Since your friend lied when he said "yes", you know that it must be red or green.

Your second question is "Is the second balloon red?" Since your friend lied when he said "no", you know, in fact, that it must be red.

### Second Testcase
For the second test case, you ask three questions and your friend lies in one of the answers.

In the first question, you ask "Are there 4 red balloons and 7 green balloons?" Your friend answers "yes", but since there are only 10 balloons, this must be a lie. You can then conclude that the remaining answers are truthful.

In your second question, you ask "Is the first balloon blue, the second balloon red, and the third balloon blue?" Since your friend is telling the truth when he answers "yes", you now know the colors of the first three balloons.

In your final question, you ask "Is the first balloon green or the fourth balloon green?" Your friend truthfully answers "yes". Thus you can conclude that one of the following must be true:

1. Both the first and the fourth balloons are green.
2. The first balloon is green, but the fourth is not.
3. The fourth balloon is green, but the first one is not.

However, since you already know that the first balloon is blue, you know that it is the third case that must be true, so you conclude that the fourth balloon is green.

### Third Testcase
For the final testcase, your friend did not lie in any of the answers. You know that:

* There is one red balloon.
* Either the sixth balloon is blue or the first balloon is red, or both.

Note that if the first balloon is red, then no other balloons can be red, because of the first answer. If the first balloon is not red, then the sixth balloon must be blue, because of the second answer. Therefore, there is no scenario in which the sixth balloon can be red.
