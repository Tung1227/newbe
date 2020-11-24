
class Node:
    def __init__(self, data,value):
        self.value = value
        self.data = data
        self.parents = []
        self.children = []
    def get_data(self):
        return self.data
    def get_value(self):
        return self.value
    def get_children(self):
        return [node.get_data() for node in self.children]
    def get_parents(self):
        return [node.get_data() for node in self.parents]
class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def clear(self):
        self.nodes = []
        self.edges = []
    def number_of_nodes(self):
        return len(self.nodes)
    def number_of_edges(self):
        return len(self.edges)
    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n.get_data() == node.get_data():
                return idx
        return -1
    def add_node(self, node_name,value):
        node = Node(node_name,value)
        if not self.is_contains(node):
            self.nodes.append(node)
    def add_node_from(self, array_of_nodes_name):
        for el in array_of_nodes_name:
            data = el[0]
            value = el[1]
            node = Node(data,value)
            if not self.is_contains(node):
                self.nodes.append(node)
    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False
    def add_edge(self, start_name, end_name):
        start_value = self.get_value_byName(start_name)
        end_value = self.get_value_byName(end_name)
        start_node = Node(start_name,start_value)
        end_node = Node(end_name,end_value)
        if not self.is_contains(start_node):
            self.add_node(start_name)
        if not self.is_contains(end_node):
            self.add_node(end_name)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(end_node)
        self.nodes[end_index].parents.append(start_node)
        self.edges.append((self.nodes[start_index], self.nodes[end_index]))
    def add_edges_from(self, array_of_tuple_node):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            self.add_edge(start, end)
    def show_nodes(self):
        return [node.get_data() for node in self.nodes]
    def show_edges(self):
        return [(edge[0].get_data(), edge[1].get_data()) for edge in self.edges]

    def get_children_value(self,node):
        NodeIndex = self.get_index(node)
        children_value = [node.get_value() for node in self.nodes[NodeIndex].children]
        return children_value
    def get_value_byName(self,name):
        for el in self.nodes:
            if name == el.get_data():
                return el.get_value()

def MaxValue(tree,node, alpha, beta):
    NodeIndex = tree.get_index(node)
    children_value = [node.get_value() for node in tree.nodes[NodeIndex].children]
    if len(children_value) == 0:
        return node.get_value()
    best = -10000
    for child in tree.nodes[NodeIndex].children:
        print(child.value)
        temp = MinValue(tree,child, alpha, beta)
        best = max(best,temp)
        if child.value>=beta:
            return child.value
        alpha = max(child.value,alpha)
        if(beta<=alpha):
            break
    return best
def MinValue(tree,node, alpha, beta):
    NodeIndex = tree.get_index(node)
    children_value = [node.get_value() for node in tree.nodes[NodeIndex].children]
    if len(children_value) == 0:
        return node.get_value()
    best = 10000
    for child in tree.nodes[NodeIndex].children: 
        temp = MaxValue(tree,child, alpha, beta)
        best = min(best,temp)
        if child.value <= alpha:
            return child.value
        beta = min(child.value,beta)
        if(beta<=alpha):
            break
    return best
def Alpha_Beta_Search(tree,node,alpha,beta):
    return MaxValue(tree,node, alpha,beta)
if __name__ == "__main__":
    tree = Tree()
    tree.add_node("A",0)
    tree.add_node_from([
        ("A",0),
        ("B",0),
        ("C",0),
        ("D",3),
        ("E",5),
        ("F",0),
        ("G",0),
        ("H",4),
        ("I",0),
        ("J",5),
        ("K",7),
        ("L",9),
        ("M",0),
        ("N",7),
    ])
    print(tree.show_nodes())
    tree.add_edges_from(
        [
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("B", "E"),
            ("C", "F"),
            ("C", "G"),
            ("C", "H"),
            ("F", "I"),
            ("F", "J"),
            ("G", "K"),
            ("G", "L"),
            ("I", "M"),
            ("I", "N"),
        ]
    )
    NodeS = Node("A",0)
    res = Alpha_Beta_Search(tree,NodeS,-10000,10000)
    print("optimal value: " ,res)