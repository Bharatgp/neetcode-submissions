class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        suffixProduct = []
        tmp = 1
        for i in range(len(nums)):
            tmp = tmp*nums[i]
            prefixProduct.append(tmp)
        tmp = 1            
        for i in range(len(nums)-1, -1 ,-1):
            tmp = tmp*nums[i]
            suffixProduct.append(tmp)            
        suffixProduct = suffixProduct[::-1] 
        res = []
        for i in range(len(nums)):
            if(i == 0):
                res.append(suffixProduct[i+1])
            elif(i==len(nums)-1):
                res.append(prefixProduct[i-1])
            else:
                res.append(suffixProduct[i+1]*prefixProduct[i-1])
        return res