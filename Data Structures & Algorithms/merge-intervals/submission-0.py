class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : (x[0],x[1]) )
        
        st,ed = intervals[0]
        res = []

        for start,end in intervals[1:]:
            if(ed >= start):
                ed = max(ed,end)
            else:
                res.append([st,ed])
                st,ed = start, end
        res.append([st,ed])                
        return res                                
