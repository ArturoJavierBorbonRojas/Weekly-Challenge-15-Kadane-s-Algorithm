# Weekly-Challenge-15-Kadane-s-Algorithm
##  Description
For Week 15, I decided to take a step back from complex AI graphics and focus purely on algorithmic efficiency and data structures. I implemented **Kadane's Algorithm**, which solves the classic "Maximum Subarray Problem".

The objective is to find the contiguous subarray within a one-dimensional array of numbers that has the largest sum. This is a very common technical interview question at top tech companies because it tests your ability to optimize brute-force solutions.

## How it works
Instead of using nested loops to calculate the sum of every possible subarray (which is very slow), Kadane's algorithm uses dynamic programming concepts. As it iterates through the array, it maintains two variables:
1. `max_current`: The maximum sum ending at the current position.
2. `max_global`: The maximum sum found so far.

At each step, it asks a simple mathematical question: *Is it better to add the current number to my existing sequence, or is my existing sequence so negative that I should just start a new sequence from the current number?*

## Complexity Analysis
* **Time Complexity:** $O(n)$ - The algorithm only needs to traverse the array exactly once, making it incredibly fast.
* **Space Complexity:** $O(1)$ - It only uses a few variables to keep track of the sums and indices, meaning it requires constant memory regardless of the array's size.

##  Dependencies
* Python 3.14.3
* Numpy
