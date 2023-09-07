Pony!

struct DLListNode
	int data
	int next_ptr
	int prev_ptr

func DLListAppend

	pull head
	pull value

	new DLListNode -> nextNode

	value -> DLListNode nextNode.data
	head -> DLListNode nextNode.prev_ptr
	0 -> DLListNode nextNode.next_ptr

	nextNode -> DLListNode head.next_ptr

	nextNode -> head

	push head

func DLListPull

	pull head

	jump if head = 0 end

	DLListNode head.prev_ptr -> previous
	DLListNode head.data -> data

	jump if previous = 0 end

	0 -> DLListNode previous.next_ptr

	delete head

	previous -> head

	end:

	push data
	push head

func DLListSize

	pull head
	
	jump if head = 0 end

	1 -> result

	loopHead:

	DLListNode head.prev_ptr -> head

	inc result

	jump if DLListNode head.prev_ptr != 0 loopHead

	end:
	push result

func DLListRemoveAt

	0 -> data

	pull head
	pull index

	jump if index != 0 indexNotZero

	push head

	call DLListPull

	pull head
	pull data

	jump end
	indexNotZero:

	head -> pointer
	0 -> counter

	loopHead:

	jump if pointer = 0 end

	DLListNode pointer.prev_ptr -> pointer

	inc counter

	jump if counter < index loopHead

	DLListNode pointer.data -> data
	DLListNode pointer.prev_ptr -> previous
	DLListNode pointer.next_ptr -> next

	jump if previous = 0 nextNode

	next -> DLListNode previous.next_ptr

	nextNode:

	jump if next = 0 end

	previous -> DLListNode next.prev_ptr

	end:

	push data
	push head