class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)
        for i in range(len(inorder)):
            if inorder[i]==root_val:
                index=i
                break
        root_in_left=inorder[:index]
        root_in_right=inorder[index+1:]
        root_pre_left=preorder[1:1+index]
        root_pre_right=preorder[1+index:]
        root_left=self.buildTree(root_pre_left,root_in_left)
        root_right=self.buildTree(root_pre_right,root_in_right)
        root.left=root_left
        root.right=root_right
        return root

if __name__=='__main__':
    pre=[3,9,20,15,7]
    ino=[9,3,15,20,7]
    s=Solution()
    root=s.buildTree(pre,ino)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)