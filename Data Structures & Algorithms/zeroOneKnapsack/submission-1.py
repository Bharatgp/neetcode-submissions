class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        rows,cols = len(weight),capacity+1
        prevRow = [0]*cols


        
        #Since for item 0 we dont have option to compare as there are no items except this one, So we fill it to avoid extra conditions 

        for c in range(1,cols,1):
            if c - weight[0] >=0:
                prevRow[c] = profit[0]
        
        # our main code : Basically here we will fill the values as : max(skip_current,include_current) for which we will need previous row 

        for r in range(1,rows,1):
            currRow = [0]*cols
            for c in range(1,cols,1):
                
                #case 1 skip
                skip = prevRow[c]

                #case 2 include current item
                include = 0

                #when can we include capacity > weight[r]
                if c-weight[r]>=0:
                    include = profit[r] + prevRow[c-weight[r]]
                currRow[c] = max(skip,include)
            prevRow = currRow
        return prevRow[-1]
            

