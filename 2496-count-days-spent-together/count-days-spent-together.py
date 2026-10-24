class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if start > end:
            return 0
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def d(s):
            m, day = map(int, s.split('-'))  
            return sum(days[:m-1]) +day   #converting daate to day nunmber 
        return d(end) - d(start) +1      