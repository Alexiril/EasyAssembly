Pony!

// That's a comment here

/* That's a block comment here 
*/

import "stdio"
import "string"

func mem_test(value, index) [memory_section]
    value[index] -> memory_section

    return memory_section

struct Point
    int x
    int y

struct Line
    Point p1
    Point p2

func struct_test(x, y) [line]
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

    return line

func math_test(one, two) [dsum]
    // Standard signed 64-bit integer
    add one, two -> stdsum
    sub one, two -> stdsub
    mul one, two -> stdmul
    div one, two -> stddiv
    rem one, two -> stdrem

    // Double (float 64-bit)
    add float one, two -> dsum
    sub float one, two -> dsub
    mul float one, two -> dmul
    div float one, two -> ddiv

    return dsum

func flow_control_test(counter) []
    7 -> a
    8 -> b

    jump if a > b to more
    jump if a < b to less

    call native printf("a = b\n")
    jump to iteration
    
    more:
    call native printf("a > b\n")
    jump to iteration
    
    less:
    call native printf("a < b\n")

    iteration:
    call native printf("counter value is %lld\n", counter)
    dec counter

    jump if counter > 0 to iteration

func pass_test []
    pass "printf(\"pass is working!\n\");"
func main()
    call native printf("argc = %d, argv[0] = %s\n", *argc, *argv[] as string)

    90 -> deg90

    call native printf("here first call goes\n")

    call pass_test

    call flow_control_test(10)

    ptr "something about them was weird" -> str
    call mem_test(str, 3) [mem_test_result]

    call native printf("value is %lld\n", mem_test_result)

    call native printf("yeah, str is: %s\n", str as string)

    call struct_test(20, 17) [struct_result]

    struct_result -> line
    
    ptr Line line.p1 -> p1
    Point p1.x -> x
    Point p1.y -> y

    delete struct_result

    call native printf("we passed deleting\n")

    call math_test(0.1, 0.5) [math_result]

    call native printf("we passed math. sum is %f\n", math_result as float)

    push 10

    ssize -> size
    pull top
    push top
    call native printf("by the way, stack size is %lld, top is %lld\n", size, top)

    array [1024] -> arr
    0 -> counter

    loopHead:

    counter -> arr[counter]
    inc counter

    jump if counter < 1024 to loopHead

    dec counter

    call native printf("yeah, array is working, last value is %lld\n", arr[counter])

    heap [16] -> container

    'a' -> byte container[0]
    'b' -> byte container[1]
    'c' -> byte container[2]
    '\x0' -> byte container[3]

    'd' -> container[4]
    'e' -> container[5]
    'f' -> container[6]
    '\x0' -> container[7]

    'g' -> container[8]
    'h' -> container[9]
    'i' -> container[10]
    '\x0' -> container[11]

    call GetStringWithIndex(container, 0) [result]

    call native printf("getting string works, the string is: %s\n", result as string)