# Forum Threads
Consider a list of posts in an internet forum divided in pages. In order to keep the pages as aesthetically pleasant as possible, the graphics team came up with the optimal number of posts in every page. Then the user experience team decided that it would be convenient to group posts into threads, this is, list all replies to a post (and the replies to those replies) consecutively, and that a thread should not be split in different pages. Now you should find a layout for the posts such that

1. posts in the same thread are listed consecutively;
2. threads are ordered by the time of the first post;
3. posts in the same thread are in the same page; and
4. the maximum difference between the number of posts per page and the intended number is minimal.

Note: the goal is to minimize how bad the worst page is, not the sum of how bad all of the pages are.

## Input Format
The input consists of a number of test cases.

The first line of each test case contains two integers *a*, *p*, the intended number of posts per page and the number of posts respectively. Then there is a line for each post, in the order they were posted. The *ith* line contains a positive integer *x* if the ith post is a reply to the *xth* post, or 0 if the *ith* post starts a new thread.

## Constraints
```
0 ≤ a, p ≤ 1 000
0 < x < i
```

## Output Format
Output one line per test case with one integer, the maximum difference between the number of posts per page and the intended number in a layout that satisfies the conditions.

## Sample Input
```
3 6
0
1
2
0
4
5
3 6
0
0
0
0
0
3
```

## Sample Output
```
0
1
```

## Explanation
In the first test case there are 6 posts that are to be distributed at a ratio of 3 posts per page. There are 2 threads with 3 posts each, so a layout with the first thread in the first page and the second thread in the second page fits perfectly.

In the second test case there are 2 single posts, a thread with 2 posts, and 2 more single posts. Since the middle thread cannot be split between the 2 pages, a layout with a one post imbalance is optimal. The optimal configuration may not be unique. In fact in this test case, there are three configurations that are optimal:

* Posts 1–3 could be put in the first page, and posts 4 and 5 in the second. In this case, the first page would contain one extra post (6, which is a reply to post 3), and the second page would contain one fewer.

* Posts 1 and 2 could be put in the first page, and posts 3–5 in the second.

* Posts 1 and 2 could be put in the first page, post 3 (with its reply) in the second, and posts 4 and 5 in the third.
