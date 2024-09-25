#Explanation
##Shane Saito

Since I was not allowed to use any built in containers for this problem, I figured that
a linked list would work well as it can add and remove integers to the top of
the stack in constant O(1) time. To implement this, I created a seperate node
class, each having two attributes (int value, pointer to next node). This will
allow the order of the nodes in the stack to be easily tracked, as a new node
can be pointed towards the previous node at the top of the stack. 

Implementing the methods was fairly straightforward as pushing simply involved
creating a new node with its value and pointer and updating the top of the stack,
while popping involved retrieving the value of the top node, updating the top 
of the stack and returning the previous value of the top node. I originally
implemented self.size to recursively calculate the size of the stack by counting
each node until the bottom node was reached, which would have been linear O(n) time
but then I realized it would be much more efficient to simply keep track of the 
size of the stack as values were added and removed. Then, the size of the stack
could be easily retrieved in O(1) time. I also added a method self.is_empty() 
to easily check if popping or peeking is even possible, as these cannot be 
performed when the stack is empty.
