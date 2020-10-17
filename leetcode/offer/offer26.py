class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    if not A and not B:
        return True
    if not A or not B:
        return False

    def back(A_, B_):
        if not A_ and not B_:
            return True
        if A_ and not B_:
            return True
        if not A_ and B_:
            return False
        if A_.val == B_.val:
            return back(A_.left, B_.left) and back(A_.right, B_.right)
        else:
            return False

    q = []
    q.append(A)
    flag = False
    while q:
        tmp = q.pop(0)
        if tmp.val == B.val:
            flag = back(tmp, B)
            if flag:
                return True
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)
    return flag

if __name__=='__main__':
    l=[3,4,5,1,2]
    b=[4,1]
    root=TreeNode(3)
    root.left=TreeNode(4)
    root.right=TreeNode(5)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(2)
    b_root=TreeNode(4)
    b_root.left=TreeNode(1)
    flag=isSubStructure(root,b_root)
    print(flag)