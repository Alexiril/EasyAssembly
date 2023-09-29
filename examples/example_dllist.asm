Pony!

import native "stdio.h"

import "doubleLinkedList"

func main

	new DLListNode -> head
	3 -> DLListNode head.data
	0 -> DLListNode head.next_ptr
	0 -> DLListNode head.prev_ptr

	call DLListAppend(7, head) [head]

	call native printf("value of head is: %lld\n", DLListNode head.data)

	call DLListPull(head) [head, deletedData]

	call native printf("value of head is: %lld and old data is: %lld\n", DLListNode head.data, deletedData)

	1 -> counter

	loopHead:
	call DLListAppend(counter, head) [head]

	inc counter

	jump if counter < 5 to loopHead

	call DLListSize(head) [size]

	call native printf("okay, now the head is: %lld, and the size is: %lld\n", DLListNode head.data, size)

	call DLListRemoveAt(1, head) [head, deletedData]
	call DLListSize(head) [size]
	
	call native printf("okay, now the head is: %lld, and the size is: %lld, and deleted was: %lld\n", DLListNode head.data, size, deletedData)

	call DLListInsert(999, 2, head) [head]
	call DLListSize(head) [size]

	0 -> counter

	loopHead2:
	call DLListGetAt(counter, head) [node]

	call native printf("data with index %lld is %lld\n", counter, DLListNode node.data)

	inc counter

	jump if counter < size to loopHead2

	call DLListClear(head) [head]
	call DLListSize(head) [size]

	call native printf("list size (cleared) is %lld\n", size)