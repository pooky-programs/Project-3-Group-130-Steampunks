// Created:
// 4/7/2024
// by Joel Liston

#include "rbTree.h";

TreeNode* RBTree::add(int ID, gameObject obj){

    if(root = nullptr){
        root = new TreeNode(ID, obj, 0, nullptr);
    }
    else{

        TreeNode* current = root;

        while(current != nullptr){

            if(current->ID == ID){
                return nullptr;
            }
            else if (current->ID < ID)
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

        if(current->ID == ID){
            return current;
        }
        else if (current->ID < ID)
        {
            current = current->left;
        }
        else{
            current = current->right;
        }
        
    }

    return nullptr;
}