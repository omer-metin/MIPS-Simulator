from engine.hardware.components import InstructionMemory
from engine.software.instructionFunctions import instruction_functions


class Processor(object):

    # STATIC VARIABLES #

    # DUNDERS #

    # PROPERTIES #

    # PUBLIC METHODS #
    @staticmethod
    def processNext():
        current_instruction = InstructionMemory.next_instruction()
        if current_instruction is None:
            return None

        raw_changed_regs, changed_mems = instruction_functions[
            current_instruction[0]](*current_instruction[1:])

        changed_regs = []
        for reg_id, old_reg in raw_changed_regs:
            if reg_id == 32:
                changed_regs.append((33, old_reg))
            elif reg_id == 33:
                changed_regs.append((16, old_reg))
            elif reg_id > 16:
                changed_regs.append((reg_id+1, old_reg))
            else:
                changed_regs.append((reg_id, old_reg))

        return changed_regs, changed_mems

    # PRIVATE METHODS #
