class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.doubles = []
        self.bookingsTemp = []
    def check_double(self, start, end):
        if len(self.doubles) == 0:
            return True

        # our binary search returns the first booking smaller than our proposed booking, so if there are none smaller this is an edge case that is handled here
        if start < self.doubles[0][0]:
            if end > self.doubles[0][0]:
                return False

            return True
        # to make sure a new booking is good, it must not interfere with the closest booking to its left which is returned in our binarySearch function
        closest = self.binarySearchDoubles(start)
        idx = self.doubles.index(closest)

        if closest[1] > start and closest[0] < end:
            return False

        # we also need to check the first booking larger than our proposed booking if such a booking exists
        if len(self.doubles) >= idx+2:
            one_bigger = self.bookings[idx+1]
            if end > one_bigger[0]:
                return False
        # self.doubles.append((start,end))
        self.doubles.sort()
        return True


    def updateDoubleBooking(self, start, end, curr_idx):
        if self.check_double(start,end) == False:
            return False

        current_booking = self.bookings[curr_idx]

        prev_end = -1
        while  current_booking[0] < end:
            if prev_end != -1:
                start = self.bookings[prev_end][1]
                if start < current_booking[0]:
                    self.bookingsTemp.append((start,current_booking[0]))
                    self.bookingsTemp.sort()
                    start = current_booking[0]
            if current_booking[1] > end:
                self.doubles.append((start, end))
                self.doubles.sort()
                self.bookings = self.bookings+ self.bookingsTemp
                self.bookingsTemp = []
                self.bookings.sort()
                return True
            else:
                if start < current_booking[1]:
                    start = max(start,current_booking[0])
                    self.doubles.append((start, current_booking[1]))
                    self.doubles.sort()
                    start = current_booking[1]

            prev_end = curr_idx
            curr_idx+=1
            if curr_idx == len(self.bookings):
                break
            else:
                current_booking = self.bookings[curr_idx]

        #we have a leftover segment that is a single booking instead of a double booking
        if self.bookings[prev_end][1] >= end:
            self.bookings = self.bookings+ self.bookingsTemp
            self.bookingsTemp = []
            self.bookings.sort()
            return True
        self.bookings.append((self.bookings[prev_end][1],end))
        self.bookings = self.bookings+ self.bookingsTemp
        self.bookingsTemp = []
        self.bookings.sort()

        return True

    def book(self, start, end):
        if len(self.bookings) == 0:
            self.bookings.append((start,end))
            return True

        if start < self.bookings[0][0]:
            if end > self.bookings[0][0]:
                return self.updateDoubleBooking(start,end, 0)

            self.bookings.append((start,end))
            self.bookings.sort()
            return True

        closest = self.binarySearch(start)
        idx = self.bookings.index(closest)

        if closest[1] > start and closest[0] < end:
            return self.updateDoubleBooking(start,end, idx)

        if len(self.bookings) >= idx+2:
            one_bigger = self.bookings[idx+1]
            if end > one_bigger[0]:
                return self.updateDoubleBooking(start,end,idx)

        self.bookings.append((start,end))
        self.bookings.sort()
        return True

    def binarySearchDoubles(self,start):
        l = 0
        r = len(self.doubles)-1

        closest = self.doubles[r]

        while l<r:
            m = (l+r) // 2
            if self.doubles[m][0] > start:
                r = m
            else:
                closest = self.doubles[m]
                l = m +1
        return self.doubles[l] if self.doubles[l][0] < start else closest
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