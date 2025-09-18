class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # nums.sort()
        # if len(nums) == 0: return 0
        # lMax = gMax = 1
        # prev = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i] - prev == 1:
        #         lMax += 1
        #     elif nums[i] != prev:
        #         lMax = 1
        #     gMax = max(gMax, lMax)
        #     prev = nums[i]
        # return gMax
            

        numSet = set(nums)
        if not nums:
            return 0
        cntMax = 1
        for num in numSet:
            inc = 0
            if num-1 not in numSet:
                while (num+inc) in numSet:
                    inc += 1
            cntMax = max(cntMax, inc)

        return cntMax