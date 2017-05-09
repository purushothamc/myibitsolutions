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
ListNode* Solution::removeNthFromEnd(ListNode* A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    ListNode *p, *head;
    p=A; head=A;
    int len = length(A);
    if (len <= 1) {
        return NULL;
    }
    if(len <= B) {
        A = A->next;
    }
    else {
        for(int i=0; i<B; i++) {
            p = p->next;
        }
        while(p->next) {
            head = head->next;
            p = p->next;
        }
        head->next = head->next->next;
    }
    return A;
}
