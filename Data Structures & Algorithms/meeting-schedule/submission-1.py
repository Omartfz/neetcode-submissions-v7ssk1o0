"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # La signature de la fonction indique bien une liste d'objets Interval
    def canAttendMeetings(self, intervals: List['Interval']) -> bool:
        
        # 1. On utilise x.start au lieu de x[0] pour le tri
        intervals.sort(key=lambda x: x.start)
        
        for i in range(len(intervals) - 1):
            
            # 2. On utilise .end et .start au lieu des crochets [1] et [0]
            if intervals[i].end > intervals[i+1].start:
                return False
                
        return True