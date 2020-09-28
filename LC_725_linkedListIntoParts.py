
# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def splitListToParts(self,root, k):
        answer = []
        list_length = 0

        current = root
        
        while current is not None:
            list_length+=1
            current = current.next
        # tricky part is figuring out which lists will be longer than k by 1,
        # larger is the remainer, smaller is k - larger
        smaller_segments,larger_segments = list_length // k, list_length % k
        answer =  [smaller_segments + 1] * larger_segments + [smaller_segments] * (k - larger_segments)

        prev, curr = None, root
        
        for index, num in enumerate(answer):
            # for each segment we need to update the last one to point to none
            if prev:
                prev.next = None
            answer[index] = curr
            # get to the right place for next segment
            for i in range(num):
                prev, curr = curr, curr.next
                
                
                
        return answer