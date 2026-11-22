class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p,s = 1,1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]

        #[1,1,2,8]

        for j in range(len(nums)-1,-1,-1):
            res[j] *= s
            s *= nums[j]

        return res