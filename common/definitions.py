# R Types #
_add = 'add'
_addu = 'addu'
_and = 'and'
_break = 'break'
_div = 'div'
_divu = 'divu'
_jalr = 'jalr'
_jr = 'jr'
_mfhi = 'mfhi'
_mflo = 'mflo'
_mthi = 'mthi'
_mtlo = 'mtlo'
_mult = 'mult'
_multu = 'multu'
_nor = 'nor'
_or = 'or'
_sll = 'sll'
_sllv = 'sllv'
_slt = 'slt'
_sltu = 'sltu'
_sra = 'sra'
_srav = 'srav'
_srl = 'srl'
_srlv = 'srlv'
_sub = 'sub'
_subu = 'subu'
_syscall = 'syscall'
_xor = 'xor'

# I Types #
_addi = 'addi'
_addiu = 'addiu'
_andi = 'andi'
_beq = 'beq'
_bgez = 'bgez'
_bgtz = 'bgtz'
_blez = 'blez'
_bltz = 'bltz'
_bne = 'bne'
_lb = 'lb'
_lbu = 'lbu'
_lh = 'lh'
_lhu = 'lhu'
_lui = 'lui'
_lw = 'lw'
_lwc1 = 'lwc1'
_ori = 'ori'
_sb = 'sb'
_slti = 'slti'
_sltiu = 'sltiu'
_sh = 'sh'
_sw = 'sw'
_swc1 = 'swc1'
_xori = 'xori'

# J Types #
_j = 'j'
_jal = 'jal'

opcodes = dict([
    # R Types #
    (_add,      0b000_000),
    (_addu,     0b000_000),
    (_and,      0b000_000),
    (_break,    0b000_000),
    (_div,      0b000_000),
    (_divu,     0b000_000),
    (_jalr,     0b000_000),
    (_jr,       0b000_000),
    (_mfhi,     0b000_000),
    (_mflo,     0b000_000),
    (_mthi,     0b000_000),
    (_mtlo,     0b000_000),
    (_mult,     0b000_000),
    (_multu,    0b000_000),
    (_nor,      0b000_000),
    (_or,       0b000_000),
    (_sll,      0b000_000),
    (_sllv,     0b000_000),
    (_slt,      0b000_000),
    (_sltu,     0b000_000),
    (_sra,      0b000_000),
    (_srav,     0b000_000),
    (_srl,      0b000_000),
    (_srlv,     0b000_000),
    (_sub,      0b000_000),
    (_subu,     0b000_000),
    (_syscall,  0b000_000),
    (_xor,      0b000_000),
    # I Types #
    (_addi,     0b001_000),
    (_addiu,    0b001_001),
    (_andi,     0b001_100),
    (_beq,      0b000_100),
    (_bgez,     0b000_001),
    (_bgtz,     0b000_111),
    (_blez,     0b000_110),
    (_bltz,     0b000_001),
    (_bne,      0b000_101),
    (_lb,       0b100_000),
    (_lbu,      0b100_100),
    (_lh,       0b100_001),
    (_lhu,      0b100_101),
    (_lui,      0b001_111),
    (_lw,       0b100_011),
    (_lwc1,     0b110_001),
    (_ori,      0b001_101),
    (_sb,       0b101_000),
    (_slti,     0b001_010),
    (_sltiu,    0b001_011),
    (_sh,       0b101_001),
    (_sw,       0b101_011),
    (_swc1,     0b111_001),
    (_xori,     0b001_110),
    # J Types #
    (_j,        0b000_010),
    (_jal,      0b000_011)
])


rd = 'rd'
rs = 'rs'
rt = 'rt'
sa = 'sa'
imm = 'immediate'
tgt = 'target_address'
fun = 'funct'
opc = 'opcode'

instruction_machinecode_orders = dict([
    (_add,      {opc: 0b000_000, sa: 0, fun: 0b100_000}),
    (_addu,     {opc: 0b000_000, sa: 0, fun: 0b100_001}),
    (_and,      {opc: 0b000_000, sa: 0, fun: 0b100_100}),
    (_break,    {opc: 0b000_000, rd: 0, rs: 0, rt: 0, sa: 0, fun: 0b001_101}),
    (_div,      {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_010}),
    (_divu,     {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_011}),
    (_jalr,     {opc: 0b000_000, rt: 0, sa: 0, fun: 0b001_001}),
    (_jr,       {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b001_000}),
    (_mfhi,     {opc: 0b000_000, rs: 0, rt: 0, sa: 0, fun: 0b010_000}),
    (_mflo,     {opc: 0b000_000, rs: 0, rt: 0, sa: 0, fun: 0b010_010}),
    (_mthi,     {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b010_001}),
    (_mtlo,     {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b010_011}),
    (_mult,     {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_000}),
    (_multu,    {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_001}),
    (_nor,      {opc: 0b000_000, sa: 0, fun: 0b100_111}),
    (_or,       {opc: 0b000_000, sa: 0, fun: 0b100_101}),
    (_sll,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (_sllv,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (_slt,      {opc: 0b000_000, sa: 0, fun: 0b101_010}),
    (_sltu,     {opc: 0b000_000, sa: 0, fun: 0b101_011}),
    (_sra,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (_srav,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (_srl,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (_srlv,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (_sub,      {opc: 0b000_000, sa: 0, fun: 0b100_010}),
    (_subu,     {opc: 0b000_000, sa: 0, fun: 0b100_011}),
    (_syscall,  {opc: 0b000_000, rd: 0, rs: 0, rt: 0, sa: 0, fun: 0b001_100}),
    (_xor,      {opc: 0b000_000, sa: 0, fun: 0b10_0110}),

    (_addi,     {opc: 0b001_000}),
    (_addiu,    {opc: 0b001_001}),
    (_andi,     {opc: 0b001_100}),
    (_beq,      {opc: 0b000_100}),
    (_bgez,     {opc: 0b000_001, rt: 0}),
    (_bgtz,     {opc: 0b000_111, rt: 0}),
    (_blez,     {opc: 0b000_110, rt: 0}),
    (_bltz,     {opc: 0b000_001, rt: 0}),
    (_bne,      {opc: 0b000_101}),
    (_lb,       {opc: 0b100_000}),
    (_lbu,      {opc: 0b100_100}),
    (_lh,       {opc: 0b100_001}),
    (_lhu,      {opc: 0b100_101}),
    (_lui,      {opc: 0b001_111}),
    (_lw,       {opc: 0b100_011}),
    (_lwc1,     {opc: 0b110_001}),
    (_ori,      {opc: 0b001_101}),
    (_sb,       {opc: 0b101_000, rs: 0}),
    (_slti,     {opc: 0b001_010}),
    (_sltiu,    {opc: 0b001_011}),
    (_sh,       {opc: 0b101_001, rs: 0}),
    (_sw,       {opc: 0b101_011, rs: 0}),
    (_swc1,     {opc: 0b111_001, rs: 0}),
    (_xori,     {opc: 0b001_110}),

    (_j,        {opc: 0b000_010}),
    (_jal,      {opc: 0b000_011})
])

instruction_assembly_orders = dict([
    (_add,      [opc, rd, rs, rt, fun]),
    (_addu,     [opc, rd, rs, rt, fun]),
    (_and,      [opc, rd, rs, rt, fun]),
    (_break,    [opc, fun]),
    (_div,      [opc, rs, rt, fun, fun]),
    (_divu,     [opc, rs, rt, fun]),
    (_jalr,     [opc, rd, rs, fun]),
    (_jr,       [opc, rs, fun]),
    (_mfhi,     [opc, rd, fun]),
    (_mflo,     [opc, rd, fun]),
    (_mthi,     [opc, rs, fun]),
    (_mtlo,     [opc, rs, fun]),
    (_mult,     [opc, rs, rt, fun]),
    (_multu,    [opc, rs, rt, fun]),
    (_nor,      [opc, rd, rs, rt, fun]),
    (_or,       [opc, rd, rs, rt, fun]),
    (_sll,      [opc, rt, rt, sa, fun]),
    (_sllv,     [opc, rd, rt, rs, fun]),
    (_slt,      [opc, rd, rs, rt, fun]),
    (_sltu,     [opc, rd, rs, rt, fun]),
    (_sra,      [opc, rd, rt, sa, fun]),
    (_srav,     [opc, rd, rt, rs, fun]),
    (_srl,      [opc, rd, rt, sa, fun]),
    (_srlv,     [opc, rd, rt, rs, fun]),
    (_sub,      [opc, rd, rs, rt, fun]),
    (_subu,     [opc, rd, rs, rt, fun]),
    (_syscall,  [opc, fun]),
    (_xor,      [opc, rd, rs, rt, fun]),

    (_addi,     [opc, rt, rs, imm]),
    (_addiu,    [opc, rt, rs, imm]),
    (_andi,     [opc, rt, rs, imm]),
    (_beq,      [opc, rs, rt, imm]),
    (_bgez,     [opc, rs, imm]),
    (_bgtz,     [opc, rs, imm]),
    (_blez,     [opc, rs, imm]),
    (_bltz,     [opc, rs, imm]),
    (_bne,      [opc, rs, rt, imm]),
    (_lb,       [opc, rt, rs, imm]),
    (_lbu,      [opc, rt, rs, imm]),
    (_lh,       [opc, rt, rs, imm]),
    (_lhu,      [opc, rt, rs, imm]),
    (_lui,      [opc, rt, rs, imm]),
    (_lw,       [opc, rt, rs, imm]),
    (_lwc1,     [opc, rt, rs, imm]),
    (_ori,      [opc, rt, rs, imm]),
    (_sb,       [opc, rt, imm]),
    (_slti,     [opc, rt, rs, imm]),
    (_sltiu,    [opc, rt, rs, imm]),
    (_sh,       [opc, rt, imm]),
    (_sw,       [opc, rt, imm]),
    (_swc1,     [opc, rt, imm]),
    (_xori,     [opc, rt, rs, imm]),

    (_j,        [opc, tgt]),
    (_jal,      [opc, tgt])
])
