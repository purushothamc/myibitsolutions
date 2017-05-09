/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    // --- Below is accepted solution, but it is long.

    /*ListNode *head, *temp, *prev, *t;
    temp = A; head = NULL, prev=NULL;
    bool dup_found=false;
    if(!temp || !(temp->next))
        return temp;
    while(temp && temp->next) {
        if(temp->val == temp->next->val) {
            dup_found = true;
            t = temp->next;
            temp->next = temp->next->next;
            delete t;
        }
        else {
        	if(dup_found) {
            	if(!head) {
                	head = NULL;
                	temp = temp->next;
            	}
                else {
                	ListNode *tn = temp;
	                temp = temp->next;
	                prev->next = temp;
	                delete tn;
                }
        	}
        	else {
        		if(!head)
                	head = temp;
                prev = temp;
        		temp = temp->next;
        	}
        	dup_found = false;
        }
    }
    if(!head && !(temp->next) && !dup_found) {
    	head = temp;
    }
    if(dup_found && temp->next == NULL) {
    	if(prev) {
    		prev->next = temp->next;
    		delete temp;
    	}
    }
    return head;*/

    // --Following solution uses fakeHead to simulate the algorithm.
    ListNode *fakeHead = new ListNode(0);
    fakeHead->next = A;
    ListNode *cur=A, *pre=fakeHead;
    while(cur != NULL) {
        while(cur->next != NULL && cur->val == cur->next->val) {
            cur = cur->next;
        }
        if(pre->next == cur) {
            pre = pre->next;
        }
        else {
            pre->next = cur->next;
        }
        cur = cur->next;
    }
    return fakeHead->next;
}