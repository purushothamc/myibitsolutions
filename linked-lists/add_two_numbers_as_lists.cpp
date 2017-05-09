/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if(!A && B)
		return B;
	else if(A && !B)
		return A;
	//A = reverse(A);
	//B = reverse(B);
	ListNode *head, *temp;
	head = NULL; temp = NULL;
	int carry = 0;
	while(A && B) {
		int sum = A->val + B->val + carry;
		int digit = sum % 10;
		carry = sum / 10;
		if(head == NULL) {
			head = new ListNode(digit);
			temp = head;
		}
		else {
			temp->next = new ListNode(digit);
			temp = temp->next;
		}
		A = A->next;
		B = B->next;
	}
	while(A) {
		if(carry) {
			int sum = A->val + carry;
			int digit = sum % 10;
			carry = sum / 10;
			temp->next = new ListNode(digit);
			temp = temp->next;
		}
		else {
			temp->next = A;
			break;
		}
		A = A->next;
	}
	while(B) {
		if(carry) {
			int sum = B->val + carry;
			int digit = sum % 10;
			carry = sum / 10;
			temp->next = new ListNode(digit);
			temp = temp->next;
		}
		else {
			temp->next = B;
			break;
		}
		B = B->next;
	}
	if(carry) {
		temp->next = new ListNode(carry);
	}
	return head;
}