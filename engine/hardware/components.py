import numpy as np

from common.exceptions import NotAllowedError
from common.types import BitString, Register

_ram_capacity_in_byte = 2**10  # * 32/8 = 1 MB


class Registers(object):

    # STATIC VARIABLES #
    _init_registers = [Register(i) for i in range(34)]
    _registers = {
        'r0':  _init_registers[0],  'zero': _init_registers[0],
        'r1':  _init_registers[1],  'at': _init_registers[1],
        'r2':  _init_registers[2],  'v0': _init_registers[2],
        'r3':  _init_registers[3],  'v1': _init_registers[3],
        'r4':  _init_registers[4],  'a0': _init_registers[4],
        'r5':  _init_registers[5],  'a1': _init_registers[5],
        'r6':  _init_registers[6],  'a2': _init_registers[6],
        'r7':  _init_registers[7],  'a3': _init_registers[7],
        'r8':  _init_registers[8],  't0': _init_registers[8],
        'r9':  _init_registers[9],  't1': _init_registers[9],
        'r10': _init_registers[10], 't2': _init_registers[10],
        'r11': _init_registers[11], 't3': _init_registers[11],
        'r12': _init_registers[12], 't4': _init_registers[12],
        'r13': _init_registers[13], 't5': _init_registers[13],
        'r14': _init_registers[14], 't6': _init_registers[14],
        'r15': _init_registers[15], 't7': _init_registers[15],
        'r16': _init_registers[16], 's0': _init_registers[16],
        'r17': _init_registers[17], 's1': _init_registers[17],
        'r18': _init_registers[18], 's2': _init_registers[18],
        'r19': _init_registers[19], 's3': _init_registers[19],
        'r20': _init_registers[20], 's4': _init_registers[20],
        'r21': _init_registers[21], 's5': _init_registers[21],
        'r22': _init_registers[22], 's6': _init_registers[22],
        'r23': _init_registers[23], 's7': _init_registers[23],
        'r24': _init_registers[24], 't8': _init_registers[24],
        'r25': _init_registers[25], 't9': _init_registers[25],
        'r26': _init_registers[26], 'k0': _init_registers[26],
        'r27': _init_registers[27], 'k1': _init_registers[27],
        'r28': _init_registers[28], 'gp': _init_registers[28],
        'r29': _init_registers[29], 'sp': _init_registers[29],
        'r30': _init_registers[30], 'fp': _init_registers[30],
        'r31': _init_registers[31], 'ra': _init_registers[31],
        'lo':  _init_registers[32], 'hi': _init_registers[33],
    }
    _registers['sp'].setRegisterValue(_ram_capacity_in_byte * 4)

    # DUNDERS #

    # PROPERTIES #

    # PUBLIC METHODS #
    @staticmethod
    def getRegister(register_id: str) -> Register:
        if isinstance(register_id, int):
            return Registers._init_registers[register_id]
        return Registers._registers[register_id]

    @staticmethod
    def resetRegisters():
        for register in Registers._init_registers:
            register.setRegisterValue(0)
        Registers._registers['sp'].setRegisterValue(
            _ram_capacity_in_byte * 4)

    # PRIVATE METHODS #


class Memory(object):

    # STATIC VARIABLES #
    _memory = np.zeros((_ram_capacity_in_byte,), dtype=np.uint32)

    # DUNDERS #

    # PROPERTIES #

    # PUBLIC METHODS #
    @staticmethod
    def loadByte(address, offset=0) -> int:
        primary_index = ((address + offset) // 4) % _ram_capacity_in_byte
        secondary_index = (address + offset) % 4

        word = BitString(Memory._memory[primary_index])

        return word[secondary_index*8:secondary_index*8 + 8].value

    @staticmethod
    def storeByte(address, offset=0, value=0):
        primary_index = ((address + offset) // 4) % _ram_capacity_in_byte
        secondary_index = (address + offset) % 4

        word = BitString(Memory._memory[primary_index])
        adding_string = BitString(value, length=8)

        word[secondary_index*8:(secondary_index+1)*8] = adding_string
        Memory._memory[primary_index] = word.value

    @staticmethod
    def loadHalfWord(address, offset=0) -> int:
        return (Memory.loadByte(address, offset) << 8) + \
            Memory.loadByte(address, offset+1)

    @staticmethod
    def storeHalfWord(address, offset=0, value=0):
        adding_string = BitString(value, 16)
        Memory.storeByte(address, offset, adding_string[:8].value)
        Memory.storeByte(address, offset+1, adding_string[8:].value)

    @staticmethod
    def loadWord(address, offset=0) -> int:
        return (Memory.loadByte(address, offset) << 24) + \
            (Memory.loadByte(address, offset+1) << 16) + \
            (Memory.loadByte(address, offset+2) << 8) + \
            Memory.loadByte(address, offset+3)

    @staticmethod
    def storeWord(address, offset=0, value=0):
        adding_string = BitString(value)
        Memory.storeByte(address, offset, adding_string[:8].value)
        Memory.storeByte(address, offset+1, adding_string[8:16].value)
        Memory.storeByte(address, offset+2, adding_string[16:24].value)
        Memory.storeByte(address, offset+3, adding_string[24:].value)

    @staticmethod
    def resetMemory():
        Memory._memory = np.zeros((_ram_capacity_in_byte,), dtype=np.uint32)

    # PRIVATE METHODS #


class InstructionMemory(object):

    # STATIC VARIABLES #
    PC = 0
    _instructions: list = []

    # DUNDERS #

    # PROPERTIES #

    # PUBLIC METHODS #
    @staticmethod
    def load_instructions(instructions: list):
        InstructionMemory._instructions = instructions[:]
        InstructionMemory.PC = 0

    @staticmethod
    def next_instruction() -> list:
        InstructionMemory.PC += 4
        try:
            return InstructionMemory._instructions[(InstructionMemory.PC-4)//4]
        except IndexError as e:
            return None

    # PRIVATE METHODS #
