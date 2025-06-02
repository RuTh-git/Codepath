def build_cookie_tree(descriptions):
    if not descriptions: 
        return None
    
    root = TreeNode(descriptions[0][0], None, None)
    for instructions in descriptions:

        def find_cookie(node, target):
            # print("Cur Node", node)
            cookie = None
            if node.val == target:
                return node
            
            if node.left:
                cookie = find_cookie(node.left, target)
            
            if cookie: 
                # print("FOUND:", cookie)
                return cookie

            if node.right:
                return find_cookie(node.right, target)

        # find node that we're inserting at
        # print("target:",instructions[0])
        insert_node = find_cookie(root, instructions[0])

        if instructions[2]: insert_node.left = TreeNode(instructions[1], None, None)
        else: insert_node.right = TreeNode(instructions[1], None, None)
    return root