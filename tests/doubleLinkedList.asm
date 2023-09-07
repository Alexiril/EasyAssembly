Pony!

struct Node
	int data
	int next_ptr
	int prev_ptr

func append

	pull head
	pull value

	new Node -> nextNode

	value -> Node nextNode.data
	head -> Node nextNode.prev_ptr
	0 -> Node nextNode.next_ptr

	nextNode -> Node head.next_ptr

	nextNode -> head

	push head

func pop

	pull head

	jump if head = 0 end

	Node head.prev_ptr -> previous
	Node head.data -> data

	jump if previous = 0 end

	0 -> Node previous.next_ptr

	delete head

	previous -> head

	end:

	push data
	push head

func listSize

	pull head
	
	jump if head = 0 end

	1 -> result

	loopHead:

	Node head.prev_ptr -> head

	inc result

	jump if Node head.prev_ptr != 0 loopHead

	end:
	push result

func removeAt

	0 -> data

	pull head
	pull index

	jump if index != 0 indexNotZero

	push head

	call pop

	pull head
	pull data

	jump end
	indexNotZero:

	head -> pointer
	0 -> counter

	loopHead:

	jump if pointer = 0 end

	Node pointer.prev_ptr -> pointer

	inc counter

	jump if counter < index loopHead

	Node pointer.data -> data
	Node pointer.prev_ptr -> previous
	Node pointer.next_ptr -> next

	jump if previous = 0 nextNode

	next -> Node previous.next_ptr

	nextNode:

	jump if next = 0 end

	previous -> Node next.prev_ptr

	end:

	push data
	push head