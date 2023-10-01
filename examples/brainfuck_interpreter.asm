Pony!

// Brainfuck interpreter in EASM (and a little bit of native functions :)

import "stdio"
import "string"
import "memory"

struct Instruction
    int operator
    int operand

func compile(file, program) [done]
    array int [512] -> stack
    0 -> stackptr

    call GetCharacter(file) [character]
    character != *EOF -> condition
    pc < 4096 -> checkSize
    and condition, checkSize -> condition

    jump if condition = false to end

    loopHead:

    ptr Instruction program[pc] -> current

    op_incdp:
    jump if character != '>' to op_decdp
    1 -> Instruction current.operator
    jump to switchEnd
    op_decdp:
    jump if character != '<' to op_incval
    2 -> Instruction current.operator
    jump to switchEnd
    op_incval:
    jump if character != '+' to op_decval
    3 -> Instruction current.operator
    jump to switchEnd
    op_decval:
    jump if character != '-' to op_out
    4 -> Instruction current.operator
    jump to switchEnd
    op_out:
    jump if character != '.' to op_in
    5 -> Instruction current.operator
    jump to switchEnd
    op_in:
    jump if character != ',' to op_jmpfwd
    6 -> Instruction current.operator
    jump to switchEnd
    op_jmpfwd:
    jump if character != '[' to op_jmpbck
    7 -> Instruction current.operator
    jump if stackptr = 512 to failure
    pc -> int stack[stackptr]
    inc stackptr
    jump to switchEnd
    op_jmpbck:
    jump if character != ']' to no_op
    jump if stackptr = 0 to failure
    dec stackptr
    int stack[stackptr] -> jmp_pc
    8 -> Instruction current.operator
    jmp_pc -> Instruction current.operand
    ptr Instruction program[jmp_pc] -> jumped
    pc -> Instruction jumped.operand
    jump to switchEnd
    no_op:
    dec pc
    switchEnd:

    inc pc

    call GetCharacter(file) [character]
    character != *EOF -> condition
    pc < 4096 -> checkSize
    and condition, checkSize -> condition

    jump if condition to loopHead

    jump if stackptr != 0 to failure
    jump if pc = 4096 to failure

    ptr Instruction program[pc] -> current
    0 -> Instruction current.operator

    end:
    return true

    failure:
    push false

func execute(program) [done]
    heap [0xFFFF] -> data

    0xFFFF -> pointer
    jump if data = null to end
    
    call SetMemory(data, 0, 0xFFFF) [data]
    0 -> pointer
    
    program -> current
    jump if Instruction current.operator = 0 to end

    loopHead:

    ptr Instruction program[pc] -> current

    op_incdp:
    jump if Instruction current.operator != 1 to op_decdp
    inc pointer
    jump to switchEnd
    op_decdp:
    jump if Instruction current.operator != 2 to op_incval
    dec pointer
    jump to switchEnd
    op_incval:
    jump if Instruction current.operator != 3 to op_decval
    inc data[pointer] 
    jump to switchEnd
    op_decval:
    jump if Instruction current.operator != 4 to op_out
    dec data[pointer]
    jump to switchEnd
    op_out:
    jump if Instruction current.operator != 5 to op_in
    call PrintCharacter(data[pointer]) [result]
    jump to switchEnd
    op_in:
    jump if Instruction current.operator != 6 to op_jmpfwd
    call InputCharacter [data[pointer]]
    jump to switchEnd
    op_jmpfwd:
    jump if Instruction current.operator != 7 to op_jmpbck
    jump if data[pointer] to switchEnd
    Instruction current.operand -> pc
    jump to switchEnd
    op_jmpbck:
    jump if Instruction current.operator != 8 to no_op
    jump if data[pointer] = false to switchEnd
    Instruction current.operand -> pc
    jump to switchEnd
    no_op:
    return false
    switchEnd:

    inc pc

    ptr Instruction program[pc] -> current
    Instruction current.operator != 0 -> condition
    pointer < 0xFFFF -> checkPtr
    and condition, checkPtr -> condition

    jump if condition to loopHead

    end:
    pointer != 0xFFFF -> result
    push result

func main
    heap Instruction [4096] -> program

    jump if program = null to failure

    jump if *argc != 2 to incorrectUsing

    int *argv[] -> argumentsPointer
    call StringSize(argumentsPointer) [executableSize]
    inc executableSize
    add int argumentsPointer, executableSize -> argumentsPointer
    call OpenFile(argumentsPointer, "r") [file]

    jump if file = null to incorrectUsing

    call compile(file, program) [status]

    call CloseFile(file) [result]

    jump if status = false to failure

    call execute(program) [status]

    jump if status to end

    failure:
    call PrintString("Error!\n") [result]

    jump to end

    incorrectUsing:
    call native printf("Usage: executable filename\n")

    end: