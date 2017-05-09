/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::swapPairs(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    // Recursive solution.
    /*if(!A || !(A->next))
        return A;
    ListNode *a, *b, *x, *y, *nxt;
    a = A; b = A->next;
    nxt = b->next;
    b->next = a;
    a->next = swapPairs(nxt);
    return b;*/

    // Iterative Solution.
    ListNode *head, *p, *nxt, *temp;
    head=A; p=NULL;
    while(head && head->next) {
        nxt = head->next->next;
        temp = head->next;
        if(!p) {
            p = head->next;
        }
        head->next->next = head;
        head->next = nxt;
        head = nxt;
    }
    if(!p)
        return A;
    return p;
}
