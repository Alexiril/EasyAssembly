Pony!

import native "stdio.h"

import "doubleLinkedList"

func main

	new DLListNode -> head
	3 -> DLListNode head.data
	0 -> DLListNode head.next_ptr
	0 -> DLListNode head.prev_ptr

	push 7
	push head

	call DLListAppend

	pull head

	invoke printf("value of head is: %lld\n", DLListNode head.data)

	push head

	call DLListPull
	
	pull head
	pull deletedData

	invoke printf("value of head is: %lld and old data is: %lld\n", DLListNode head.data, deletedData)

	1 -> counter

	loopHead:
	push counter
	push head

	call DLListAppend

	pull head

	inc counter

	jump if counter < 5 loopHead

	push head
	call DLListSize
	pull size
	invoke printf("okay, now the head is: %lld, and the size is: %lld\n", DLListNode head.data, size)

	push 1
	push head
	call DLListRemoveAt
	pull head
	pull deletedData
	push head
	call DLListSize
	pull size
	
	invoke printf("okay, now the head is: %lld, and the size is: %lld, and deleted was: %lld\n", DLListNode head.data, size, deletedData)

	push 999
	push 2
	push head

	call DLListInsert

	push head
	call DLListSize
	pull size

	0 -> counter

	loopHead2:

	push counter
	push head
	call DLListGetAt
	pull node

	invoke printf("data with index %lld is %lld\n", counter, DLListNode node.data)

	inc counter

	jump if counter < size loopHead2

	push head
	call DLListClear
	pull head

	push head
	call DLListSize
	pull size

	invoke printf("list size is %lld\n", size)