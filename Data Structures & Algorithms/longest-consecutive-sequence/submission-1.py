class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        dic={}
        nums.sort()

        for num in nums:
            if num-1 in dic:
                dic[num]=dic[num-1]+1
            else:
                dic[num]=1    
            print (dic)  
        return max(value for value in dic.values())
