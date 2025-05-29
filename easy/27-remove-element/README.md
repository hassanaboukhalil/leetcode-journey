# 27. Remove Element

**Difficulty:** Easy  
**Topic(s):** Array, Two Pointers  
**LeetCode Link:** [Remove Element](https://leetcode.com/problems/remove-element)

---

## 🧠 Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.  
The order of elements can change. Return the number of elements that are not equal to `val`.

The first `k` elements of `nums` should hold the result. The remaining elements can be ignored.

---

## 🧪 Examples

**Example 1:**

Input: nums = [3,2,2,3]
<br>
val = 3
<br>
Output: 2, nums = [2,2,_,_]

**Example 2:**

Input: nums = [0,1,2,2,3,0,4,2]
<br>
val = 2
<br>
Output: 5, nums = [0,1,4,0,3,_,_,_]

## 💬 Explanation

- I use two pointers (left and right) to scan from both ends.

- If the left side is fine, we move forward.

- If left is the value and right is not, we swap and continue.

- Count how many times the value is found (val_recurring) and subtract it from the total.

- This ensures in-place operation with O(n) time and O(1) space.

## 🌟 Like this format?

Star this repository if it helps you, and feel free to share or fork it!
