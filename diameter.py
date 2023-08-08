import pytest

from typing import Optional, Tuple

class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

def diameter(root: Optional[TreeNode]) -> int:
    """Length of longest path in tree."""

    # Either
    # (1) Left has the longest path
    # (2) Right has the longest path
    # (3) Root is in the longest path in which case
    #     the length is max_depth(left) + max_depth(right)
    # We focus on case 3

    def dnd(root: Optional[TreeNode], current_depth: int) -> Tuple[int, int]:
        """Helper to find diameter.

        Returns:
            (diameter, depth)
        """
        if root is None:
            return (0, current_depth)
        if not root.left and not root.right:
            return (0, current_depth)

        # bug, left_depth and right_depth compute
        # the depth from the root but it should
        # be depth from current
        if root.left:
            left_diameter, left_depth = dnd(root.left, current_depth + 1)
        else:
            left_diameter, left_depth = 1, current_depth
        if root.right:
            right_diameter, right_depth = dnd(root.right, current_depth + 1)
        else:
            right_diameter, right_depth = 1, current_depth
        left_depth -= current_depth
        right_depth -= current_depth
        
        max_diam = max(left_diameter, right_diameter, left_depth + right_depth)
        depth = max(left_depth, right_depth)
        print(f"{root.val=},{left_diameter=},{right_diameter=},{left_depth=},{right_depth=},{max_diam=}")
        return max_diam, depth
    ret, _ = dnd(root, 0)
    return ret

def test_empty():
    assert diameter(None) == 0

def test_single():
    assert diameter(TreeNode(val=0)) == 0

def test_one_child():
    assert diameter(TreeNode(val=1, left=TreeNode(val=2))) == 1
    assert diameter(TreeNode(val=1, right=TreeNode(val=2))) == 1

def test_two_children():
    assert diameter(
        TreeNode(val=1,
            left=TreeNode(val=2),
            right=TreeNode(val=3),
        )
    ) == 2

def test_longest_path_does_not_contain_root():
    assert diameter(
        TreeNode(val=1,
            left=TreeNode(val=2,
                left=TreeNode(val=3,
                    left=TreeNode(val=4)),
                right=TreeNode(val=5))
        )
    ) == 3

pytest.main()
