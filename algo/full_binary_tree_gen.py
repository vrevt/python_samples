from functools import cache
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        x = self
        rep = []
        def dfs(node, ind, prev):
            rep.append((ind, prev))
            if node.left:
                dfs(node.left, ind + 1, 'left')
            if node.right:
                dfs(node.right, ind + 1, 'right')

        dfs(x, 0, 'root')
        ans = ''
        for node in rep:
            ans = ans + ' ' + node[1] + str(node[0])

        return ans
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]

        result = []
        for i in range(1, n - 1, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - 1 - i):
                    result.append(TreeNode(0, left, right))

        return result


if __name__ == '__main__':
    sol = Solution()
    n = 7
    print(sol.allPossibleFBT(n))
