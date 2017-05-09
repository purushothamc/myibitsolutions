/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::insertionSortList(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    ListNode *head, *cur, *p;
    if(A == NULL || A->next == NULL)
        return A;
    head = NULL;
    while (A != NULL) {
        cur = A;
        A = A->next;
        if(head == NULL || cur->val < head->val) {
            cur->next = head;
            head = cur;
        }
        else {
            p = head;
            while(p != NULL) {
                if(p->next == NULL || cur->val < p->next->val) {
                    cur->next = p->next;
                    p->next = cur;
                    break;
                }
                p = p->next;
            }
        }
    }
    return head;
}
