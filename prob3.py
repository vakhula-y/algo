import os

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        canvas = [[" "] * 100 for _ in range(40)]

        def draw(node, r, c, dir_x, h_step, v_step):
            if not node:
                return

            for i, char in enumerate(str(node.value)):
                canvas[r][c + i] = char

            if node.left:
                canvas[r - max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "\\" if dir_x == -1 else "/"
                draw(node.left, r - v_step, c + dir_x * h_step,
                     dir_x, max(2, h_step - 2), max(2, v_step // 2))

            if node.right:
                canvas[r + max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "/" if dir_x == -1 else "\\"
                draw(node.right, r + v_step, c + dir_x * h_step,
                     dir_x, max(2, h_step - 2), max(2, v_step // 2))

        root_r = 18
        for i, ch in enumerate(str(self.value)):
            canvas[root_r][40 + i] = ch

        if self.left:
            canvas[root_r][36:39] = ["-", "-", "-"]
            draw(self.left, root_r, 34, -1, 6, 8)

        if self.right:
            canvas[root_r][42:45] = ["-", "-", "-"]
            draw(self.right, root_r, 46, 1, 6, 8)

        for row in canvas:
            line = "".join(row).rstrip()
            if line:
                print(line)

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.print_inorder()


def build_from_postorder(arr):
    if not arr:
        return None

    idx = [len(arr) - 1]

    def build():
        if idx[0] < 0:
            return None

        val = arr[idx[0]]
        idx[0] -= 1

        if val in ("N", "None", None):
            return None

        node = BinaryTree(int(val))

        node.right = build()
        node.left = build()

        return node

    return build()


def main():
    filename = "tree_data.txt"

    data_to_write = [
        "N", "N", 16, "N", "N", 17, 8, "N", "N", 18, 
        "N", "N", 19, 9, 4, "N", "N", 20, "N", 10, 
        "N", "N", 11, 5, 2, "N", "N", 12, "N", "N", 
        13, 6, "N", "N", 14, "N", "N", 15, 7, 3, 1
    ]

    with open(filename, "w") as f:
        f.write(" ".join(map(str, data_to_write)))

    with open(filename, "r") as f:
        loaded_data = f.read().strip().split()

    root = build_from_postorder(loaded_data)

    if root:
        root.print_tree()
        print("\nInorder обхід:")
        root.print_inorder()
        print("\n")
    else:
        print("Дерево порожнє")


if __name__ == "__main__":
    main()
