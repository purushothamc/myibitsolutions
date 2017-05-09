/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode *merge(ListNode *A, ListNode *B) {
    if(A == NULL)
		return B;
	if(B == NULL)
		return A;
	ListNode *result=NULL;
	if(A->val <= B->val) {
		result = A;
		A = A->next;
	}
	else {
		result = B;
		B = B->next;
	}
	ListNode *p = result;
	while(A && B) {
		if(A->val <= B->val) {
			p->next = A;
			A = A->next;
		}
		else {
			p->next = B;
			B = B->next;
		}
		p= p->next;
	}
	if(A)
		p->next = A;
	else if(B)
		p->next = B;
	return result;
}
ListNode* Solution::sortList(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if(A == NULL || A->next == NULL)
        return A;
    ListNode *slow, *fast;
    slow = A; fast = A;
    while(fast && fast->next) {
        fast = fast->next;
        if(fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
    }
    fast = slow->next;
    slow->next = NULL;
    ListNode *left = sortList(A);
    ListNode *rigt = sortList(fast);
    return merge(left, rigt);
}
