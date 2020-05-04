from common.definitions import *
from common.types import *
from engine.hardware.components import InstructionMemory, Memory, Registers


def fnc_add(rd: Register, rs: Register, rt: Register):
    val = rs.value + rt.value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_and(rd: Register, rs: Register, rt: Register):
    val = (rs & rt).value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_div(rs, rt):
    val_lo = rs.value // rt.value
    val_hi = rs.value % rt.value
    lo_old = Registers.getRegister('lo').signedValue
    hi_old = Registers.getRegister('hi').signedValue
    Registers.getRegister('hi').setRegisterValue(val_hi)
    Registers.getRegister('lo').setRegisterValue(val_lo)
    return ([(Registers.getRegister('hi').register_id, hi_old),
             (Registers.getRegister('lo').register_id, lo_old)], [])


def fnc_jalr(rd: Register, rs: Register):
    rd_old = rd.signedValue
    rd.setRegisterValue(InstructionMemory.PC)
    InstructionMemory.PC = rs.value
    return ([(rd.register_id, rd_old)], [])


def fnc_jr(rs: Register):
    InstructionMemory.PC = rs.value
    return ([], [])


def fnc_mfhi(rd: Register):
    rd_old = rd.signedValue
    rd.setRegisterValue(Registers.getRegister('hi').value)
    return ([(rd.register_id, rd_old)], [])


def fnc_mflo(rd: Register):
    rd_old = rd.signedValue
    rd.setRegisterValue(Registers.getRegister('lo').value)
    return ([(rd.register_id, rd_old)], [])


def fnc_mthi(rs: Register):
    hi_old = Registers.getRegister('hi').signedValue
    Registers.getRegister('hi').setRegisterValue(rs.value)
    return ([(Registers.getRegister('hi').register_id, hi_old)], [])


def fnc_mtlo(rs: Register):
    lo_old = Registers.getRegister('lo').signedValue
    Registers.getRegister('lo').setRegisterValue(rs.value)
    return ([(Registers.getRegister('lo').register_id, lo_old)], [])


def fnc_mult(rd: Register, rs: Register):
    val = rd.value * rs.value
    val_bit_str = BitString(val, length=64)
    lo_old = Registers.getRegister('lo').signedValue
    hi_old = Registers.getRegister('hi').signedValue
    Registers.getRegister('hi').setRegisterValue(val_bit_str[:32].value)
    Registers.getRegister('lo').setRegisterValue(val_bit_str[32:].value)
    return ([(Registers.getRegister('hi').register_id, hi_old),
             (Registers.getRegister('lo').register_id, lo_old)], [])


def fnc_nor(rd: Register, rs: Register, rt: Register):
    val = 2**len(rd) - (rs.value | rt.value)
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_or(rd: Register, rs: Register, rt: Register):
    val = rs.value | rt.value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_sll(rd: Register, rt: Register, rs_sa):
    sa = rs_sa.value if isinstance(rs_sa, Register) else rs_sa
    val = (rt << sa).value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_slt(rd: Register, rs: Register, rt: Register):
    val = 1 if rs.value < rt.value else 0
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_sra(rd: Register, rt: Register, rs_sa):
    sa = rs_sa.value if isinstance(rs_sa, Register) else rs_sa
    val = (rt >> sa).value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_sub(rd, rs, rt):
    val = rs.value - rt.value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_xor(rd: Register, rs: Register, rt: Register):
    val = rs.value ^ rt.value
    rd_old = rd.signedValue
    rd.setRegisterValue(val)
    return ([(rd.register_id, rd_old)], [])


def fnc_addi(rt: Register, rs: Register, imm):
    val = rs.value + imm
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_andi(rt: Register, rs: Register, imm):
    val = rs.value & imm
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_beq(rs: Register, rt: Register, imm):
    if rs.value == rt.value:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_bgez(rs, imm):
    if rs.value >= 0:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_bgtz(rs, imm):
    if rs.value > 0:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_blez(rs, imm):
    if rs.value <= 0:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_bltz(rs, imm):
    if rs.value < 0:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_bne(rs: Register, rt: Register, imm):
    if rs.value != rt.value:
        InstructionMemory.PC += imm
    return ([], [])


def fnc_lb(rt: Register, rs: Register, imm):
    val = Memory.loadByte(rs.value, offset=imm)
    if val >= 2**7:
        val = 2**len(rt) - (2**8 - val)
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_lbu(rt: Register, rs: Register, imm):
    val = Memory.loadByte(rs.value, offset=imm)
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_lh(rt: Register, rs: Register, imm):
    val = Memory.loadHalfWord(rs.value, offset=imm)
    if val >= 2**15:
        val = 2**len(rt) - (2**16 - val)
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_lhu(rt: Register, rs: Register, imm):
    val = Memory.loadHalfWord(rs.value, offset=imm)
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_lui(rt: Register, imm):
    val = BitString(imm) << 16
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_lw(rt: Register, rs: Register, imm):
    val = Memory.loadWord(rs.value, offset=imm)
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_ori(rt: Register, rs: Register, imm):
    val = rs.value | imm
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_sb(rt: Register, rs: Register, imm):
    val = rt[24:].value
    mem_old = Memory.loadByte(rs.value, offset=imm)
    Memory.storeByte(rs.value, offset=imm, value=val)
    return ([], [(rs.value + imm, mem_old)])


def fnc_slti(rt: Register, rs: Register, imm):
    val = 1 if rs.value < imm else 0
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_sh(rt: Register, rs: Register, imm):
    val = rt[16:].value
    mem1_old = Memory.loadByte(rs.value, offset=imm)
    mem2_old = Memory.loadByte(rs.value, offset=imm+1)
    Memory.storeHalfWord(rs.value, offset=imm, value=val)
    return ([], [(rs.value + imm, mem1_old), (rs.value + imm + 1, mem2_old)])


def fnc_sw(rt: Register, rs: Register, imm):
    val = rt.value
    mem1_old = Memory.loadByte(rs.value, offset=imm)
    mem2_old = Memory.loadByte(rs.value, offset=imm+1)
    mem3_old = Memory.loadByte(rs.value, offset=imm+2)
    mem4_old = Memory.loadByte(rs.value, offset=imm+3)
    Memory.storeWord(rs.value, offset=imm, value=val)
    return ([], [(rs.value + imm, mem1_old), (rs.value + imm + 1, mem2_old),
                 (rs.value + imm + 2, mem3_old), (rs.value + imm + 3, mem4_old)])


def fnc_xori(rt: Register, rs: Register, imm):
    val = rs.value ^ imm
    rt_old = rt.signedValue
    rt.setRegisterValue(val)
    return ([(rt.register_id, rt_old)], [])


def fnc_j(tgt):
    InstructionMemory.PC = tgt
    return ([], [])


def fnc_jal(tgt):
    ra_old = Registers.getRegister('ra').signedValue
    Registers.getRegister('ra').setRegisterValue(InstructionMemory.PC)
    InstructionMemory.PC = tgt
    return ([(Registers.getRegister('ra').register_id, ra_old)], [])


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
