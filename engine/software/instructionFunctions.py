from common.definitions import *
from common.types import *
from engine.hardware.components import Registers, InstructionMemory, Memory


def fnc_add(rd: Register, rs: Register, rt: Register):
    val = rs.value + rt.value
    rd.setRegisterValue(val)


def fnc_and(rd: Register, rs: Register, rt: Register):
    val = (rs & rt).value
    rd.setRegisterValue(val)


def fnc_div(rs, rt):
    val_lo = rs.value // rt.value
    val_hi = rs.value % rt.value
    Registers.getRegister('hi').setRegisterValue(val_hi)
    Registers.getRegister('lo').setRegisterValue(val_lo)


def fnc_jalr(rd: Register, rs: Register):
    rd.setRegisterValue(InstructionMemory.PC+4)
    InstructionMemory.PC = rs.value


def fnc_jr(rs: Register):
    InstructionMemory.PC = rs.value


def fnc_mfhi(rd: Register):
    rd.setRegisterValue(Registers.getRegister('hi').value)


def fnc_mflo(rd: Register):
    rd.setRegisterValue(Registers.getRegister('lo').value)


def fnc_mthi(rs: Register):
    Registers.getRegister('hi').setRegisterValue(rs.value)


def fnc_mtlo(rs: Register):
    Registers.getRegister('lo').setRegisterValue(rs.value)


def fnc_mult(rd: Register, rs: Register):
    val = rd.value * rs.value
    val_bit_str = BitString(val, length=64)
    Registers.getRegister('hi').setRegisterValue(val_bit_str[:32].value)
    Registers.getRegister('lo').setRegisterValue(val_bit_str[32:].value)


def fnc_nor(rd: Register, rs: Register, rt: Register):
    val = 2**len(rd) - (rs.value | rt.value)
    rd.setRegisterValue(val)


def fnc_or(rd: Register, rs: Register, rt: Register):
    val = rs.value | rt.value
    rd.setRegisterValue(val)


def fnc_sll(rd: Register, rt: Register, rs_sa):
    sa = rs_sa.value if isinstance(rs_sa, Register) else rs_sa
    val = (rt << sa).value
    rd.setRegisterValue(val)


def fnc_slt(rd: Register, rs: Register, rt: Register):
    val = 1 if rs.value < rt.value else 0
    rd.setRegisterValue(val)


def fnc_sra(rd: Register, rt: Register, rs_sa):
    sa = rs_sa.value if isinstance(rs_sa, Register) else rs_sa
    val = (rt >> sa).value
    rd.setRegisterValue(val)


def fnc_sub(rd, rs, rt):
    val = rs.val - rt.val
    rd.setRegisterValue(val)


def fnc_xor(rd: Register, rs: Register, rt: Register):
    val = rs.value ^ rt.value
    rd.setRegisterValue(val)


def fnc_addi(rt: Register, rs: Register, imm):
    val = rs.value + imm
    rt.setRegisterValue(val)


def fnc_andi(rt: Register, rs: Register, imm):
    val = rs.value & imm
    rt.setRegisterValue(val)


def fnc_beq(rs: Register, rt: Register, imm):
    if rs.value == rt.value:
        InstructionMemory.PC += imm


def fnc_bgez(rs, imm):
    if rs.value >= 0:
        InstructionMemory.PC += imm


def fnc_bgtz(rs, imm):
    if rs.value > 0:
        InstructionMemory.PC += imm


def fnc_blez(rs, imm):
    if rs.value <= 0:
        InstructionMemory.PC += imm


def fnc_bltz(rs, imm):
    if rs.value < 0:
        InstructionMemory.PC += imm


def fnc_bne(rs: Register, rt: Register, imm):
    if rs.value != rt.value:
        InstructionMemory.PC += imm


def fnc_lb(rt: Register, rs: Register, imm):
    val = Memory.loadByte(rs.value, offset=imm)
    if val >= 2**7:
        val = 2**len(rt) - (2**8 - val)
    rt.setRegisterValue(val)


def fnc_lbu(rt: Register, rs: Register, imm):
    val = Memory.loadByte(rs.value, offset=imm)
    rt.setRegisterValue(val)


def fnc_lh(rt: Register, rs: Register, imm):
    val = Memory.loadHalfWord(rs.value, offset=imm)
    if val >= 2**15:
        val = 2**len(rt) - (2**16 - val)
    rt.setRegisterValue(val)


def fnc_lhu(rt: Register, rs: Register, imm):
    val = Memory.loadHalfWord(rs.value, offset=imm)
    rt.setRegisterValue(val)


def fnc_lui(rt: Register, imm):
    val = BitString(imm) << 16
    rt.setRegisterValue(val)


def fnc_lw(rt: Register, rs: Register, imm):
    val = Memory.loadWord(rs.value, offset=imm)
    rt.setRegisterValue(val)


def fnc_ori(rt: Register, rs: Register, imm):
    val = rs.value | imm
    rt.setRegisterValue(val)


def fnc_sb(rt: Register, rs: Register, imm):
    val = rt[24:].value
    Memory.storeByte(rs.value, offset=imm, value=val)


def fnc_slti(rt: Register, rs: Register, imm):
    val = 1 if rs.value < imm else 0
    rt.setRegisterValue(val)


def fnc_sh(rt: Register, rs: Register, imm):
    val = rt[16:].value
    Memory.storeHalfWord(rs.value, offset=imm, value=val)


def fnc_sw(rt: Register, rs: Register, imm):
    val = rt.value
    Memory.storeWord(rs.value, offset=imm, value=val)


def fnc_xori(rt: Register, rs: Register, imm):
    val = rs.value ^ imm
    rt.setRegisterValue(val)


def fnc_j(tgt):
    InstructionMemory.PC = tgt


def fnc_jal(tgt):
    Registers.getRegister('ra').setRegisterValue(InstructionMemory.PC+4)
    InstructionMemory.PC = tgt


instruction_functions = {
    add_: fnc_add,
    addu_: fnc_add,
    and_: fnc_and,
    break_: lambda: None,
    div_: fnc_div,
    divu_: fnc_div,
    jalr_: fnc_jalr,
    jr_: fnc_jr,
    mfhi_: fnc_mfhi,
    mflo_: fnc_mflo,
    mthi_: fnc_mthi,
    mtlo_: fnc_mtlo,
    mult_: fnc_mult,
    multu_: fnc_mult,
    nor_: fnc_nor,
    or_: fnc_or,
    sll_: fnc_sll,
    sllv_: fnc_sll,
    slt_: fnc_slt,
    sltu_: fnc_slt,
    sra_: fnc_sra,
    srav_: fnc_sra,
    srl_: fnc_sra,
    srlv_: fnc_sra,
    sub_: fnc_sub,
    subu_: fnc_sub,
    syscall_: lambda: None,
    xor_: fnc_xor,
    addi_: fnc_addi,
    addiu_: fnc_addi,
    andi_: fnc_andi,
    beq_: fnc_beq,
    bgez_: fnc_bgez,
    bgtz_: fnc_bgtz,
    blez_: fnc_blez,
    bltz_: fnc_bltz,
    bne_: fnc_bne,
    lb_: fnc_lb,
    lbu_: fnc_lbu,
    lh_: fnc_lh,
    lhu_: fnc_lhu,
    lui_: fnc_lui,
    lw_: fnc_lw,
    # lwc1_
    ori_: fnc_ori,
    sb_: fnc_sb,
    slti_: fnc_slti,
    sltiu_: fnc_slti,
    sh_: fnc_sh,
    sw_: fnc_sw,
    # swc1_
    xori_: fnc_xori,
    j_: fnc_j,
    jal_: fnc_jal
}
