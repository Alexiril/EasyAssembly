Pony!

// That's a comment here.

import native easm2c "stdio.h"

function math_test
    add r0, r1 -> r2
    sub r0, r1 -> r3
    mul r0, r1 -> r4
    div r0, r1 -> r5
    rem r0, r1 -> r6

    add i64 r0, i64 r1 -> i64 r7
    sub i64 r0, i64 r1 -> i64 r8
    mul i64 r0, i64 r1 -> i64 r9
    div i64 r0, i64 r1 -> i64 r10
    rem i64 r0, i64 r1 -> i64 r11

    add f32 r0, f32 r1 -> f32 r12
    sub f32 r0, f32 r1 -> f32 r13
    mul f32 r0, f32 r1 -> f32 r14
    div f32 r0, f32 r1 -> f32 r15
end

function add_params
    r0 -> r5
    r1 -> r6

    add r5, r6 -> r0
end

function main
    17° -> f64 r0
    stack push r0

    ptr "17 degrees = %f radians\n" -> r1

    invoke printf(u64 r1 as "const char*", f64 r0) // TODO: need to create free type cast system

    20 -> r0
    stack push r0

    stack size -> r1
    stack pop r2
    stack push r2
    invoke printf(
        "stack size is %lld and top is %lld\n", u64 r1, u64 r2)

    2 -> r0
    1.5f -> f32 r1

    call math_test

    invoke printf("something %lld\n", u64 r0)

    5 -> r0
    -1 -> i64 r1

    myData init r0

    ptr myData -> r9

    r9[] -> r10
    r9[r10] -> r10

    $LoopHead

    call add_params

    jump if (r0 != 0) $LoopHead

    stack pop r10

    shift r r0, 2 -> r0
    shift l r0, 2 -> r0

    u'°' -> r0
    ptr u8"some ° here" -> r0

    xor r0, r0 -> r0
end