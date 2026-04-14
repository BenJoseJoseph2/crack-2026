# 1. Two Sum

## Problem Link

https://leetcode.com/problems/two-sum/

## Problem Statement

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order

## Examples

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

## Key Insights

1. We need to return indices, not the values themselves.
2. Exactly one valid pair always exists — no need to handle "no solution" case.
3. The same element cannot be used twice (e.g. if target=6 and nums=[3], you can't use index 0 twice).
4. Array is not sorted — so binary search doesn't directly apply without sorting first.

## Solution

```python


Two Sum — Complete Algorithm Breakdown

Brute Force Approach

Algorithm

The idea is dead simple — check every possible pair of indices and see if their values add up to the target.

Start an outer loop with index i from 0 to n-2
For each i, start an inner loop with index j from i+1 to n-1
At each pair (i, j), check if nums[i] + nums[j] == target
If yes → return [i, j] immediately
j always starts at i+1 so we never reuse the same index twice



def two_sum_brute(nums, target):
    n = len(nums)

    for i in range(n):              # Fix the first element
        for j in range(i + 1, n):  # Try every element after i
            if nums[i] + nums[j] == target:
                return [i, j]


DRY RUN : 

nums = [2, 7, 11, 15],  target = 9

i=0, j=1  →  2 + 7  = 9  ✓  →  return [0, 1]

-----------------------------------------

nums = [3, 2, 4],  target = 6

i=0, j=1  →  3 + 2 = 5  ✗
i=0, j=2  →  3 + 4 = 7  ✗
i=1, j=2  →  2 + 4 = 6  ✓  →  return [1, 2]


Time Complexity — O(n²)
Why O(n²)?
The outer loop runs n times. For each iteration of the outer loop, the inner loop runs roughly n times too (slightly less, but in the same order). So total comparisons:

When i=0  → j runs n-1 times
When i=1  → j runs n-2 times
When i=2  → j runs n-3 times
...
When i=n-2 → j runs 1 time

Total = (n-1) + (n-2) + (n-3) + ... + 1
      = n(n-1) / 2
      = roughly n²/2
      = O(n²)  ← we drop constants in Big O


Space Complexity — O(1)
The brute force uses no extra data structures at all. Just two integer loop variables i and j. No arrays, no maps, no recursion stack. Memory usage stays constant no matter how large the input is. That's the one silver lining of this approach — it is memory efficient, just horribly slow.


Optimized Approach — Hash Map

Algorithm

Instead of nested loops, we use a hash map (dictionary in Python) to store numbers we've already seen and their indices.

Iterate through the array once
For each number nums[i]:
Calculate the complement needed: complement = target - nums[i]
Check if complement exists in the hash map
If yes → we found the pair! Return [map[complement], i]
If no → add the current number and its index to the map: map[nums[i]] = i
This way, for every number, we do one quick lookup (average O(1)) instead of a full scan.


def two_sum(nums, target):
    seen = {}  # Maps  value → index

    for i, n in enumerate(nums):
        diff = target - n          # The complement we're looking for

        if diff in seen:           # Already seen it? Pair found!
            return [seen[diff], i]

        seen[n] = i                # Not found yet — store for future



nums = [2, 7, 11, 15],  target = 9

i=0, n=2  |  diff = 9 - 2 = 7  |  7 in seen? NO   |  store seen = {2: 0}
i=1, n=7  |  diff = 9 - 7 = 2  |  2 in seen? YES  |  return [seen[2], 1] = [0, 1] ✓

------------------------------------------------------------------

nums = [3, 2, 4],  target = 6

i=0, n=3  |  diff = 6 - 3 = 3  |  3 in seen? NO   |  store seen = {3: 0}
i=1, n=2  |  diff = 6 - 2 = 4  |  4 in seen? NO   |  store seen = {3:0, 2:1}
i=2, n=4  |  diff = 6 - 4 = 2  |  2 in seen? YES  |  return [seen[2], 2] = [1, 2] ✓

------------------------------------------------------------------

Edge case → nums = [3, 3],  target = 6

i=0, n=3  |  diff = 6 - 3 = 3  |  3 in seen? NO   |  store seen = {3: 0}
i=1, n=3  |  diff = 6 - 3 = 3  |  3 in seen? YES  |  return [seen[3], 1] = [0, 1] ✓
           ↑ Works perfectly because we checked BEFORE storing index 1
```
