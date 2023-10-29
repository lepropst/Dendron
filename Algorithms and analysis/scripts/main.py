
import os
import queue
import shutil
import sys
import functools
from linked_list import LinkedList
from binary_search_tree import BSTNode
from binary_search import binary_search
from avl_tree import AVLTree
from json import load
from quadratic_hash_table import HashTable

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


def avl_discussion(data, dele=0):
    if os.path.exists("./graph_images/avl"):
        shutil.rmtree("./graph_images/avl")
    avlTree1 = AVLTree()
    inlist = data.get("data").get("array_1")
    inlist_2 = data.get("data").get("array_2")
    run_avl_inserts(avlTree=avlTree1, list=inlist, dir="second")
    del inlist
    del avlTree1

    avlTree = AVLTree()
    avlTree = run_avl_inserts(avlTree=avlTree, list=inlist_2, dir="first")
    print(f"Final Graph:\n<img src={"\"./graph_images/avl/second/root/Final Tree.png\""}/>")
    li = list()
    def func(node):
        if node is None:
            return []
        li =[]
        print(node.key)
        li+=node.key
        if node.left.node != None:
            li+=func(node.left.node)
        if node.right.node != None:
            li+=func(node.right.node)
        return [li]
    
    func(avlTree.node)
    print(li)
    print("\nInorder traversal:", avlTree.inorder_traverse())
    # print("\npreorder traversal:", avlTree.preorder_traverse())
    # print("\nPostorder traversal:", avlTree.postorder_traverse(avlTree.node))

    for x in range(3):
        print(f"{x}" + (functools.reduce(lambda a, b: a+b,["-"]* 10)))
        if avlTree.node:
            print("deleting")
            avlTree.print_tree(f"deleting {avlTree.node.key}",f"deleting_{x}")
            avlTree.delete(avlTree.node.key, f"delete/{x}")
            print("done_deleting")
            avlTree.print_tree(f"done_deleting {avlTree.node.key}",f"delete/{x}/done_deleting_{x}")
            avlTree.rebalance(f"delete/{x}")
            print("done_balancing_")
            avlTree.print_tree(f"done_balancing_{avlTree.node.key}", f"delete/{x}/done_balancing_{x}")
        else:
            print(avlTree.node)

def run_avl_inserts(avlTree, list, dir):
    for x in list:
        avlTree.print_tree(f"Inserting {x} into the tree", f"{dir}/inserting_{x}")
        print(f"Inserting {x} into the tree: ")
        if os.path.exists(os.path.join("./graph_images/avl", f"{dir}/inserting_{x}",f"Inserting {x} into the tree.png")):
            print(f"\n<img src={"\""}{os.path.join("./graph_images/avl", f"{dir}/inserting_{x}",f"Inserting {x} into the tree.png")}{"\""}/>")
        else: 
            print("<img><svg height='100' width='100'><circle cx='50' cy='50' r='40' stroke='black' stroke-width='3' fill='red' /></svg></img>")
        avlTree.insert(x)
        avlTree.print_tree(f"After inserting {x}", f"{dir}/inserting_{x}")
        print(f"After Inserting\n<img src={"\""}{os.path.join("./graph_images/avl", f"{dir}/inserting_{x}",f"After inserting {x}.png")}{"\""}/>")
        avlTree.rebalance(f"{dir}/inserting_{x}")
        avlTree.print_tree(f"After balancing {x}", f"{dir}/balancing_{x}")
        print(f"After balancing\n<img src={"\""}{os.path.join("./graph_images/avl", f"{dir}/balancing_{x}",f"After balancing {x}.png")}{"\""}/>\n")

    avlTree.print_tree("Final Tree", f"{dir}/root")
    return avlTree
def main():
    with open("data.json", "r") as f:
        data = load(f)
     
    # Generic main
    data_structure_choice = sys.argv[1]

    # Create the appropriate data structure
    if data_structure_choice == "array":
        data_structure = list()
    elif data_structure_choice == "linked_list":
        data_structure = LinkedList()
        pass
    elif data_structure_choice == "stack":
        data_structure = list()
        pass
    elif data_structure_choice == "queue":
        data_structure = queue.Queue()
        pass
    elif data_structure_choice == "hash_table":
        if len(sys.argv) >2:
            data_structure = HashTable(size=len(data.get("data_array")*2),modulo=sys.argv[2])
        else:
            data_structure = HashTable(size=len(data.get("data_array")*2),modulo=15)

    elif data_structure_choice == "bst":
        data_structure = BSTNode()
    elif data_structure_choice == "avl":
        data_structure = AVLTree() 
    elif data_structure_choice=="discussion":
        return avl_discussion(data)
    else:
        raise ValueError("Invalid data structure choice")
    
    # Insert the data from the JSON file into the data structure
    for item in data.get("data_array"):
        if data_structure_choice == "array":
            data_structure.append(item)
        elif data_structure_choice == "linked_list":
            data_structure.insert(item)
        elif data_structure_choice == "stack":
            data_structure.append(item)
        elif data_structure_choice == "queue":
            data_structure.put(item)
        # elif data_structure_choice == "hash_table":
        #     data_structure.insert(item)
        elif data_structure_choice == "bst":
            data_structure.insert(item)
        elif data_structure_choice == "avl":
            data_structure.insert(item)
    if data_structure_choice =="bst":
        data_structure.print_tree("final_tree", dir="final_tree")
        print(data_structure.inorder_traverse(list()))
        print(data_structure.preorder_traverse(list()))
        print(data_structure.postorder_traverse(list()))

    if data_structure_choice =="avl":
        data_structure.print_tree("final tree",dir="final_tree")
        print(data_structure._inorder_traverse(keys=list()))
        print(data_structure._preorder_traverse(keys=list()))
        print(data_structure._postorder_traverse(keys=list()))

    if data_structure_choice =="hash_table":
        data_structure.hash(arr=data.get("data_array"))
        data_structure.printArray()

    # if data_structure_choice == ("queue"):
    #     rnge = data_structure.qsize()
    #     # for i in range(rnge):
    #     #     print(data_structure.get(i), end=" ")
        
    if data_structure_choice == ("stack"):
        for item in range(len(data_structure)):
            print(data_structure[item], end=" ")
        
    for item in data.get("data_delete_array"):
        if data_structure_choice == "array":
            data_structure.remove(item)
        elif data_structure_choice == "linked_list":
            data_structure.remove_node(item)
        elif data_structure_choice == "stack":
            data_structure.pop()
            print(data_structure)
        elif data_structure_choice == "queue":
            print("TRYING TO DELETE")
            item= data_structure.get(timeout=0.1, block=False)
            print(f"DELETED {item}")
            print(data_structure)
        elif data_structure_choice == "hash_table":
            data_structure.delete(item)
        elif data_structure_choice == "bst":
            data_structure.delete(item)
        elif data_structure_choice == "avl":
            data_structure.delete(item, data_structure.node)


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




if __name__ == "__main__":
    main()
