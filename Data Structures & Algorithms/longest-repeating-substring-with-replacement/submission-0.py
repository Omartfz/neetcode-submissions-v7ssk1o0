class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequence=defaultdict(int)
        max_count=0
        left=0
        best=0
        for right in range (len(s)):
            frequence[s[right]]+=1
            max_count=max(max_count,frequence[s[right]])

            while (right-left+1)-max_count>k:
                frequence[s[left]]-=1
                left+=1
            best=max(best,right-left+1)
        return best




        