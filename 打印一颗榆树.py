tree_height = 5
tree_leaves = [" " * (tree_height - i - 1) + "*" * (2*i + 1) for i in range(tree_height)]

# 打印树冠
for leaf in tree_leaves:
    print(leaf)

# 打印树干
trunk_width = 3
trunk_position = (2*tree_height + 1 - trunk_width) // 2
for i in range(tree_height):
    if i == tree_height // 2:
        print(f"{' ' * trunk_position}{'*' * trunk_width}")
    else:
        print(" " * (tree_height - 1))