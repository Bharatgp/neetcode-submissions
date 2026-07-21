class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1]*len(nums)
        sufProd = [1]*len(nums)

        for i in range(1,len(nums)):
            preProd[i]=nums[i-1]*preProd[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            sufProd[i]=sufProd[i+1]*nums[i+1]
        
        res = [i*j for i,j in zip(preProd,sufProd)]
        return res
