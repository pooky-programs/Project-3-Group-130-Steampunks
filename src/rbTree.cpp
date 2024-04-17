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

bool RBTree::insert(int ID, gameObject obj){

    TreeNode* node = add(ID, obj);

    if(node == nullptr){
        return false;
    }

    //balance tree if necessary
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