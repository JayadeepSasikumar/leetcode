class Solution:
    def twoSum(self, nums, target):
        """
        Link to problem: https://leetcode.com/problems/two-sum/
        
        Problem statement:
            Given an array of integers, return indices of the two
            numbers such that they add up to a specific target.

            You may assume that each input would have exactly one
            solution, and you may not use the same element twice.

        Example:

            Given nums = [2, 7, 11, 15], target = 9,

            Because nums[0] + nums[1] = 2 + 7 = 9,
            return [0, 1].
        
        Args -
            nums - list, of int
            target - int
        
        Pseudocode -
            1. Keep a dict locs = {element: position}
            2. For each item in nums,
                i. check if an entry exists in loc for its complement
                   (target-item).
                   if it exists and is at a different position:
                       return the indices of item and its complement.
                   if not:
                       add item: index to nums
        
        Returns -
            result - list, of int, indices of the two elements found.
        """
        locs = {}
        for idx, item in enumerate(nums):
            try:
                other_idx = locs[target-item]
            except KeyError:
                locs[item] = idx
            else:
                if idx == other_idx:
                    continue
                return [idx, other_idx]