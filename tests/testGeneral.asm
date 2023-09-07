Pony!

// That's a comment here

/* That's a block comment here 
*/

import native "stdio.h"

func mem_test
    pull value
    pull index

    value[index] -> memory_section

    push memory_section

struct Point
    int x
    int y

struct Line
    Point p1
    Point p2

func struct_test
    pull x
    pull y

    new local Point -> p0
    x -> Point p0.x
    y -> Point p0.y

    new Point -> p1
    x -> Point p1.x
    y -> Point p1.y

    new Point -> p2
    x -> Point p2.y
    y -> Point p2.x

    new Line -> line
    Point p1[] -> Line line.p1
    Point p2[] -> Line line.p2

    push line

func math_test
    pull one
    pull two

    // Standard signed 64-bit integer
    add int one, two -> stdsum
    sub int one, two -> stdsub
    mul int one, two -> stdmul
    div int one, two -> stddiv
    rem int one, two -> stdrem

    // Double (float 64-bit)
    add float one, two -> dsum
    sub float one, two -> dsub
    mul float one, two -> dmul
    div float one, two -> ddiv

    push dsum

func flow_control_test
    7 -> a
    8 -> b

    jump if a > b more
    jump if a < b less

    invoke printf("a = b\n")
    jump loop
    
    more:
    invoke printf("a > b\n")
    jump loop
    
    less:
    invoke printf("a < b\n")

    loop:
    pull counter

    iteration:
    invoke printf("counter value is %lld\n", counter)
    dec counter

    jump if counter > 0 iteration

func pass_test
    pass "printf(\"pass is working!\n\");"

func main
    90 -> deg90

    call pass_test

    push 10
    call flow_control_test

    push 3

    ptr "something about them was weird" -> str
    push str
    call mem_test

    pull mem_test_result
    invoke printf("value is %lld\n", mem_test_result)

    invoke printf("yeah, str is %s\n", str)

    push 17
    push 20
    call struct_test

    pull struct_result

    struct_result -> line
    
    ptr Line line.p1 -> p1
    Point p1.x -> x
    Point p1.y -> y

    delete struct_result

    invoke printf("we passed deleting\n\x")

    push 0.5
    push 0.1
    call math_test

    pull math_result
    invoke printf("we passed math. sum is %f\n", math_result as float)

    ssize -> size
    pull top
    push top
    invoke printf("by the way, stack size is %lld, top is %lld\n", size, top)