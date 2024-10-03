// Checking if a binary tree is a complete binary tree in C

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
    int key;
    struct Node *left, *right;
};

// Node creating
struct Node *newNode(char k){
   struct Node *node = (struct Node *)malloc(sizeof(struct Node));
   node->key = k;
   node->right = node->left = NULL;
   return node;
}

// Count the number of nodes
int countNumberNodes(struct Node *root){
    if (root == NULL)
        return (0);
    return (1 + countNumberNodes(root->left) + countNumberNodes(root->right));	
}

// Check if the tree is a complete binary tree
bool checkComplete(struct Node *root, int index, int numberNodes){
    // Check if the tree is complete
    if (root == NULL)
        return true;
        
    if (index >= numberNodes)
        return false;
        
    return (checkComplete(root->left, 2 * index + 1, numberNodes) && checkComplete(root->right, 2 * index + 2, numberNodes));
}

int main(){
	struct Node *root = NULL;
	root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	
	int node_count = countNumberNodes(root);
	int index = 0;
	
	if(checkComplete(root, index, node_count)){
		printf("The tree is a complete binary tree");
	}else{
		printf("The tree is not a complete binary tree");
		}
	return 0;
}
