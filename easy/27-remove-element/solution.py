class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        val_recurring = 0

        while left <= right:
            if nums[right] == val:
                right -= 1
                val_recurring += 1
                continue
            if nums[left] != val:
                left += 1
                continue
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                val_recurring += 1

        return len(nums) - val_recurring