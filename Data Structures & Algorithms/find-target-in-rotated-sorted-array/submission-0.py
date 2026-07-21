class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low <= high):
            m = (high+low)//2
            if(nums[m] == target):
                return m
            if(nums[low] <= nums[m]):
                if( nums[low] <= target < nums[m]):
                    high = m-1
                else:
                    low = m+1
            else:
                if(nums[m] < target <= nums[high]):
                    low = m + 1
                else:
                    high = m - 1
        return -1