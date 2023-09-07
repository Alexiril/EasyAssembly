Pony!

import "easmRuntime.asm"

define only easm2py

function a
    add r0, r1 -> r0
    return
end

function b
    sub i64 r0, i64 r1 -> i64 r0
    return
end

define all
define only easm2c

function a
    sub i64 r0, i64 r1 -> i64 r0
    return
end