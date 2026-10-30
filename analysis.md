Question: Why does the linked-list stack push at the head instead of the tail, and why must the array queue be circular?

The linked-list Stack pushes at the head because inserting a new node at the head is faster and takes O(1) time. If we insert at the tail, it may take O(n) time. The array queue must be ciRcular so that the empty spaces at the begiNning of the array can be reused. This helps avoid wastIng space and keeps Enqueue and dequeue operations efficient.
