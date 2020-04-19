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
        instructions = MIPSAssembler._setOpcodes()

        machine_codes = []
        for instruction in instructions:
            machine_codes.append(instruction.toMachineCode())

        return machine_codes

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
    def _setOpcodes() -> list:
        instructions = []
        for instruction in MIPSAssembler._current_instructions:
            instruction_key = instruction[0]
            opcode = opcodes[instruction_key]
            instruction[0] = opcode
            inst_dict: dict = instruction_machinecode_orders[instruction_key]
            if opcode == 0b000_000:
                inst_dict.update(dict(
                    zip(instruction_assembly_orders[instruction_key],
                        instruction)))
                instructions.append(R_Type(**inst_dict))
            elif (opcode >> 1) == 0b000_01:
                inst_dict.update(dict(
                    zip(instruction_assembly_orders[instruction_key],
                        instruction)))
                instructions.append(J_Type(**inst_dict))
            elif (opcode >> 2) == 0b010_0:
                continue
            else:
                inst_dict.update(dict(
                    zip(instruction_assembly_orders[instruction_key],
                        instruction)))
                instructions.append(I_Type(**inst_dict))

        return instructions

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
                        address.strip('$,)')).register_id
                    instruction.append(int(offset_part))
