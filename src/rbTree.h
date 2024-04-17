// Created:
// 4/7/2024
// by Joel Liston

#ifndef COP3530_PROJECT_3_RBTREE_H
#define COP3530_PROJECT_3_RBTREE_H

using namespace std;
#include "gameObject.h"

struct TreeNode{
        
    int ID;
    int nodeHeight;
    int color; // 0 = red, 1 = black
    gameObject object;

    TreeNode* left;
    TreeNode* right;

    TreeNode* parent;

    TreeNode(int id, gameObject Object, int Height, TreeNode* Parent){
		ID = id;
		object = Object;
		left = nullptr;
		right = nullptr;
		nodeHeight = Height;
		parent = Parent;
        color = 0;

	}

};

class RBTree{

private:

    TreeNode* root;

    //balance tree
    //height at node
    //find black nodes
    TreeNode* add(int ID, gameObject obj);


public:

    bool insert(int ID, gameObject obj);
    TreeNode* searchID(int ID);


};

#endif //COP3530_PROJECT_3_RBTREE_H
