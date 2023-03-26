#include "graph.h"
#include <iostream>
using namespace std;

bool Graph::isNode(Node node)
{
	if (this->graph_in.find(node) == this->graph_in.end() && this->graph_out.find(node) == this->graph_out.end())
		return false;
	return true;
}

bool Graph::isEdge(Node start, Node end)
{
	std::array<Node, 2> a = { start, end };
	if (this->edges.find(a) == this->edges.end())
		return false;
	return true;
}

bool Graph::addNode(Node node)
{
	if (isNode(node))
	{
		//throw("Node already in graph");
		return false;
	}
	vector<Node> list;
	this->graph_in[node] = list;
	this->graph_out[node] = list;
	return true;
}

bool Graph::addEdge(Node start, Node end, int cost)
{
	if (isEdge(start, end) or !isNode(start) or !isNode(end))
	{
		return false;
	}
	array<Node, 2> a = { start, end };
	this->edges[a] = cost;
	this->graph_out[start].push_back(end);
	this->graph_in[end].push_back(start);
	return true;
}

int Graph::getNmNodes()
{
	return this->graph_in.size();
}

int Graph::getNmEdges()
{
	return this->edges.size();
}

bool Graph::removeEdge(Node start, Node end)
{
	if (!isEdge(start, end))
		return false;
	array<Node, 2> a = { start, end };
	this->edges.erase(a);
	auto i1 = find(this->graph_out[start].begin(), this->graph_out[start].end(), end);
	this->graph_out[start].erase(i1);
	auto i2 = find(this->graph_in[end].begin(), this->graph_in[end].end(), start);
	this->graph_in[end].erase(i2);
	return true;
}

bool Graph::removeNode(Node node)
{
	if (!isNode(node))
		return false;

	for (auto i = this->graph_in[node].begin(); i < this->graph_in[node].end(); ++i)
	{
		cout << *i << " ";
	}
	return true;
}