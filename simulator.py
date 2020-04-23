import time

from engine.hardware.components import InstructionMemory, Memory, Registers
from engine.software.instructionFunctions import instruction_functions
from engine.software.mipsAssembler import MIPSAssembler

DELAY = 0.5     # Can be thought as clock cycle time

sample_assembly = """
    ori $t0, $zero, 5   # a = 5
loop:  mult $t0, $t0       # temp = a*a 
    add $t1, $t1, $lo   # b += temp
    addi $t0, $t0, -1   # a += -1
    bgtz $t0, loop       # while a>0
"""

instructions = MIPSAssembler.assembly(sample_assembly)
InstructionMemory.load_instructions(instructions)

while True:
    time.sleep(DELAY)

    current_instruction = InstructionMemory.next_instruction()
    if current_instruction is None:
        print("Done")
        break
    instruction_functions[current_instruction[0]](*current_instruction[1:])

    print(f"PC: {InstructionMemory.PC}\n")
    print("Registers")
    print(f"t0:\t{Registers.getRegister('t0').value}\t" +
          str(Registers.getRegister('t0')))
    print(f"t1:\t{Registers.getRegister('t1').value}\t" +
          str(Registers.getRegister('t1')))
    print(f"lo:\t{Registers.getRegister('lo').value}\t" +
          str(Registers.getRegister('lo')))
    print("\n")
