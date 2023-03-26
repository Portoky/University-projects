from Service.graph_service import Service
from Service.graph_service import ServiceExcepion
from graph_class.graph import GraphException


class Console:
    def __init__(self, service):
        self.__service = service
        self.__commands = {"1": self.add_node, "2": self.add_edge, "3": self.remove_node, "4": self.remove_edge,
                           "5": self.write_to_file, "6":self.print_nodes, "7":self.print_outbound_edges,
                           "8": self.print_inbound_edges, "9": self.degree_of_node, "10": self.get_edge_cost,
                           "11":self.set_edge_cost}

    def read_command(self):
        done = False
        while not done:
            self.print_options()
            cmd = input("Your command: ")
            if cmd == "0":
                break
            try:
                self.__commands[cmd]()
            except KeyError:
                print("Command non existent")
            except ServiceExcepion as se:
                print(se)
            except GraphException as ge:
                print(ge)

    def add_node(self):
        node = int(input("The node: "))
        self.__service.add_node(node)

    def add_edge(self):
        start = int(input("Starting node: "))
        end = int(input("Ending node: "))
        cost = int(input("Cost of the edge: "))
        self.__service.add_edge(start, end, cost)

    def remove_node(self):
        node = int(input("The node: "))
        self.__service.remove_node(node)

    def remove_edge(self):
        start = int(input("Starting node: "))
        end = int(input("Ending node: "))
        self.__service.remove_edge(start, end)

    def write_to_file(self):
        self.__service.write_file()

    def print_nodes(self):
        nodes = self.__service.get_nodes()
        for node in nodes:
            print(str(node) + " ", end='')
        print()

    def get_edge_cost(self):
        start = int(input("Starting node: "))
        end = int(input("Ending node: "))
        print(self.__service.get_edge_cost(start, end))

    def set_edge_cost(self):
        start = int(input("Starting node: "))
        end = int(input("Ending node: "))
        cost = int(input("Cost of the edge: "))
        self.__service.set_edge_cost(start, end, cost)

    def degree_of_node(self):
        node = int(input("The node: "))
        inDegree = self.__service.get_in_degree(node)
        outDegree = self.__service.get_out_degree(node)
        print("In degree: " + str(inDegree))
        print("Out degree: " + str(outDegree))

    def print_outbound_edges(self):
        node =int(input("The node: "))
        iter = self.__service.iter_outbound_edges(node)
        for outnodes in iter:
            print(str(outnodes), end=' ')
        print()

    def print_inbound_edges(self):
        node = int(input("The node: "))
        iter = self.__service.iter_inbound_edges(node)
        for outnodes in iter:
            print(str(outnodes), end=' ')
        print()

    @staticmethod
    def print_options():
        print("Options:")
        print("0: Exit")
        print("1: Add node")
        print("2: Add edge")
        print("3: Remove node")
        print("4: Remove edge")
        print("5: Save to file")
        print("6: Print nodes")
        print("7: Print outbound edges")
        print("8: Print inbound edges")
        print("9: Degree of node")
        print("10: Get cost of an edge")
        print("11: Set cost of an edge")