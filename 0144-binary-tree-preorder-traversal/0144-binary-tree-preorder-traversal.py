# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def preorderTraversal(self, root: TreeNode | None) -> list[int]:
    ans = []

    def preorder(root: TreeNode | None) -> None:
      if not root:
        return

      ans.append(root.val)
      preorder(root.left)
      preorder(root.right)

    preorder(root)
    return ans