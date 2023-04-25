/*Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)*/


// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


#include <iostream>
#include <vector>
using namespace std;

void traverse(Node* root, vector<int> * vec) {
    vec->push_back(root->val);

    for (auto child : root -> children) {
        traverse(child, vec);
    }
    
}

class Solution {
public:
    vector<int> preorder(Node* root) {

        if (root == nullptr) {
            return {};
        }

        vector<int> traverse_result = {};

        traverse(root, &traverse_result);

        return traverse_result;
        
    }
};

int main(void) {
    Node a, b, c;

    a.val = 1;
    b.val = 3;
    c.val = 2;

    // Allocate memory for Node objects using new operator
    Node* ptrB = new Node(3);
    Node* ptrC = new Node(2);

    // Push the pointers to the Node objects into the children vector
    a.children.push_back(ptrB);
    a.children.push_back(ptrC);

    // Access the children using pointers
    // std::cout << "a.val: " << a.val << std::endl;
    // std::cout << "a.children[0]->val: " << a.children[0]->val << std::endl;
    // std::cout << "a.children[1]->val: " << a.children[1]->val << std::endl;



    Solution sol;

    auto result = sol.preorder(&a);

    for (auto i : result) {
        cout << i << " ";
    }
    cout << endl;

        // Don't forget to free the dynamically allocated memory to avoid memory leaks
    delete ptrB;
    delete ptrC;
}