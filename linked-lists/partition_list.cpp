/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::partition(ListNode* A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if(A == NULL || A->next == NULL)
        return A;
    ListNode *h = new ListNode(0), *head=A;
    h->next = head;
    head = h;
    ListNode *p = head;

    ListNode *h2 = new ListNode(0);
    ListNode *p2 = h2;

    while(p->next) {
    	if(p->next->val < B)
    		p = p->next;
    	else {
    		ListNode *temp = p->next;
    		p2->next = temp;
    		p2 = p2->next;
    		p->next = temp->next;
    	}
    }
    p2->next = NULL;
    p->next = h2->next;
    return head->next;
}
