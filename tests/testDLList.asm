Pony!

import native "stdio.h"

import "doubleLinkedList.asm"

func main

	new Node -> head
	3 -> Node head.data
	0 -> Node head.next_ptr
	0 -> Node head.prev_ptr

	push 7
	push head

	call append

	pull head

	invoke printf("value of head is: %lld\n", Node head.data)

	push head

	call pop
	
	pull head
	pull deletedData

	invoke printf("value of head is: %lld and old data is: %lld\n", Node head.data, deletedData)

	1 -> counter

	loopHead:
	push counter
	push head

	call append

	pull head

	inc counter

	jump if counter < 5 loopHead

	push head
	call listSize
	pull size
	invoke printf("okay, now the head is: %lld, and the size is: %lld\n", Node head.data, size)

	push 1
	push head
	call removeAt
	pull head
	pull deletedData
	push head
	call listSize
	pull size
	
	invoke printf("okay, now the head is: %lld, and the size is: %lld, and deleted was: %lld\n", Node head.data, size, deletedData)
