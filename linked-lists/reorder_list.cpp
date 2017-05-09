/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* reverse(ListNode *A) {
     ListNode *temp, *prev, *nxt;
     prev = NULL; nxt = NULL;
     temp = A;
     while(temp) {
         nxt = temp->next;
         temp->next = prev;
         prev = temp;
         temp = nxt;
     }
     return prev;
}
ListNode* Solution::reorderList(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    ListNode *slow, *fast, *current, *h1, *h2;
	slow = A; fast = A;
	while(fast != NULL && fast->next != NULL){
		slow = slow->next;
		fast = fast->next->next;
	}
	h2 = reverse(slow->next);
	h1 = A;
	slow->next = NULL;
	ListNode *result = new ListNode(0);
	current = result;
	while(h1 || h2) {
		if(h1) {
			current->next = h1;
			h1 = h1->next;
			current = current->next;
		}
		if(h2) {
			current->next = h2;
			h2 = h2->next;
			current = current->next;
		}
	}
	return result->next;
}
