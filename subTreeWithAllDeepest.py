class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithAllDeepest(root):

    def rec(curr_node,depth):
        if curr_node is None:
            return depth
        old_val = curr_node.val

        curr_node.val = [depth,depth, old_val]

        curr_node.val[0] = rec(curr_node.left,depth+1)

        curr_node.val[1] = rec(curr_node.right,depth+1)

        return max(curr_node.val[0],curr_node.val[1])

    rec(root, 0)

    myQ = [root]

    current_max = -1
    current_idx = -1
    while len(myQ) > 0:
        curr = myQ.pop(0)
        if curr.val[0] == curr.val[1]:
            if curr.val[0] > current_max:
                current_max = curr.val[0]
                current_idx = curr
        curr.val = curr.val[2]
        if curr.left is not None:
            myQ.append(curr.left)
        if curr.right is not None:
            myQ.append(curr.right)
    return current_idx

n7 = TreeNode(7,None,None)
n6 = TreeNode(6,None,None)
n0 = TreeNode(0,None,None)
n8 = TreeNode(8,None,None)
n4 = TreeNode(4,None,None)

n2 = TreeNode(2,n7,n4)
n5 = TreeNode(5,n6,n2)
n1 = TreeNode(1,n0,n8)
n3 = TreeNode(3,n5,n1)

print(subtreeWithAllDeepest(n3))