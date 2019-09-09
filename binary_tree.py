#Binary Tree

class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None


class binary_search_tree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)
            
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
                cur_node.left_child.parent=cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
                cur_node.right_child.parent=cur_node
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
            
    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)
            
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0
        
    def _height(self,cur_node,cur_height):
        if cur_node==None:
            return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)

    def delete_value(self,value):
        return self.delete_node(self.find(value))
    
    def delete_node(self, node):
        #returns node w/ min value in tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current
        #returns number of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child!=None:
                num_children+=1
            if n.right_child!=None:
                num_children+=1
            return num_children

        node_parent=node.parent #get parent of node to be deleted
        node_children=num_children(node) #get number of children of node to be deleted

        #break operation into 3 cases based on structure of tree &
        #node to be deleted

        #CASE1
        if node_children==0:
            #remove reference to node from parent
            if node_parent.left_child==node:
                node_parent.left_child=None
            else:
                node_parent.right_child=None

        #CASE 2 (node has a single child)
        if node_children==1:
            #get single child node
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            #replace node to be deleted with its child
            if node_parent.left_child==node:
                node_parent.left_child=child
            else:
                node_parent.right_child=child

            #correct parent pointer in node
            child.parent=node_parent

        #CASE 3 (node has two children)
        if node_children==2:
            #get inorder successor of the deleted node
            successor=min_value_node(node.right_child)

            #copy inorder successor's value to node formerly
            #holding the value we wished to be delete
            node.value=successor.value

            #delete the inorder successor now that it's value was
            #copied into the other node
            self.delete_node(successor)
            
            
            
            
        
       
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None: 
            return self._search(value,cur_node.right_child)
        return False
    
    
def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.print_tree()

print("tree height: "+str(tree.height()))

print(tree.search(10))
print(tree.search(30))
