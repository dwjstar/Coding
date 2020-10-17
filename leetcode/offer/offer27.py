class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirrorTree( root: TreeNode) -> TreeNode:
    if not root:
        return
    root.left,root.right=root.right,root.left
    mirrorTree(root.left)
    mirrorTree(root.right)
    return root

if __name__=='__main__':
    l=[4,2,7,1,3,6,9]
    root=TreeNode(l[0])
    l1=TreeNode(l[1])
    l2=TreeNode(l[2])
    l3=TreeNode(l[3])
    l4=TreeNode(l[4])
    l5=TreeNode(l[5])
    l6=TreeNode(l[6])
    root.left=l1
    root.right=l2
    l1.left=l3
    l1.right=l4
    l2.left=l5
    l2.right=l6
    mirrorTree(root)
    q=[]
    q.append(root)
    while q:
        tmp=q.pop(0)
        print(tmp.val)
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)


