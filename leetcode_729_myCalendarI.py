
#https://leetcode.com/problems/my-calendar-i/

class MyCalendar(object):

    def __init__(self):
        self.bookings = []


    def book(self, start, end):
        if len(self.bookings) == 0:
            self.bookings.append((start,end))
            return True

        # our binary search returns the first booking smaller than our proposed booking, so if there are none smaller this is an edge case that is handled here
        if start < self.bookings[0][0]:
            if end > self.bookings[0][0]:
                return False
            self.bookings.append((start,end))
            self.bookings.sort()
            return True

        # to make sure a new booking is good, it must not interfere with the closest booking to its left which is returned in our binarySearch function
        closest = self.binarySearch(start)
        idx = self.bookings.index(closest)

        if closest[1] > start and closest[0] < end:
            return False

        # we also need to check the first booking larger than our proposed booking if such a booking exists
        if len(self.bookings) >= idx+2:
            one_bigger = self.bookings[idx+1]
            if end > one_bigger[0]:
                return False
        self.bookings.append((start,end))
        self.bookings.sort()
        return True


    def binarySearch(self,start):
        l = 0
        r = len(self.bookings)-1

        closest = self.bookings[r]

        while l<r:
            m = (l+r) // 2
            if self.bookings[m][0] > start:
                r = m
            else:
                closest = self.bookings[m]
                l = m +1
        return self.bookings[l] if self.bookings[l][0] < start else closest