class Node:
    def __init__(self, data, value):
        self.data = data
        self.value = value
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
    def add_node(self, node_name, value):
        node = Node(node_name, value)
        if not self.is_contains(node):
            self.nodes.append(node)
    def add_node_from(self, array_of_tuple_node):
        for nd in array_of_tuple_node:
            data = nd[0]
            value = nd[1]
            node = Node(data,value)
            if not self.is_contains(node):
                self.nodes.append(node)
    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False
    def add_edge(self, start_name, end_name,value = 0):
        start_value = self.get_value_byName(start_name)
        end_value = self.get_value_byName(end_name)
        start_node = Node(start_name,start_name)
        end_node = Node(end_name,end_name)
        if not self.is_contains(start_node):
            self.add_node(start_name)
        if not self.is_contains(end_node):
            self.add_node(end_name)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(end_node)
        self.nodes[end_index].parents.append(start_node)
        self.edges.append((self.nodes[start_index], self.nodes[end_index],value))
    def add_edges_from(self, array_of_tuple_node):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            value = tup[2]
            self.add_edge(start, end, value)
    def show_nodes(self):
        return [node.get_value() for node in self.nodes]
    def show_edges(self):
        return [(edge[0].get_data(), edge[1].get_data(), edge[2]) for edge in self.edges]
    def get_value_byName(self,name):
        for el in self.nodes:
            if name == el.get_data():
                return el.get_value()
def Uniform_cost_search(tree, initialState,goalTest):
    frontier = []
    explore = []
    frontier.append(initialState)
    while(len(frontier)>0):
        print("frontier: >" )
        for el in frontier:
            print("(",el.get_data(),")","[",el.get_value(),"]")
        state = frontier.pop(deleteMin(frontier))
        State_index = tree.get_index(state)
        explore.append(state)
        if state.get_data() == goalTest.get_data():
            return True
        for child in tree.nodes[State_index].children:
            child_idx = tree.get_index(child)
            if child not in list(set(frontier + explore)):
                temp_node = tree.nodes[child_idx]
                temp_node.value  = temp_node.value + state.value
                frontier.append(temp_node)

            else:
                if is_inFrontier(child,frontier):
                    index = is_inFrontier(child,frontier)
                    frontier[index] = update_cost(child,state,frontier)
def deleteMin(frontier):
    if len(frontier) < 2:
        return 0
    min_el = frontier[0]
    for el in frontier:
        if el.get_value() < min_el.get_value():
            min_el = el
    for el in frontier:
        index = is_inFrontier(min_el,frontier)
    return index
def is_inFrontier(node, frontier):
    for indx,el in enumerate(frontier):
        if el.get_data() == node.get_data():
            return indx
    return 0
def update_cost(node,state,frontier):
    for el in frontier:
        if node.get_data() == el.get_data():
            if el.get_value > state.get_value()+node.get_value():
                el.value = state.get_value()+node.get_value()
    return el
if __name__ == "__main__":
    tree = Tree()
    tree.add_node("S",0)
    tree.add_node_from([
        ("S",0),
        ("A",3),
        ("B",5),
        ("C",2),
        ("D",9),
        ("E",12),
        ("F",5),
        ("G",23),
        ("H",11),
    ])
    print(tree.show_nodes())
    tree.add_edges_from(
        [
            ("S", "A",3),
            ("S", "B",5),
            ("B", "C",6),
            ("B", "D",7),
            ("C", "E",8),
            ("C", "G",7),
            ("D", "H",7),
            ("D", "G",8),
        ]
    )
    print(tree.show_edges())
    NodeS = Node("S",0)
    NodeG = Node("G",23)
    res = Uniform_cost_search(tree,NodeS,NodeG)
    print("optimal value :",res )