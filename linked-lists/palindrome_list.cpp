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
int Solution::lPalin(ListNode* A) {
    ListNode *slow, *fast;
    slow = A; fast = A;
    if(!(A) && !(A->next)) {
        return 1;
    }
    while(fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    slow->next = reverse(slow->next);
    ListNode *c, *d;
    c = A; d = slow->next;
    while(c && d) {
        if(c->val != d->val)
            return 0;
        c = c->next;
        d = d->next;
    }
    return 1;
}