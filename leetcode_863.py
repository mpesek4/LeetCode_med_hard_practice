class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distanceK(root, target, K):
    def rec2(current):
        if current is not None:
            if type(current.val) == int:
                rec2(current.left)
                rec2(current.right)
                return
            current.val = current.val[0]
            rec2(current.left)
            rec2(current.right)
        
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
    
    def dfs(current, moves_left):
        if current in explored:
            return
        explored[current] = 1
        if current is None:
            return
        if moves_left == 0:
            current.val = current.val[0]
            answer.append(current)
            return
        children = [current.left,current.right,current.val[1]]
        
        for child in children:
            dfs(child, moves_left-1)
            
    dfs(target, K)
    rec2(root)
    
    
    return answer[0:]

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