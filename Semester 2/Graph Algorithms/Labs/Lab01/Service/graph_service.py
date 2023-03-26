import copy

from graph_class.graph import Graph


class ServiceExcepion(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Service:
    def __init__(self, graph, text):
        self.__graph = graph
        self.__text = text

    def copy_graph(self):
        return copy.deepcopy(self.__graph)

    def get_nm_of_nodes(self):
        return self.__graph.nm_of_nodes

    def get_nodes(self):
        return list(self.__graph.graph_in.keys())

    def edge_in_between(self, start, end):
        return self.__graph.is_edge(start, end) or self.__graph.is_edge(end, start)

    def get_edge_cost(self, start, end):
        return self.__graph.information_of_edge(start, end)

    def set_edge_cost(self, start, end, cost):
        self.__graph.modify_edge(start, end, cost)

    def get_in_degree(self, node):
        return self.__graph.get_in_degree(node)

    def get_out_degree(self, node):
        return self.__graph.get_out_degree(node)

    def iter_outbound_edges(self, node):
        return self.__graph.iterate_outbound_edges_of_node(node)

    def iter_inbound_edges(self, node):
        return self.__graph.iterate_inbound_edges_of_node(node)

    def load_file(self):
        try:
            fin = open(self.__text, "rt")
            lines = fin.readlines()
            fin.close()
        except FileNotFoundError:
            raise ServiceExcepion("File does not exists!")
        except IOError:
            raise ServiceExcepion("IOError!")

        line1 = lines.pop(0)
        line1 = line1.strip()
        n = line1[0]
        m = line1[1]
        self.__graph = Graph(list(range(0, n)))
        for line in lines:
            line = line.strip()
            start = line[0]
            end = line[1]
            cost = line[2]
            self.__graph.add_edge(start, end, cost)

    def write_file(self):
        try:
            fout = open(self.__text, "wt")
        except FileNotFoundError:
            raise ServiceExcepion("File does not exists!")
        except IOError:
            raise ServiceExcepion("IOError!")

        fout.write(str(self.__graph.nm_of_nodes) + " ")
        fout.write(str(self.__graph.nm_of_edges) + "\n")
        for edge in self.__graph.edges:
            fout.write(str(edge[0]) + " " + str(edge[1]) + " " + str(self.__graph.edges[edge]) + "\n")

    def add_node(self, node):
        self.__graph.add_node(node)

    def add_edge(self, start, end, cost):
        self.__graph.add_edge(start, end, cost)

    def remove_node(self, node):
        self.__graph.remove_node(node)

    def remove_edge(self, start, end):
        self.__graph.remove_edge(start, end)

    def is_edge(self, start, end):
        return self.__graph.is_edge(start, end)






