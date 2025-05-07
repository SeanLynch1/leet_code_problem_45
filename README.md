# LeetCode Problem 45: Jump Game 2

## Problem Statement
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

  Input: nums = [2,3,1,1,4]
  Output: 2
  Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

## My inital Solution
After solving LeetCode Problem 55 (Jump Game) and realizing the effectiveness of the greedy algorithm, I attempted to apply a similar approach to this problem. I used the same idea of making local optimal decisions at each index, but my implementation wasn't fully greedy. As a result, some indices could be revisited, leading to less efficient performance. My solution ultimately ranked in the 27th percentile for time complexity on LeetCode.

While this approach was functional, I later realized that a truly greedy algorithm, which ensures each index is visited only once, could provide a more optimal solution. Below, I’ve included both my initial solution and the optimal solution that visits each index at most once.
