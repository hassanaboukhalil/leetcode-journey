# 88. Merge Sorted Array

**Difficulty:** Easy  
**Topic(s):** Array, Two Pointers  
**LeetCode Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)

---

## 🧠 Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.  
The final sorted array should not be returned but stored in `nums1` in-place.

---

## 🧪 Examples

**Example 1:**

Input: nums1 = [1,2,3,0,0,0], m = 3
<br>
nums2 = [2,5,6], n = 3
<br>
Output: [1,2,2,3,5,6]

**Example 2:**

Input: nums1 = [1], m = 1
<br>
nums2 = [], n = 0
<br>
Output: [1]

**Example 3:**

Input: nums1 = [0], m = 0
<br>
nums2 = [1], n = 1
<br>
Output: [1]

## 💬 Explanation

- We use three pointers:

  - p1 for the end of the valid part of nums1

  - p2 for the end of nums2

  - p for the end of the merged array (which is the end of nums1)

- We compare from the end and fill nums1 backwards to avoid overwriting.

- This achieves O(m + n) time and O(1) space.

## 🌟 Like this format?

Star this repository if it helps you, and feel free to share or fork it!
