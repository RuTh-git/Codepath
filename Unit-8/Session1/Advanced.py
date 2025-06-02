'''
Problem 1: Ivy Cutting

Binary Tree - print root till rightmost node - Iterative

Time - O(h) - h is the height of the tree
Space - O(h) 
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    res = []
    current = root
    while current:
        res.append(current.val)
        if current.right:
            current = current.right
        else:
            break
    return res

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

'''
Problem 2: Ivy Cutting II

Binary tree - print right branch - recursive

Time - O(h) - h is the height of the tree
Space - O(h) - recursion stack will use space a/c to height of the tree
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if root is None:
        return []
    return [root.val] + right_vine(root.right)

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

'''
Problem 3: Pruning Plans

Post order traversal

Time - O(n)
Space - O(h) - height of the tree due to the recursive call stack
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if root is None:
        return []
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

'''
Problem 4: Sum Inventory

Add all elements in the binary tree

Time - O(n)
Space - O(h)
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    if inventory is None:
        return 0
    total = inventory.val 
    total += sum_inventory(inventory.left)
    total += sum_inventory(inventory.right)
    return total

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))

'''
Problem 5: Calculating Yield II

Time - O(n) - algorithm needs to visit each node in the tree to evaluate the expression.
Space - O(h) - height of the tree - due to the recursive call stack.
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.left is None and root.right is None:
        return root.val
    
    # recursively calculate the yield of the left and right subtrees
    left_yield = calculate_yield(root.left)
    right_yield = calculate_yield(root.right)

    # Apply the operation at the current node
    if root.val == "+":
        return left_yield + right_yield
    elif root.val == "-":
        return left_yield - right_yield
    elif root.val == "*":
        return left_yield * right_yield
    elif root.val == "/":
        return left_yield / right_yield

"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

'''
Problem 6: Plant Classifications

Time - O(n)
Space - O(h)
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(taxonomy):
    if taxonomy is None:
        return []
    if taxonomy.left is None and taxonomy.right is None:
        return [taxonomy.val]
    return get_most_specific(taxonomy.left) + get_most_specific(taxonomy.right)

"""
           Plantae
          /       \
         /         \
        /           \ 
Non-flowering     Flowering
   /      \       /        \
Mosses   Ferns Gymnosperms Angiosperms
                             /     \
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))

'''
Problem 7: Count Old Growth Trees

Time - O(n)
Space - O(h)
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    left_count = count_old_growth(root.left, threshold)
    right_count = count_old_growth(root.right, threshold)

    if root.val > threshold:
        return 1 + left_count + right_count
    else:
        return left_count + right_count

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))

'''
Problem 8: Twinning Trees
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root1 or not root2:
        return False
    if root1.val == root2.val:
        return True
    else:
        return False
    return is_identical(root1.left, root2.left)

   

"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))