from Ui.graph_ui import Console
from graph_class.graph import Graph
from Service.graph_service import Service
import random

class FileException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def generate_random_graph(n, m):
    nodes = list(range(0, n))
    graph = Graph(nodes)
    for edge in range(0, m):
        start = -1
        end = -1
        cost = -1
        while start == end or graph.is_edge(start, end):
            start = random.randint(0, n - 1)
            end = random.randint(0, n - 1)
            cost = random.randint(0, 999)
        graph.add_edge(start, end, cost)
    return graph

def read_graph_from_file(text):
    try:
        fin = open(text, "rt")
        lines = fin.readlines()
        fin.close()
    except FileNotFoundError:
        raise FileException("File does not exists!")
    except IOError:
        raise FileException("IOError!")

    line1 = lines.pop(0)
    line1 = line1.strip().split()
    n = int(line1[0])
    m = int(line1[1])
    the_graph = Graph(list(range(0, n)))
    for line in lines:
        line = line.strip().split()
        start = int(line[0])
        end = int(line[1])
        cost = int(line[2])
        the_graph.add_edge(start, end, cost)
    return the_graph

if __name__ == '__main__':
    option = 0
    graph = Graph([])
    while option != 1 and option != 2:
        option = int(input("Do you want to generate or read from file (1/2): "))
    if option == 1:
        n = 0
        m = 1
        while m > n * (n-1) / 2:
            n = int(input("The number of nodes: "))
            m = int(input("The number of edges (smaller than (if n is the number of nodes): n * (n-1) / 2): "))
        graph = generate_random_graph(n, m)
    elif option == 2:
        graph = read_graph_from_file("graph100k.txt")

    service = Service(graph, "graph_saved.txt")
    console = Console(service)
    console.read_command()
