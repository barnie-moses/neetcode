class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
            
        length = 1
        nums_set = set(nums)

        for num in nums_set:
            if num-1 not in nums_set:
                start = num
                curLen = 1
                while (start +1 ) in nums_set:
                    curLen +=1
                    start +=1
                    if length <= curLen:
                        length = curLen

        return length