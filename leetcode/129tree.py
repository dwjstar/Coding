class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumNumbers(self, root: TreeNode) -> int:
    def dfs(preroot, pretotal):
        if not preroot:
            return 0
        pretotal = pretotal * 10 + preroot.val
        if not preroot.left and not preroot.right:
            return pretotal
        else:
            return dfs(preroot.left, pretotal) + dfs(preroot.right, pretotal)

    total = dfs(root, 0)
    return total


if __name__ == '__main__':
    pass
