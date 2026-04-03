class Solution:
    def longestPalindrome(self, s: str) -> str:
        word=""
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if len(word)<right-left+1:
                    word=s[left:right+1]
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if len(word)<right-left+1:
                    word=s[left:right+1]
                left-=1
                right+=1
        return word
                


























        """
        res=""
        resLen=0


        for i in range (len(s)):
            
                l,r=i,i
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>resLen:
                        res=s[l:r+1]
                        resLen=r-l+1
                    l-=1
                    r+=1
            
                l,r=i,i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>resLen:
                        res=s[l:r+1]
                        resLen=r-l+1
                    l-=1
                    r+=1
        return res"""



            
        