ListNode* reverseKGroup(ListNode* &head, int k)
    {
        ListNode* previous=NULL;
        ListNode* current=head;
        ListNode* nxt=NULL;
        
        ListNode * check;
        check=current;

        
        int count=1;
        while(check->next!=NULL&&count<=k)
        {
            count++;
            check=check->next;
        }
        if(count<k)
            return head;

        count=0;
        
        while(current!=NULL&&count<k)
        {
            nxt=current->next;
            current->next=previous;
            previous=current;
            current=nxt;
            count++;
        }
        
        if(nxt!=NULL)
        {
            head->next=reverseKGroup(nxt,k);
        }
        
        return previous;
    }