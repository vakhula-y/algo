class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, None)
        self.NIL.color = "black"
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, value, priority):
        node = Node(value, priority)
        node.left = self.NIL
        node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.priority >= current.priority:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.priority >= parent.priority:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == "red":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def peek_max(self):
        if self.root == self.NIL:
            return None
        return self.minimum(self.root).value

    def delete_max(self):
        if self.root == self.NIL:
            return None
        node = self.minimum(self.root)
        removed_value = node.value
        self.delete_node(node)
        return removed_value

    def delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.maximum(z.left)
            y_original_color = y.color
            x = y.left
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.left)
                y.left = z.left
                y.left.parent = y
            self.transplant(z, y)
            y.right = z.right
            y.right.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == "black" and s.right.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.right.color == "black":
                        s.left.color = "black"
                        s.color = "red"
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "red":
                    s.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == "black" and s.left.color == "black":
                    s.color = "red"
                    x = x.parent
                else:
                    if s.left.color == "black":
                        s.right.color = "black"
                        s.color = "red"
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "black"
                    s.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def inorder(self, node, result):
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append((node.value, node.priority))
            self.inorder(node.right, result)

    def view(self):
        result = []
        self.inorder(self.root, result)
        return result


if __name__ == "__main__":
    pq = RedBlackPriorityQueue()

    pq.insert("A", 1)
    pq.insert("B", 10)
    pq.insert("C", 5)

    print(pq.view())
    print(pq.peek_max())
    print(pq.delete_max())
    print(pq.view())
