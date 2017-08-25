/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
TreeLinkNode* findNextRight(TreeLinkNode *t) {
    t = t->next;
    while(t) {
        if(t->left) return t->left;
        if(t->right) return t->right;
        else t = t->next;
    }
    return NULL;
}
void connect(TreeLinkNode* A) {
    TreeLinkNode *p, *q;
    p = A; q = A;
    p->next = NULL;
    while(p) {
        q = p;
        while(q) {
            if(q->left) {
                if(q->right) {
                    q->left->next = q->right;
                }
                else {
                    q->left->next = findNextRight(q);
                }
            }
            if(q->right) {
                q->right->next = findNextRight(q);
            }
            q = q->next;
        }
        if(p->left) {
            p = p->left;
        }
        else if(p->right) {
            p = p->right;
        }
        else {
            p = findNextRight(p);
        }
    }
}
