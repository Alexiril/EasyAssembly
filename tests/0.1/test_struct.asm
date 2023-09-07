Pony!

structure Point x, y, z end

structure Line p1, p2 end

structure Simplex l1, l2, l3 end

function main
    pass easm2c "int somevariable = 3;"

    ptr r0 -> r10

    new Point -> r0
    myPoint init r0
    5 -> Point r0 : x
    0 -> Point r0 : y
    0 -> Point r0 : z

    new shared Point -> r0
    myPoint2 init r0
    3 -> Point r0 : x
    2 -> Point r0 : y
    1 -> Point r0 : z

    new Line -> r0
    myPoint -> Line r0 : p1
    myPoint2 -> Line r0 : p2

    Point myPoint : x -> r0

    delete myPoint
end