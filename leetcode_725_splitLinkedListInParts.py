
# https://leetcode.com/problems/split-linked-list-in-parts/


# my solution was missing an edge case and passing 39/41, this solution was inspired by another submission
def splitListToParts(root, k):
    answer = []
    list_length = 0
    
    current = root
    while current is not None:
        list_length+=1
        current = current.next
        
    
    smaller_segments,larger_segments = list_length // k, list_length % k

    # once we know the size of our segments, we can create an array that just stores the size of our segments
    answer =  [smaller_segments + 1] * larger_segments + [smaller_segments] * (k - larger_segments)
    
    prev, curr = None, root
    for index, num in enumerate(answer):
        # at start and aftger every segment, we make the previous segment no longer connected to the one we are about to create
        if prev:
            prev.next = None
        answer[index] = curr
        # we stored the sizes ofe ach segment, so now we just move that many nodes forward until it is time to break off a segment
        for i in range(num):
            prev, curr = curr, curr.next
    return answer