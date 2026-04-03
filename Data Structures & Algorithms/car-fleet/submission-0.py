class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        tab=[]
        for i in range (len(position)):
            tab.append((position[i],speed[i]))
        tab.sort(reverse=True)
        for i in range(len(tab)):
            stack.append((target-tab[i][0])/tab[i][1])
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        


        