// Created:
// 4/7/2024
// by Joel Liston

#include "rbTree.h"
#include <iostream>

TreeNode* RBTree::add(int ID, gameObject obj){

    if(root == nullptr){
        root = new TreeNode(ID, obj, 0, nullptr);
        return root;
    }
    else{

        TreeNode* current = root;

        while(current != nullptr){

            if(current->ID == ID){
                return nullptr;
            }
            else if (current->ID > ID)
            {
                if(current->left == nullptr){
                    current->left = new TreeNode(ID, obj, 0, current);
                    return current->left;
                }
                else{
                    current = current->left;
                }
            }
            else{
                if(current->right == nullptr){
                    current->right = new TreeNode(ID, obj, 0, current);
                    return current->right;
                }
                else{
                    current = current->right;
                }
            }
            
        }
    }

    return nullptr;

}

TreeNode *RBTree::getRoot() {
    return root;
}

void RBTree::inorder_traversal(TreeNode* node) {
    if (node == nullptr) {
        return;
    }
    inorder_traversal(node->left);
    cout << node->object._appid << endl;
    inorder_traversal(node->right);
}

TreeNode* TreeNode::getUncle(TreeNode* p){
    if(p == nullptr || p->parent == nullptr){
        return nullptr;
    }
    else{
        if(p->parent->right == p){
            return p->parent->left;
        }
        else{
            return p->parent->right;
        }
    }
}

bool RBTree::balance(TreeNode* node){

    if(node == nullptr){
        return false;
    }

    //root starts as black
    if(node->parent == nullptr){
        node->color = 1;
        return true;
    }

    //case 1: parent is black, do nothing
    if(node->parent->color == 1){
        return true;
    }

    //case 2: uncle is red
    if(node->uncle == nullptr){
        //move on
    }
    else if(node->uncle->color == 0){
        node->uncle->color = 1;
        node->parent->color = 1;
        node->parent->parent->color = 0;
        return balance(node->parent->parent);
    }

    //case 3: uncle is black (or nullptr), rotations necessary
    TreeNode* p = node->parent;
    TreeNode* g = node->parent->parent;
    TreeNode* temp;
    int tempColor;

    //LL
    if(g->left == p && p->left == node){
        temp = p->right;
        p->right = g;
        g->left = temp;

        p->parent = g->parent;
        g->parent = p;

        if(p->parent != nullptr){
            if(p->parent->right == g){
                p->parent->right = p;
            }
            else{
                p->parent->left = p;
            }
        }
        else{
            root = p;
        }

        tempColor = p->color;
        p->color = g->color;
        g->color = tempColor;

    }

    //LR
    if(g->left == p && p->right == node){
        temp = node->left;

        node->left = p;
        p->parent = node;
        p->right = temp;
        node->parent = g;

        temp = node->right;
        node->right = g;
        g->left = temp;

        node->parent = g->parent;
        g->parent = node;

        if(node->parent != nullptr){
            if(node->parent->right == g){
                node->parent->right = node;
            }
            else{
                node->parent->left = node;
            }
        }
        else{
            root = node;
        }

        tempColor = node->color;
        node->color = g->color;
        g->color = tempColor;
    }

    //RR (mirror LL)
    if(g->right == p && p->right == node){
        temp = p->left;
        p->left = g;
        g->right = temp;

        p->parent = g->parent;
        g->parent = p;

        if(p->parent != nullptr){
            if(p->parent->left == g){
                p->parent->left = p;
            }
            else{
                p->parent->right = p;
            }
        }
        else{
            root = p;
        }

        tempColor = p->color;
        p->color = g->color;
        g->color = tempColor;

    }

    //RL (Mirror LR)
    if(g->right == p && p->left == node){
        temp = node->right;

        node->right = p;
        p->parent = node;
        p->left = temp;
        node->parent = g;

        temp = node->left;
        node->left = g;
        g->right = temp;

        node->parent = g->parent;
        g->parent = node;

        if(node->parent != nullptr){
            if(node->parent->left == g){
                node->parent->left = node;
            }
            else{
                node->parent->right = node;
            }
        }
        else{
            root = node;
        }

        tempColor = node->color;
        node->color = g->color;
        g->color = tempColor;
    }

    return true;
}

bool RBTree::insert(int ID, gameObject obj){

    TreeNode* node = add(ID, obj);

    return balance(node);

}

TreeNode* RBTree::searchID(int ID){

    if(root == nullptr){
        return nullptr;
    }

    TreeNode* current = root;

    while(current != nullptr){
        int debug = current->ID;

        if(current->ID == ID){
            return current;
        }
        else if (current->ID < ID)
        {
            current = current->right;
        }
        else{
            current = current->left;
        }
        
    }

    return nullptr;
}