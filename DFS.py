class Node:
    def __init__(self, data):
        self.data = data
        self.parents = []
        self.children = []
    def get_data(self):
        return self.data
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
    def add_node(self, node_name):
        node = Node(node_name)
        if not self.is_contains(node):
            self.nodes.append(node)
    def add_node_from(self, array_of_nodes_name):
        for el in array_of_nodes_name:
            node = Node(el)
            if not self.is_contains(node):
                self.nodes.append(node)
    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False
    def add_edge(self, start_name, end_name):
        start_node = Node(start_name)
        end_node = Node(end_name)
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

# Bai tap 2
def Depth_First_Search(tree,initialState, goalTest):
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("frontier: ", frontier)
        state = frontier.pop(len(frontier)-1)  # pop(0) [1,2,3,4,5]
        stateNode = Node(state)
        explored.append(state)
        if goalTest == state:
            return True
        index = tree.get_index(stateNode)
        for neighbor in tree.nodes[index].get_children():
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False
if __name__ == "__main__":
    G = Tree()
    G.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    G.add_edges_from(
        [
            ("S", "A"),
            ("S", "B"),
            ("S", "C"),
            ("A", "D"),
            ("B", "G"),
            ("B", "E"),
            ("C", "E"),
            ("D", "F"),
            ("E", "H"),
            ("F", "E"),
            ("H", "G"),
            ("F", "G"),
        ]
    )
    result = Depth_First_Search(G,"S", "D")
    print(result)