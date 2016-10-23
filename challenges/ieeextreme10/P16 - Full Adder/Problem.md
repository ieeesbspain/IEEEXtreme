# Full Adder
We would like your help to create a basic adder. However, this adder, should work in any base, with any set of symbols.

## Input Format
The first line of input contains an integer *b*, a space, and a list of *b* symbols that make up the base. The symbols are listed in order from the least significant symbol to the most significant symbol. In other words, the first symbol listed corresponds to 0, the second corresponds to 1, etc. These symbols can be numbers, uppercase letters, or lowercase letters.

The remaining lines contain the addition problem to be solved, as shown in the sample input and output. The operands will be non-negative numbers expressed in the given base. Note that the last line contains question marks which must be replaced with the correct value.

## Constraints
```
2 ≤ b ≤ 62
```

The numbers to be added can contain up to 10^7 symbols.

## Output Format
The first four lines of output should be identical to the input. The last line should contain the solution to the problem, with the answer aligned appropriately.

## Sample Input
```
10 0123456789
752
+76045
------
???
```

## Sample Output
```
10 0123456789
752
+76045
------
76797
```

## Explanation
The first sample corresponds to a normal base-10 addition problem.

Additional sample problems are available if you click on the `Run Code` button.

The second sample problem has the following input:
```
10 wj8Ma04HJg
 H
+8J4J
-----
???
```

This is a base-10 problem with different symbols. `H` corresponds to the digit `7` and `8J4J` is the number `2868`. When adding these numbers, the result is `2875`, which is represented as `8JH0` in the given base. Thus the expected output is:
```
10 wj8Ma04HJg
 H
+8J4J
-----
8JH0
```
