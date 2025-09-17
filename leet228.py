class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i=1
        j=0
        result=[]
        start=nums[0]
        end=nums[0]
        while i<len(nums):
            if end+1==nums[i]:
                end=nums[i]
            elif start==end:
                result.append(str(end))
                start=nums[i]
                end=nums[i]
            else:
                result.append(str(start)+"->"+str(end))
                start=nums[i]
                end=nums[i]
            i+=1
        # Add the last range
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
        return result




        
