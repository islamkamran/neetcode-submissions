"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            # we have to compare the current start with the previous end so better we start from the second postion
            m1 = intervals[i-1]  # previous meeting
            m2 = intervals[i]    # Current meeting

            # we can do this in the m1 and m2 but lets do the start and end here
            if m1.end > m2.start:
                return False
        
        return True
