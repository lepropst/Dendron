
from binary_search_tree import BSTNode
from binary_search import binary_search
from avl_tree import AVLTree


def run_tree_inserts(root: BSTNode, arr: list) -> None:
    for a in arr:
        print(f"inserting {a}")
        root.insert(a)


def run_tree_deletes(root: BSTNode, arr: list):
    for a in arr:
        print(f"deleting {a}")
        root.delete(a)


def run_binary_search(item: int or str, arr: list) -> int:
    return binary_search(arr, 0, len(arr)-1, item)


def main():
    avlTree = AVLTree()
    inlist = ["E","L", "I", "A", "S", "R", "N", "G", "J"]
    for i in inlist:
        print("Inserting {i} into the tree: ")
        avlTree.print_tree(f"Inserting {i} into the tree: ", f"first/inserting_{i}")
        avlTree.insert(i)
        avlTree.print_tree(f"After inserting {i} into the tree: ", f"first/inserting_{i}")

        avlTree.rebalance( f"first/inserting_{i}")

        avlTree.print_tree("After balancing", f"first/balancing{i}")


    inlist = ["R","A", "N", "G", "E", "L", "I", "S", "J"]
    avlTree = AVLTree()
    for x in inlist:
        print(f"Inserting {x} into the tree: ")
        avlTree.print_tree(f"Inserting {x} into the tree: ", f"second/inserting_{x}")
        avlTree.insert(x)
        avlTree.print_tree(f"After inserting {x}", f"second/inserting_{x}")
        avlTree.rebalance(f"second/inserting_{x}")

        avlTree.print_tree(f"After balancing", f"second/balancing{x}")


    print("Inorder traversal:", avlTree.inorder_traverse())
    print("Postorder traversal:", avlTree.postorder_traverse())
    for x in range(3):
        if avlTree.node:
            avlTree.print_tree(f"Deleting {avlTree.node.key}",f"deleting_{x}")
            avlTree.delete(avlTree.node.key, f"delete/{x}")
            avlTree.print_tree(f"Done deleting {avlTree.node.key}",f"delete/{x}/done_deleting_{x}")
            avlTree.rebalance(f"delete/{x}")
            avlTree.print_tree(f"done_balancing_{avlTree.node.key}", f"delete/{x}/done_balancing_{x}")
        else:
            print(avlTree.node)
# Insert at least the first 9 unique letters from your name (all in uppercase) into an AVL tree, one at a time, in order, re-balancing as necessary.
# This time, start with the first letter of your last name and use all unique letters from your last name, in order.
# ( Proceed through your first and middle name, as necessary, to get enough unique letters).
# For each insertion state the letter you are inserting.
# If the insertion requires re-balancing, show the tree both before and after the rotation, and identify the type of rotation that was used.
# Provide the order that your tree nodes would be visited, using a pre-order traversal.
# Provide the order that your tree nodes would be visited, using a post-order traversal.
# Using the AVL tree you created, repeat the following three times, as follows:
# Delete the root node, replacing it with a node from the left subtree (unless there is no left subtree).
# If rotation for re-balancing, show the tree before and after the rotation, and identify the type of rotation that was used.


# Usage example
# if __name__ == "__main__":
#     a = AVLTree()
#     print ("----- Inserting -------")
#     #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
#     inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
#     for i in inlist:
#         a.insert(i)

#     a.display()

#     print ("----- Deleting -------")
#     a.delete(3)
#     a.delete(4)
#     # a.delete(5)
#     a.display()

#     print ()
#     print ("Input            :", inlist )
#     print ("deleting ...       ", 3)
#     print ("deleting ...       ", 4)
#     print ("Inorder traversal:", a.inorder_traverse())


if __name__ == "__main__":
    main()
