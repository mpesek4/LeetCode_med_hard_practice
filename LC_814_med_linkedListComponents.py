
#https://leetcode.com/contest/weekly-contest-80/problems/linked-list-components/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def numComponents(head, G):
    curr = head
    dp = {}
    # create a dictionary storing the next values of all nodes
    while curr:
        if curr.next:
            dp[curr.val] = curr.next.val
        curr = curr.next
    
    ans = len(G)
    # assume at start no components are connected
    # if a node in G has a connection in G, we know they are in a connected component so we decrement answer
    for item in G:
        if item in dp and dp[item] in G:
            ans-=1
    return ans