class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(1)
                update = 1
            else:
                update = update * nums[i-1]
                res.append(update)

        for j in range(len(res)-1 , -1, -1):
            if j == len(nums) -1:
                res[j] = res[j] *1
                update = 1
            else:
                update = update * nums[j+1]
                res[j] = res[j]*update
        return res



        

        