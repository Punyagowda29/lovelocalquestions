# create a class TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None): #initialise or set the dfault value of left and right as 0
        self.val = val
        self.left = left
        self.right = right

def lowest_ancestor(root, p, q): #here p and q are in different subtrees
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root

# Function to build a BST from a list of values
def bst(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0]) if nodes[0] is not None else None
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)

        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)

        i += 1

    return root

# Example usage:
user_input = input("Enter the values of the BST nodes ")
tree_nodes = [int(x) if x != 'null' else None for x in user_input.split(",")] #takes none value as null in the input
bst_root =bst(tree_nodes)
p_value = int(input("value of node p: "))
q_value = int(input("value of node q: "))
p_node = TreeNode(p_value)
q_node = TreeNode(q_value)
result = lowest_ancestor(bst_root, p_node, q_node)
print("Lowest Common Ancestor:", result.val if result else None)
