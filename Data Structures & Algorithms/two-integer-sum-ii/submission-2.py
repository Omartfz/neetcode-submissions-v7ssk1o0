class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while left<right:
            somme=numbers[right]+numbers[left]
            if somme==target:
                return [left+1,right+1]
            elif somme<target:
                left+=1
            elif somme>target:
                right-=1
        return []

