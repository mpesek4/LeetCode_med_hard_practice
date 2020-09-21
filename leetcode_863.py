class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distanceK(self,root, target, K):
        ''' since we need to go down and up the tree from our target, I felt it was better to turn the tree into a graph
        the rec function just connects every node to its parent in a dictionary called connection_dict so we don't modify our tree'''
        def rec(current, parent):
            if current is None:
                return
            old_val = current.val
            # current.val = [old_val, parent]
            connection_dict[current] = parent
            rec(current.left,current)
            rec(current.right,current)



        connection_dict = {}
        rec(root, None)

        answer = []
        explored = {}
        ''' now that our tree is a graph, just do a DFS keeping track of explored nodes and stopping if we are more edges away than our target variable'''
        def dfs(current, moves_left):
            if current in explored:
                return
            explored[current] = 1
            if current is None:
                return
            if moves_left == 0:
                answer.append(current.val)
                return
            children = [current.left,current.right,connection_dict[current]]

            for child in children:
                dfs(child, moves_left-1)

        dfs(target, K)



        return answer  ''' time complexity is O(V+E) and will be worse the more connected the graph is, space is the height of the tree for DFS'''

n7 = TreeNode(7,None,None)
n6 = TreeNode(6,None,None)
n0 = TreeNode(0,None,None)
n8 = TreeNode(8,None,None)
n4 = TreeNode(4,None,None)

n2 = TreeNode(2,n7,n4)
n5 = TreeNode(5,n6,n2)
n1 = TreeNode(1,n0,n8)
n3 = TreeNode(3,n5,n1)

print(distanceK(n3, n5, 2))