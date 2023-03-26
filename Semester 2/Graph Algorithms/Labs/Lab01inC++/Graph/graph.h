#pragma once

#include <map>
#include <vector>
#include <array>
typedef int Node;

using namespace std;

class Graph
{
private:
	map<Node, vector<Node>> graph_out;
	map<Node, vector<Node>> graph_in;
	map<std::array<Node, 2>, int> edges;
public:
	bool isNode(Node);
	
	bool isEdge(Node, Node);

	bool addNode(Node);

	bool addEdge(Node, Node, int);

	int getNmNodes();

	int getNmEdges();
	
	bool removeEdge(Node, Node);

	bool removeNode(Node);
};
