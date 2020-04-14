from common.definitions import *
from engine.hardware.components import Registers
from common.types import *


class MIPSAssembler(object):

    # STATIC VARIABLES #
    _current_instructions = None

    # DUNDERS #

    # PROPERTIES #

    # PUBLIC METHODS #
    @staticmethod
    def assembly(source: str) -> str:
        MIPSAssembler._current_instructions = MIPSAssembler._word_parser(
            source)
        MIPSAssembler._setRegisterAddresses()
        MIPSAssembler._setImmediates()
        MIPSAssembler._setMemoryLocations()
        MIPSAssembler._setOpcodes()
        print(MIPSAssembler._current_instructions)

    # PRIVATE METHODS #
    @staticmethod
    def _word_parser(source) -> list:
        lines = [line.split('#')[0].replace('\t', '')
                 for line in source.splitlines()]
        words = []
        for line in lines:
            line_words = []
            for raw_word in line.split():
                if len(raw_word) > 0:
                    line_words.append(raw_word)

            if len(line_words) > 0:
                words.append(line_words)
        return words

    @staticmethod
    def _setOpcodes():
        for instruction in MIPSAssembler._current_instructions:
            opcode = opcodes[instruction[0]]
            instruction[0] = opcode
            if opcode == 0b000_000:
                R_Type()
            elif (opcode >> 1) == 0b000_01:
                J_Type()
            elif (opcode >> 2) == 0b010_0:
                continue
            else:
                I_Type()

    @staticmethod
    def _setRegisterAddresses():
        for instruction in MIPSAssembler._current_instructions:
            for i, word in enumerate(instruction):
                if isinstance(word, str) and word.startswith('$'):
                    try:
                        instruction[i] = Registers.getRegister(
                            word.strip('$,')).register_id
                    except Exception as e:
                        raise e

    @staticmethod
    def _setImmediates():
        for instruction in MIPSAssembler._current_instructions:
            for i, word in enumerate(instruction):
                if isinstance(word, str) and word.isnumeric():
                    instruction[i] = int(word)

    @staticmethod
    def _setMemoryLocations():
        for instruction in MIPSAssembler._current_instructions:
            for i, word in enumerate(instruction):
                if isinstance(word, str) and word.find('(') >= 0:
                    offset_part, address_part = word.split('(', 1)
                    address = address_part.strip(')')
                    instruction[i] = Registers.getRegister(
                        address.strip('$,)')).value + int(offset_part)
