class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[float('-inf')]+nums
        curr=(len(self.heap)-1)//2
        while curr>0:
            i=curr
            while i*2<len(self.heap):
                if (2*i+1<len(self.heap)) and (self.heap[2*i+1]<self.heap[2*i]) and (self.heap[2*i+1]<self.heap[i]):
                    tmp=self.heap[i]
                    self.heap[i]=self.heap[2*i+1]
                    self.heap[2*i+1]=tmp
                    i=2*i+1
                elif self.heap[i]>self.heap[2*i]:
                    tmp=self.heap[i]
                    self.heap[i]=self.heap[2*i]
                    self.heap[2*i]=tmp
                    i=2*i
                else:
                    break

            curr-=1
        self.k=k
        while len(self.heap)-1>self.k:
            self.pop()
    
    def helper(self,i):
        while i*2<len(self.heap):
                if (2*i+1<len(self.heap)) and (self.heap[2*i+1]<self.heap[2*i]) and (self.heap[2*i+1]<self.heap[i]):
                    tmp=self.heap[i]
                    self.heap[i]=self.heap[2*i+1]
                    self.heap[2*i+1]=tmp
                    i=2*i+1
                elif self.heap[i]>self.heap[2*i]:
                    tmp=self.heap[i]
                    self.heap[i]=self.heap[2*i]
                    self.heap[2*i]=tmp
                    i=2*i
                else:
                    break

    def pop(self):
        if len(self.heap)==1:
            return None
        if len(self.heap)==2:
            return self.heap.pop()
        res=self.heap[1]
        self.heap[1]=self.heap.pop()
        i=1
        self.helper(i)
        return res


    def add(self, val: int) -> int:
        self.heap.append(val)
        i=len(self.heap)-1
        while self.heap[i]<self.heap[i//2]:
            tmp=self.heap[i]
            self.heap[i]=self.heap[i//2]
            self.heap[i//2]=tmp
            i=i//2
        if len(self.heap)-1>self.k:
            self.pop()
        return self.heap[1]
        
