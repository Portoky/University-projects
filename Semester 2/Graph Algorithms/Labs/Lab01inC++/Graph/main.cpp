#include <iostream>
#include <string>
#include "graph.h"

using namespace std;

int main()
{
	Graph g;
	g.addNode(5);
	cout << g.isNode(5) << " ";
	cout << g.addNode(5) << " ";
	g.addNode(6);
	g.addNode(7);
	g.addNode(8);
	g.addEdge(7, 8, 2);
	g.addEdge(5, 6, 2);
	cout << g.isEdge(5, 6) << " ";
	g.removeEdge(5, 6);
	cout << g.isEdge(5, 6) << " ";
	cout << g.removeNode(5);
	cout << g.removeNode(6);
	cout << g.removeNode(7);
}