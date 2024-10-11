// Kosaraju's algorithm to find strongly connected components in C

#include <stdio.h>
#include <stdlib.h>

struct Graph {
    int V;
    int** adj;
};

// Create a new Graph
Graph *createGraph(int V) {
	Graph *graph;
	graph = (struct Graph*)malloc(sizeof(struct Graph));
	graph->V = V;
	
	graph->adj = (int**)malloc(V * sizeof(int*));
	for (int i = 0; i < V; i++) {
	    graph->adj[i] = (int*) malloc(V * sizeof(int));
	    for (int j = 0; j < V; j++) 
	        graph->adj[i][j] = 0;
	}
	return graph;	   
}

// Add edge to graph
void  addEdge(Graph* graph, int v, int w) {
    graph->adj[v][w] = 1;
}

// DFS to fill the stack
void fillOrder(Graph* graph, int v, int* visited, int* stack, int* stackIndex) {
    visited[v] = 1;
    
    for ( int i = 0; i < graph->V; i++) {
        if (graph->adj[v][i] && !visited[i])
          fillOrder(graph, i, visited, stack, stackIndex);
    }
    stack[(*stackIndex)++] = v;
}

// DFS for printing components
void DFSPrint(Graph* graph, int v, int* visited) {
    visited[v] = 1;
    printf("%d ",v);
    
    for (int i = 0; i < graph->V; i++) {
        if (graph->adj[v][i] && !visited[i])
          DFSPrint(graph, i, visited);
    }
}

// Transpose
Graph* getTranspose(Graph* graph) {
    Graph* gTranspose = createGraph(graph->V);
    
    for (int v = 0; v < graph->V; v++) {
        for (int w = 0; w < graph->V; w++) {
            if (graph->adj[v][w])
              addEdge(gTranspose, w, v);
        }
    }
    
    return gTranspose;
}

// SCC
void printSCC(Graph* graph) {
    int* stack = (int*)malloc(graph->V * sizeof(int));
    int stackIndex = 0;
    
    int* visited = (int*)malloc(graph->V * sizeof(int));
    for ( int i = 0; i < graph->V; i++)
        visited[i] = 0;
    
    for (int i = 0; i <graph->V; i++) {
        if (!visited[i])
          fillOrder(graph, i, visited, stack, &stackIndex);
    }
    
    Graph* gTranspose = getTranspose(graph);
    
    for (int i = 0; i < graph->V; i++)
        visited[i] = 0;
    
    while (stackIndex > 0) {
        int v = stack[--stackIndex];
        if (!visited[v]) {
          DFSPrint(gTranspose, v, visited);
          printf("\n");
        }
    }
    
    free(stack);
    free(visited);
}

int main() {
    int V = 5;
    Graph* graph = createGraph(V);
    
    addEdge(graph, 0, 2);
    addEdge(graph, 2, 1);
    addEdge(graph, 1, 0);
    addEdge(graph, 0, 3);
    addEdge(graph, 3, 4);
    
    printf("Strongly Connected Components\n");
    printSCC(graph);
    
    return 0;
}
