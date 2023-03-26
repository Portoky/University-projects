class GraphException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Graph:
    def __init__(self, nodes):
        self.__graph_out = {}
        self.__graph_in = {}
        self.__edges = {}
        for node in nodes:
            self.__graph_out[node] = []
            self.__graph_in[node] = []
    @property
    def graph_out(self):
        return self.__graph_out

    @property
    def graph_in(self):
        return self.__graph_in

    @property
    def edges(self):
        return self.__edges

    @property
    def nm_of_nodes(self):
        return len(self.__graph_in.keys())

    @property
    def nm_of_edges(self):
        return len(self.__edges)

    def is_node(self, node):
        if node in self.__graph_in.keys():
            return True
        return False

    def is_edge(self, start, end):
        if (start, end) in self.__edges.keys():
            return True
        return False

    def add_node(self, node):
        if self.is_node(node):
            raise GraphException("Node already in graph!")
        self.__graph_in[node] = []
        self.__graph_out[node] = []

    def remove_node(self, node):
        if not self.is_node(node):
            raise GraphException("Node not in graph!")

        for out_node in self.__graph_out[node]:
            if node in self.__graph_in[out_node]:
                self.__graph_in[out_node].remove(node)
        for in_node in self.__graph_in[node]:
            if node in self.__graph_out[in_node]:
                self.__graph_out[in_node].remove(node)
        del self.__graph_in[node]
        del self.__graph_out[node]

        nm_of_edges = self.nm_of_edges
        edges = list(self.__edges.keys())
        for i in range(nm_of_edges):
            if edges[i][0] == node or edges[i][1] == node:
                del self.__edges[edges[i]]

    def add_edge(self, start, end, cost):
        if not self.is_node(start) or not self.is_node(end):
            raise GraphException(f"Nodes don't exist {start} {end}")
        if self.is_edge(start, end):
            raise GraphException("Edge already exists")
        self.__edges[(start, end)] = cost
        self.__graph_out[start].append(end)
        self.__graph_in[end].append(start)

    def remove_edge(self, start, end):
        if not self.is_node(start) or not self.is_node(end):
            raise GraphException("Nodes don't exist")
        if not self.is_edge(start, end):
            raise GraphException("Edge does not exist")
        del self.__edges[(start, end)]
        self.__graph_out[start].remove(end)
        self.__graph_in[end].remove(start)

    def get_out_degree(self, node):
        if not self.is_node(node):
            raise GraphException("Node does not exist")
        return len(self.__graph_out[node])

    def get_in_degree(self, node):
        if not self.is_node(node):
            raise GraphException("Node does not exist")
        return len(self.__graph_in[node])

    def iterate_outbound_edges_of_node(self, node):
        if not self.is_node(node):
            raise GraphException("Node does not exist")
        out_target = []
        for target in self.__graph_out[node]:
            out_target.append(target)
        return iter(out_target)

    def iterate_inbound_edges_of_node(self, node):
        if not self.is_node(node):
            raise GraphException("Node does not exist")
        in_target = []
        for target in self.__graph_in[node]:
            in_target.append(target)
        return iter(in_target)

    def information_of_edge(self, start, end):
        if not self.is_edge(start, end):
            raise GraphException("Edge does not exists")
        return self.__edges[(start, end)]

    def modify_edge(self, start, end, cost):
        if not self.is_edge(start, end):
            raise GraphException("Edge does not exists")
        self.__edges[(start, end)] = cost
