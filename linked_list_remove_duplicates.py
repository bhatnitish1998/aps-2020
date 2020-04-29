 # Remove duplicate elements in linked list

 # Input: pointer to root node (node consists of left, right, and data)

 # Output : Returns the head of the linked list with duplicated deleted

 def removeDuplicates(head):
        if head==None:
            return head
        else:
            current=head
            while(current.next!=None):
                if current.data==current.next.data:
                    current.next=current.next.next
                else:
                    current=current.next
            return head