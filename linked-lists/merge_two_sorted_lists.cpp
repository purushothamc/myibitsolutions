/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    /* -------- Following is a recursive solution which uses stack space.
    /*ListNode *result = NULL;
    if(A == NULL)
        return B;
    else if (B == NULL)
        return A;
    if(A->val <= B->val) {
        result = A;
        result->next = mergeTwoLists(A->next, B);
    }
    else {
        result = B;
        result->next = mergeTwoLists(A, B->next);
    }
    return result;*/

    // ---- Iterative Solution.
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
