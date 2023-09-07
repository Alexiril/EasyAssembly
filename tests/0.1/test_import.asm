Pony!

define set main

import "easmRuntime.asm"
import "tests/test_export.asm"

function main
    100 -> r0
    50 -> r1
    call a
    return
end