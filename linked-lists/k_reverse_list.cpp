/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int length(ListNode *A) {
    int len = 0;
    while(A) {
        len += 1;
        A = A->next;
    }
    return len;
}
ListNode* Solution::rotateRight(ListNode* A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int len = length(A);
    B = B % len;
    ListNode *head, *p, *current;
    head=A; p=A; current=A;
    if(!A || !(A->next) || B == 0)
        return A;
    for(int i=0; i<B-1; i++)
        p = p->next;
    while(p->next) {
        current = current->next;
        p = p->next;
    }
    while(head->next != current)
        head = head->next;
    p->next = A;
    head->next = NULL;
    A = current;
    return A;
}
