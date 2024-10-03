#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct node{
    int data;
	struct node *left;
	struct node *right;
};

// creatinh a new node
struct node *newnode(int data){
	struct node *node = (struct node *)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    
    return (node);
}

// calculate the depth considering both left and right subtrees
int depth(struct node *node){
	if(node == NULL){
		return 0;
		}
	int leftDepth = depth(node->left);
	int rightDepth = depth(node->right);
	return (leftDepth > rightDepth ? leftDepth : rightDepth) +1;
}

// check if the tree is perfect
bool is_perfect(struct node * root, int d, int level){
    // check if the tree is empty
    if (root == NULL)
        return true;
    
    // check the presence of children
    if (root -> left == NULL && root->right == NULL)
        return (d == level + 1);
        
    if(root->left == NULL || root->right == NULL)
        return false;
        
    return is_perfect(root->left, d, level + 1) && is_perfect(root->right, d, level + 1);
}

// warapper function
bool is_Perfect(struct node *root){
    int d = depth(root);
    return is_perfect(root, d, 0);
}


int main(){
	struct node *root = NULL;
	root = newnode(1);
	root->left = newnode(2);
	root->right = newnode(3);
	root->left->left = newnode(4);
	root->left->right = newnode(5);
	root->right->left = newnode(6);
	root->right->right = newnode(7);
	
	if (is_Perfect(root)){
		printf("The tree is a perfect binary tree\n");
	} else{
		printf("The tree is not a perfect bonary tree\n");
		}
	
	return 0;
}
