class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = 1
        cnt_o = 0
        for num in nums:
            if num!=0:
                prd = num * prd
            if num == 0:
                cnt_o += 1
        if cnt_o > 1:
            return [0 for i in nums]
        if cnt_o == 1:
            op = []
            for i in nums:
                if i == 0 :
                    op.append(prd)
                else:
                    op.append(0)
            return op
        if cnt_o == 0:
            return [int(prd/num) for num in nums]